import re
from pathlib import Path

import polars as pl
from pytest import fixture, raises

from seedcase_sprout.core.properties import (
    FieldProperties,
    ResourceProperties,
    TableSchemaProperties,
)
from seedcase_sprout.core.sprout_checks.check_data import check_data

string_field = FieldProperties(name="my_string", type="string")
bool_field = FieldProperties(name="my_bool", type="boolean")
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


def test_no_error_when_data_column_names_match_properties(resource_properties):
    """Should throw no error if the column names in the data frame match the column
    names in the properties."""
    df = pl.DataFrame(
        {
            string_field.name: ["abc", "def"],
            bool_field.name: [True, False],
            number_field.name: [23, 45],
        }
    )
    resource_properties.schema.fields = [string_field, bool_field, number_field]

    assert check_data(df, resource_properties) is df


def test_throws_error_when_data_has_extra_columns(resource_properties):
    """Should throw an error if the data has extra columns."""
    df = pl.DataFrame({"extra_col1": [""], bool_field.name: [True], "extra_col2": [""]})
    resource_properties.schema.fields = [bool_field]

    with raises(ValueError, match=r"Extra columns.*extra_col1.*extra_col2") as error:
        check_data(df, resource_properties)

    assert bool_field.name not in str(error)


def test_throws_error_when_data_has_missing_columns(resource_properties):
    """Should throw an error if the data has missing columns."""
    df = pl.DataFrame({bool_field.name: [True]})
    resource_properties.schema.fields = [string_field, bool_field, number_field]

    with raises(
        ValueError, match=rf"Missing columns.*{string_field.name}.*{number_field.name}"
    ) as error:
        check_data(df, resource_properties)

    assert bool_field.name not in str(error)


def test_throws_error_when_data_has_extra_and_missing_columns(resource_properties):
    """Should throw an error if the data has extra columns and missing columns."""
    df = pl.DataFrame({"extra_col": [""], bool_field.name: [True]})
    resource_properties.schema.fields = [string_field, bool_field, number_field]

    with raises(ValueError) as error:
        check_data(df, resource_properties)

    assert re.search(r"Extra columns.*extra_col", str(error))
    assert re.search(
        rf"Missing columns.*{string_field.name}.*{number_field.name}", str(error)
    )
    assert bool_field.name not in str(error)


def test_no_error_when_data_has_correct_columns_in_different_order(resource_properties):
    """Should not throw an error if the data has the correct columns in a different
    order."""
    df = pl.DataFrame({string_field.name: [""], bool_field.name: [True]})
    resource_properties.schema.fields = [bool_field, string_field]

    assert check_data(df, resource_properties) is df
