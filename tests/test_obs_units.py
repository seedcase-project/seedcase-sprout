from pathlib import Path

import polars as pl
from polars.testing import assert_frame_equal
from pytest import fixture, mark, raises

from seedcase_sprout.examples import example_package_properties
from seedcase_sprout.obs_units import (
    exclude_deleted_obs_units,
    read_obs_unit_file,
)
from seedcase_sprout.properties import (
    FieldProperties,
    LicenseProperties,
    ResourceProperties,
    SproutProperties,
    TableSchemaProperties,
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
                    FieldProperties(name="pulse"),
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
                    FieldProperties(name="pain"),
                ]
            ),
        ),
    ],
)


@fixture
def _units_csv(tmp_path) -> Path:
    (tmp_path / "units.csv").write_text("participant_id,visit_id\nabc,123")
    return tmp_path / "units.csv"


def test_reading_none_path_returns_none():
    assert (
        read_obs_unit_file(path=None, package_properties=example_package_properties())
        is None
    )


def test_reads_file_with_only_header(tmp_path):
    (tmp_path / "units.csv").write_text("participant_id,visit_id")
    units_df = read_obs_unit_file(tmp_path / "units.csv", package_properties)

    assert units_df is not None
    assert_frame_equal(
        units_df,
        pl.DataFrame({"participant_id": [], "visit_id": []}).with_columns(
            pl.col("participant_id").cast(pl.String), pl.col("visit_id").cast(pl.Int64)
        ),
    )


def test_reads_correct_ids(_units_csv):
    units_df = read_obs_unit_file(_units_csv, package_properties)

    assert units_df is not None
    assert_frame_equal(
        units_df, pl.DataFrame({"participant_id": ["abc"], "visit_id": [123]})
    )


def test_errors_when_null_in_file(tmp_path):
    (tmp_path / "units.csv").write_text("participant_id,visit_id\nabc,")
    with raises(ValueError):
        read_obs_unit_file(tmp_path / "units.csv", package_properties)


@mark.parametrize(
    "properties",
    [
        SproutProperties(),
        SproutProperties(resources=[ResourceProperties()]),
        SproutProperties(
            resources=[ResourceProperties(schema=TableSchemaProperties())]
        ),
        SproutProperties(
            resources=[
                ResourceProperties(
                    schema=TableSchemaProperties(fields=[FieldProperties()])
                )
            ]
        ),
        SproutProperties(
            resources=[
                ResourceProperties(
                    schema=TableSchemaProperties(
                        fields=[FieldProperties(name="another_field")]
                    )
                )
            ]
        ),
        SproutProperties(
            resources=[
                ResourceProperties(
                    schema=TableSchemaProperties(
                        fields=[FieldProperties(name="another_field")]
                    )
                ),
                ResourceProperties(
                    schema=TableSchemaProperties(
                        fields=[FieldProperties(name="participant_id")]
                    )
                ),
            ]
        ),
        SproutProperties(
            resources=[
                ResourceProperties(
                    schema=TableSchemaProperties(
                        fields=[FieldProperties(name="another_field")]
                    )
                ),
                ResourceProperties(
                    schema=TableSchemaProperties(
                        fields=[
                            FieldProperties(name="participant_id"),
                            FieldProperties(name="visit_id"),
                        ]
                    )
                ),
            ]
        ),
    ],
)
def test_errors_when_id_cols_not_fields_in_all_resources(_units_csv, properties):
    with raises(ValueError):
        read_obs_unit_file(_units_csv, properties)


def test_errors_when_types_do_not_match(tmp_path):
    (tmp_path / "units.csv").write_text("participant_id,visit_id\n123,abc")
    with raises(ExceptionGroup):
        read_obs_unit_file(tmp_path / "units.csv", package_properties)


def test_errors_when_file_does_not_exist(tmp_path):
    with raises(FileNotFoundError):
        read_obs_unit_file(tmp_path / "units.csv", package_properties)


def test_errors_when_file_empty(tmp_path):
    (tmp_path / "units.csv").touch()
    with raises(pl.exceptions.NoDataError):
        read_obs_unit_file(tmp_path / "units.csv", package_properties)


def test_errors_when_file_not_csv(tmp_path):
    (tmp_path / "units.json").write_text(
        '[{"participant_id": "abc", "visit_id": "123"}]'
    )
    with raises(ValueError):
        read_obs_unit_file(tmp_path / "units.json", package_properties)


def test_excludes_rows_with_one_col_in_id():
    data = pl.DataFrame(
        {
            "participant_id": ["a", "b", "c", "d"],
            "another_col": [1, 2, 3, 4],
        }
    )
    units_df = pl.DataFrame(
        {
            "participant_id": ["b", "c"],
        }
    )

    result_df = exclude_deleted_obs_units(data=data, obs_unit_ids=units_df)

    assert_frame_equal(
        result_df,
        pl.DataFrame(
            {
                "participant_id": ["a", "d"],
                "another_col": [1, 4],
            }
        ),
    )


def test_excludes_rows_with_two_cols_in_id():
    data = pl.DataFrame(
        {
            "participant_id": ["a", "a", "b", "c"],
            "visit_id": [1, 2, 1, 3],
            "another_col": [1, 2, 3, 4],
        }
    )
    units_df = pl.DataFrame(
        {
            "participant_id": ["a", "c"],
            "visit_id": [1, 3],
        }
    )

    result_df = exclude_deleted_obs_units(data=data, obs_unit_ids=units_df)

    assert_frame_equal(
        result_df,
        pl.DataFrame(
            {
                "participant_id": ["a", "b"],
                "visit_id": [2, 1],
                "another_col": [2, 3],
            }
        ),
    )


@mark.parametrize("participant_ids", [[], ["e", "f"]])
def test_does_not_exclude_rows_when_none_match(participant_ids):
    data = pl.DataFrame(
        {
            "participant_id": ["a", "b", "c", "d"],
            "another_col": [1, 2, 3, 4],
        }
    )
    units_df = pl.DataFrame(
        {
            "participant_id": participant_ids,
        }
    ).with_columns(pl.all().cast(pl.String))

    result_df = exclude_deleted_obs_units(data=data, obs_unit_ids=units_df)

    assert_frame_equal(result_df, data)
