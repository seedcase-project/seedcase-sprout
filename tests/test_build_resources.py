from pathlib import Path

import polars as pl
from polars.testing import assert_frame_equal
from pytest import fixture

from seedcase_sprout import write_properties
from seedcase_sprout.build_resources import build_resources
from seedcase_sprout.config import BuildResourcesConfig, Config, ResourceConfig
from seedcase_sprout.properties import (
    FieldProperties,
    LicenseProperties,
    ResourceProperties,
    SproutProperties,
    TableSchemaProperties,
)


def sprout_config(base_path: Path) -> Config:
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
                    input_dir=base_path / "other-staging" / "resource-2",
                    output_dir=base_path / "other-output-folder",
                    extras={"key": "value"},
                ),
            ],
        ),
    )


package_properties = SproutProperties.from_default(
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
                fields=[
                    FieldProperties(name="participant_id", type="string"),
                    FieldProperties(name="visit_id", type="integer"),
                    FieldProperties(name="other_col", type="number"),
                ]
            ),
        ),
        ResourceProperties(
            name="resource-2",
            title="test",
            description="test",
            schema=TableSchemaProperties(
                fields=[
                    FieldProperties(name="participant_id", type="string"),
                    FieldProperties(name="visit_id", type="integer"),
                    FieldProperties(name="other_col", type="boolean"),
                ]
            ),
        ),
    ],
)


@fixture
def _units_csv(tmp_path) -> Path:
    (tmp_path / "units.csv").write_text("participant_id,visit_id\na,2\nc,5")
    return tmp_path / "units.csv"


@fixture
def _datapackage_json(tmp_path) -> Path:
    return write_properties(package_properties, tmp_path / "datapackage.json")


@fixture
def _resource_1_data(tmp_path) -> Path:
    data_path = (
        tmp_path
        / sprout_config(tmp_path).build_resources.resources[0].input_dir
        / "2026-09-08T092401Z.parquet"
    )
    data_path.parent.mkdir(parents=True, exist_ok=True)
    pl.DataFrame(
        {
            "participant_id": ["a", "a", "b", "c"],
            "visit_id": [1, 2, 1, 1],
            "other_col": [2.3, 4.3, 5.0, None],
        }
    ).write_parquet(data_path)
    return data_path


@fixture
def _resource_2_data(tmp_path) -> Path:
    data_path = (
        sprout_config(tmp_path).build_resources.resources[1].input_dir
        / "2026-09-09T133400Z.parquet"
    )
    data_path.parent.mkdir(parents=True, exist_ok=True)
    pl.DataFrame(
        {
            "participant_id": ["a", "a", "b", "c"],
            "visit_id": [1, 2, 1, 5],
            "other_col": [True, False, True, False],
        }
    ).write_parquet(data_path)
    return data_path


def test_excludes_deleted_obs_units(
    tmp_path, _datapackage_json, _units_csv, _resource_1_data, _resource_2_data
):
    config = sprout_config(tmp_path)
    resources = config.build_resources.resources

    output_paths = build_resources(config, tmp_path)

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


def test_failing_resource_does_not_break_flow(
    tmp_path, _datapackage_json, _units_csv, _resource_2_data
):
    config = sprout_config(tmp_path)

    output_paths = build_resources(config, tmp_path)

    assert len(output_paths) == 1
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
