from pathlib import Path

import polars as pl
from polars.testing import assert_frame_equal
from pytest import fixture, raises

from seedcase_sprout import write_properties
from seedcase_sprout.build_resources import build_resources
from seedcase_sprout.config import BuildResourcesConfig, Config, ResourceConfig
from seedcase_sprout.properties import (
    FieldProperties,
    FieldType,
    LicenseProperties,
    ResourceProperties,
    SproutProperties,
    TableSchemaProperties,
)


def package_properties(visit_id_type: FieldType = "integer") -> SproutProperties:
    return SproutProperties.from_default(
        name="test",
        title="test",
        description="test",
        licenses=[LicenseProperties(name="test")],
        resources=[
            ResourceProperties(
                name="resource-1",
                title="test",
                description="test",
                schema=TableSchemaProperties(
                    primary_key=["participant_id", "visit_id"],
                    fields=[
                        FieldProperties(name="participant_id", type="string"),
                        FieldProperties(name="visit_id", type=visit_id_type),
                        FieldProperties(name="other_col", type="number"),
                    ],
                ),
            ),
            ResourceProperties(
                name="resource-2",
                title="test",
                description="test",
                schema=TableSchemaProperties(
                    primary_key=["participant_id", "visit_id"],
                    fields=[
                        FieldProperties(name="participant_id", type="string"),
                        FieldProperties(name="visit_id", type=visit_id_type),
                        FieldProperties(name="other_col", type="boolean"),
                    ],
                ),
            ),
        ],
    )


@fixture
def _config(tmp_path) -> Config:
    return Config(
        build_resources=BuildResourcesConfig(
            delete_obs_units_file=Path("units.csv"),
            resources=[
                ResourceConfig(
                    name="resource-1",
                    input_dir=Path("staging") / "resource-1",
                    output_dir=Path("output-folder"),
                    extras={"key": "value"},
                ),
                ResourceConfig(
                    name="resource-2",
                    input_dir=tmp_path / "other-staging" / "resource-2",
                    output_dir=tmp_path / "other-output-folder",
                    extras={"key": "value"},
                ),
            ],
        ),
    )


@fixture
def _units_csv(tmp_path) -> Path:
    (tmp_path / "units.csv").write_text("participant_id,visit_id\na,2\nc,5")
    return tmp_path / "units.csv"


@fixture
def _datapackage_json(tmp_path) -> Path:
    return write_properties(package_properties(), tmp_path / "datapackage.json")


resource_1_df = pl.DataFrame(
    {
        "participant_id": ["a", "a", "b", "c"],
        "visit_id": [1, 2, 1, 1],
        "other_col": [2.3, 4.3, 5.0, None],
    }
)


@fixture
def _resource_1_data(tmp_path, _config) -> Path:
    input_dir = tmp_path / _config.build_resources.resources[0].input_dir
    input_dir.mkdir(parents=True, exist_ok=True)
    pl.DataFrame(
        {
            "participant_id": ["a", "a", "b", "c"],
            "visit_id": [1, 2, 1, 1],
            "other_col": [2.3, 4.3, 0, None],
        }
    ).write_parquet(input_dir / "2025-09-08T092401Z.parquet")
    # ID (b, 1) corrected to 5.0
    resource_1_df.write_parquet(input_dir / "2026-09-08T092401Z.parquet")
    return input_dir


resource_2_df = pl.DataFrame(
    {
        "participant_id": ["a", "a", "b", "c"],
        "visit_id": [1, 2, 1, 5],
        "other_col": [True, False, True, False],
    }
)


@fixture
def _resource_2_data(tmp_path, _config) -> Path:
    input_dir = tmp_path / _config.build_resources.resources[1].input_dir
    input_dir.mkdir(parents=True, exist_ok=True)
    resource_2_df.write_parquet(input_dir / "2026-09-09T133400Z.parquet")
    return input_dir


def test_combines_staged_resources_and_excludes_deleted_obs_units(
    tmp_path, _config, _datapackage_json, _units_csv, _resource_1_data, _resource_2_data
):
    resources = _config.build_resources.resources

    output_paths = build_resources(_config, tmp_path)

    assert output_paths == [
        tmp_path / "output-folder" / f"{resources[0].name}.parquet",
        tmp_path / "other-output-folder" / f"{resources[1].name}.parquet",
    ]
    assert_frame_equal(
        pl.read_parquet(output_paths[0]),
        pl.DataFrame(
            {
                "participant_id": ["a", "b", "c"],
                "visit_id": [1, 1, 1],
                "other_col": [2.3, 5.0, None],
            }
        ),
        check_row_order=False,
    )
    assert_frame_equal(
        pl.read_parquet(output_paths[1]),
        pl.DataFrame(
            {
                "participant_id": ["a", "b"],
                "visit_id": [1, 1],
                "other_col": [True, True],
            }
        ),
        check_row_order=False,
    )


