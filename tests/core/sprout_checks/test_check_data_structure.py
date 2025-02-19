from pathlib import Path

import polars as pl
from pytest import fixture, mark, raises

from seedcase_sprout.core.checks.check_error import CheckError
from seedcase_sprout.core.properties import (
    FieldProperties,
    ResourceProperties,
    TableSchemaProperties,
)
from seedcase_sprout.core.sprout_checks.check_data import check_data


@fixture
def data_path(tmp_path) -> Path:
    return tmp_path / "data.csv"


string_field = FieldProperties(name="my_string", type="string")
date_field = FieldProperties(name="my_date", type="date")
number_field = FieldProperties(name="my_number", type="number")


@fixture
def resource_properties() -> ResourceProperties:
    return ResourceProperties(
        name="data",
        title="data",
        path=str(Path("resources", "1", "data.csv")),
        description="My data...",
        schema=TableSchemaProperties(),
    )


@mark.parametrize("fields", [None, [], ["not", "fields"]])
def test_throws_error_if_resource_properties_invalid(
    data_path, resource_properties, fields
):
    """Should throw an error if the resource properties are not correct."""
    resource_properties.schema.fields = fields

    with raises(ExceptionGroup) as error_info:
        check_data(data_path, resource_properties)
    assert all([isinstance(error, CheckError) for error in error_info.value.exceptions])


def test_throws_error_if_file_not_found(data_path, resource_properties):
    """Should throw an error if the file cannot be found."""
    resource_properties.schema.fields = [string_field]

    with raises(FileNotFoundError):
        check_data(data_path, resource_properties)


def test_throws_error_if_file_empty(data_path, resource_properties):
    """Should throw an error if the file is empty."""
    resource_properties.schema.fields = [string_field]
    data_path.touch()

    with raises(pl.exceptions.NoDataError):
        check_data(data_path, resource_properties)


def test_throws_error_if_file_cannot_be_read_as_csv(data_path, resource_properties):
    """Should throw an error if the file cannot be read as a CSV file."""
    data_path.write_text(f'{string_field.name}\n"This quote is not escaped')
    resource_properties.schema.fields = [string_field]

    with raises(pl.exceptions.ComputeError):
        check_data(data_path, resource_properties)


@mark.parametrize(
    "data", ["value\nvalue,12\nvalue", "value,12\nvalue\nvalue", "value\nvalue\nvalue"]
)
def test_no_error_if_data_row_has_fewer_columns_than_header(
    data_path, resource_properties, data
):
    """If a data row has fewer columns then the header, missing columns should be
    null-padded and no error should be thrown (provided this is a valid value for the
    column)."""
    data_path.write_text(f"{string_field.name},{number_field.name}\n{data}")
    resource_properties.schema.fields = [string_field, number_field]

    assert check_data(data_path, resource_properties) == data_path


def test_throws_error_if_data_row_has_more_columns_than_header(
    data_path, resource_properties
):
    """Should throw an error if a data row has more columns then the header."""
    data_path.write_text(f"{string_field.name}\nvalue,value\nvalue,value")
    resource_properties.schema.fields = [string_field]

    with raises(pl.exceptions.ShapeError):
        check_data(data_path, resource_properties)


@mark.parametrize(
    "data,fields",
    [
        ("123\n456", [number_field]),
        ("wrong_name\nvalue", [string_field]),
        (
            f"{string_field.name},{date_field.name}\nval,1023-02-12",
            [date_field, string_field],
        ),
        (f"{date_field.name},extra_name\n2023-12-12,val", [date_field]),
        (f"{date_field.name}\n2012-12-12", [date_field, string_field]),
    ],
)
def test_throws_error_if_data_and_schema_column_names_dont_match(
    data_path, resource_properties, data, fields
):
    """Should throw an error if the data has a header that doesn't match the column
    names in the properties exactly."""
    data_path.write_text(data)
    resource_properties.schema.fields = fields

    with raises(pl.exceptions.ShapeError):
        check_data(data_path, resource_properties)


def test_throws_error_if_no_schema(data_path, resource_properties):
    """Should throw an error if there is no schema information, as it makes it
    impossible to check the data header."""
    data_path.write_text("col1")
    resource_properties.schema = None

    with raises(pl.exceptions.ShapeError):
        check_data(data_path, resource_properties)


def test_accepts_data_with_header(data_path, resource_properties):
    """The check should pass if the data has a header that matches column names in the
    properties and the data is otherwise well-formed."""
    data_path.write_text(
        f"{string_field.name},{date_field.name},{number_field.name}\ne6c0eee7,1953-03-10,182.60"
    )
    resource_properties.schema.fields = [string_field, date_field, number_field]

    assert check_data(data_path, resource_properties) == data_path
