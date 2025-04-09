import polars as pl
from pytest import mark, raises

from seedcase_sprout.core.examples import (
    example_data,
    example_data_all_types,
    example_resource_properties,
    example_resource_properties_all_types,
)
from seedcase_sprout.core.properties import FieldProperties
from seedcase_sprout.core.sprout_checks._check_column_types import _check_column_types


def test_accepts_correct_column_types():
    """Should not raise an error when the Polars data type of a column matches the
    Frictionless data type given in the resource properties."""
    resource_properties = example_resource_properties_all_types()
    resource_properties.schema.fields += [
        FieldProperties(name="my_categorical", type="string"),
        FieldProperties(name="my_enum", type="string"),
        FieldProperties(name="my_int8", type="integer"),
        FieldProperties(name="my_int8_year", type="year"),
        FieldProperties(name="my_uint64", type="integer"),
        FieldProperties(name="my_float32", type="number"),
        FieldProperties(name="my_decimal", type="number"),
        FieldProperties(name="my_int_geopoint", type="geopoint"),
    ]
    data = example_data_all_types().with_columns(
        [
            pl.Series(
                "my_categorical", ["low", "medium", "high"], dtype=pl.Categorical
            ),
            pl.Series(
                "my_enum",
                ["low", "low", "high"],
                dtype=pl.Enum(["low", "medium", "high"]),
            ),
            pl.Series("my_int8", [1, 22, 33], dtype=pl.Int8),
            pl.Series("my_int8_year", [1, 22, 33], dtype=pl.Int8),
            pl.Series("my_uint64", [1, 22, 33], dtype=pl.UInt64),
            pl.Series("my_float32", [1.1, 2.2, 3.3], dtype=pl.Float32),
            pl.Series("my_decimal", ["1.20", "2.56", "3.39"], dtype=pl.Decimal),
            pl.Series(
                "my_int_geopoint",
                [[3, 4], [5, 45], [12, -4]],
                dtype=pl.Array(pl.Int16, 2),
            ),
        ]
    )

    assert _check_column_types(data, resource_properties) is data


def test_accepts_columns_in_any_order():
    """Should not raise an error when the data types match but the columns are in a
    different order."""
    resource_properties = example_resource_properties()
    resource_properties.schema.fields.reverse()
    data = example_data()

    assert _check_column_types(data, resource_properties) is data


@mark.parametrize(
    "frictionless_type",
    [
        "string",
        "boolean",
        "integer",
        "number",
        "year",
        "datetime",
        "date",
        "time",
        "yearmonth",
        "geopoint",
        "duration",
        "object",
        "array",
        "geojson",
    ],
)
def test_rejects_incorrect_column_type(frictionless_type):
    """Should raise an error if the Polars type does not match the Frictionless type."""
    data = pl.DataFrame({"my_col": pl.Series([{"prop": "value"}] * 3, dtype=pl.Object)})
    resource_properties = example_resource_properties()
    resource_properties.schema.fields = [
        FieldProperties(name="my_col", type=frictionless_type)
    ]

    with raises(ExceptionGroup) as error_info:
        _check_column_types(data, resource_properties)

    errors = error_info.value.exceptions
    assert len(errors) == 1


def test_rejects_geopoint_with_incorrect_size():
    """Should raise an error if the size of the array representing a geopoint is not
    correct."""
    data = pl.DataFrame(
        {"my_geopoint": pl.Series([[1, 1, 1]] * 3, dtype=pl.Array(pl.Int8, 3))}
    )
    resource_properties = example_resource_properties()
    resource_properties.schema.fields = [
        FieldProperties(name="my_geopoint", type="geopoint")
    ]

    with raises(ExceptionGroup) as error_info:
        _check_column_types(data, resource_properties)

    errors = error_info.value.exceptions
    assert len(errors) == 1


def test_rejects_geopoint_with_incorrect_inner_type():
    """Should raise an error if the type of the nested elements in a geopoint array is
    not correct."""
    data = pl.DataFrame(
        {"my_geopoint": pl.Series([["a", "b"]] * 3, dtype=pl.Array(pl.String, 2))}
    )
    resource_properties = example_resource_properties()
    resource_properties.schema.fields = [
        FieldProperties(name="my_geopoint", type="geopoint")
    ]

    with raises(ExceptionGroup) as error_info:
        _check_column_types(data, resource_properties)

    errors = error_info.value.exceptions
    assert len(errors) == 1