def test_no_rows_excluded_when_no_units_file_in_config(
    tmp_path, _units_csv, _datapackage_json, _resource_1_data, _resource_2_data
):
    config = Config(
        build_resources=BuildResourcesConfig(
            resources=[
                ResourceConfig(
                    name="resource-1",
                    input_dir=Path("staging") / "resource-1",
                    output_dir=Path("output-folder"),
                    extras={"key": "value"},
                ),
                ResourceConfig(
                    name="resource-2",
                    input_dir=tmp_path / "other-staging" / "resource-2",
                    output_dir=tmp_path / "other-output-folder",
                    extras={"key": "value"},
                ),
            ],
        ),
    )

    output_paths = build_resources(config, tmp_path)

    _assert_no_rows_excluded(output_paths)


def test_no_rows_excluded_when_units_file_header_only(
    tmp_path, _config, _datapackage_json, _resource_1_data, _resource_2_data
):
    (tmp_path / "units.csv").write_text("participant_id,visit_id")

    output_paths = build_resources(_config, tmp_path)

    _assert_no_rows_excluded(output_paths)


def test_no_rows_excluded_when_no_ids_match(
    tmp_path, _config, _datapackage_json, _resource_1_data, _resource_2_data
):
    (tmp_path / "units.csv").write_text("participant_id,visit_id\na,3\nd,1")

    output_paths = build_resources(_config, tmp_path)

    _assert_no_rows_excluded(output_paths)


def test_errors_when_units_file_empty(
    tmp_path, _config, _datapackage_json, _resource_1_data, _resource_2_data
):
    (tmp_path / "units.csv").touch()

    with raises(pl.exceptions.NoDataError):
        build_resources(_config, tmp_path)


def test_errors_when_units_file_not_csv(
    tmp_path, _datapackage_json, _resource_1_data, _resource_2_data
):
    config = Config(
        build_resources=BuildResourcesConfig(delete_obs_units_file=Path("units.json")),
    )

    with raises(ValueError, match="CSV"):
        build_resources(config, tmp_path)


def test_errors_if_units_file_does_not_match_properties(
    tmp_path, _config, _datapackage_json
):
    (tmp_path / "units.csv").write_text("participant_id,some_id\na,2\nc,5")

    with raises(ValueError, match="not present"):
        build_resources(_config, tmp_path)


def test_resources_not_processed_if_nulls_in_units_file(
    tmp_path, _config, _datapackage_json, _resource_1_data, _resource_2_data
):
    (tmp_path / "units.csv").write_text("participant_id,visit_id\na,2\nc,")

    assert build_resources(_config, tmp_path) == []
    assert not _config.build_resources.resources[0].output_dir.exists()
    assert not _config.build_resources.resources[1].output_dir.exists()


def test_resources_not_processed_if_data_does_not_match_properties(
    tmp_path, _config, _units_csv, _resource_1_data, _resource_2_data
):
    write_properties(
        package_properties(visit_id_type="string"), tmp_path / "datapackage.json"
    )

    assert build_resources(_config, tmp_path) == []


def test_failing_resource_does_not_break_flow(
    tmp_path, _config, _datapackage_json, _units_csv, _resource_2_data
):
    output_paths = build_resources(_config, tmp_path)

    assert len(output_paths) == 1
    assert not _config.build_resources.resources[0].output_dir.exists()
    assert_frame_equal(
        pl.read_parquet(output_paths[0]),
        pl.DataFrame(
            {
                "participant_id": ["a", "b"],
                "visit_id": [1, 1],
                "other_col": [True, True],
            }
        ),
        check_row_order=False,
    )


def _assert_no_rows_excluded(output_paths: list[Path]) -> None:
    assert_frame_equal(
        pl.read_parquet(output_paths[0]), resource_1_df, check_row_order=False
    )
    assert_frame_equal(
        pl.read_parquet(output_paths[1]), resource_2_df, check_row_order=False
    )
