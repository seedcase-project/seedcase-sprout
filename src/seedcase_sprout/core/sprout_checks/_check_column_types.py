from typing import Callable, TypedDict

import polars as pl

from seedcase_sprout.core.get_nested_attr import get_nested_attr
from seedcase_sprout.core.properties import (
    FieldProperties,
    FieldType,
    ResourceProperties,
)


def _check_column_types(
    data: pl.DataFrame, resource_properties: ResourceProperties
) -> pl.DataFrame:
    """Checks that column data types match the data types specified in the properties.

    The resource properties specify a Frictionless data type for each column.
    This function checks if the Polars data type of each column in the data is an
    allowed realisation of the corresponding Frictionless data type.

    Column names are expected to match the names specified in the resource properties.

    Args:
        data: The data frame to check.
        resource_properties: The resource properties to check against.

    Returns:
        The data frame, if all column types are correct.

    Raises:
        ExceptionGroup: A group of `ValueError`s, one per incorrectly typed column.
    """
    all_column_props: list[FieldProperties] = get_nested_attr(
        resource_properties, "schema.fields", default=[]
    )
    errors = []
    for polars_type, column_props in zip(data.schema.dtypes(), all_column_props):
        type_check = _FRICTIONLESS_TO_POLARS_TYPE_CHECK[column_props.type or "any"]
        check, allowed_types = type_check["check"], type_check["allowed_types"]
        if not check(polars_type):
            errors.append(
                ValueError(
                    f"Expected type for column '{column_props.name}' "
                    f"to be {allowed_types} but found '{polars_type}'."
                )
            )
    if errors:
        raise ExceptionGroup(
            (
                "The following columns in the data have data types that do not match "
                "the data types in the resource properties:"
            ),
            errors,
        )
    return data


class _PolarsTypeCheck(TypedDict):
    check: Callable[[pl.DataType], bool]
    allowed_types: str


_STRING_TYPE_CHECK: _PolarsTypeCheck = {
    "check": lambda dtype: dtype == pl.String,
    "allowed_types": f"'{pl.String}'",
}

# Mapping from Frictionless field types to checks on Polars data types
_FRICTIONLESS_TO_POLARS_TYPE_CHECK: dict[FieldType, _PolarsTypeCheck] = {
    "string": {
        "check": lambda dtype: isinstance(dtype, (pl.String, pl.Categorical, pl.Enum)),
        "allowed_types": f"one of '{pl.String, pl.Categorical, pl.Enum}'",
    },
    "boolean": {
        "check": lambda dtype: dtype == pl.Boolean,
        "allowed_types": f"'{pl.Boolean}'",
    },
    "integer": {
        "check": lambda dtype: dtype.is_integer(),
        "allowed_types": "an integer type",
    },
    "number": {
        "check": lambda dtype: dtype.is_float() or dtype.is_decimal(),
        "allowed_types": "a float or decimal type",
    },
    "year": {
        "check": lambda dtype: dtype.is_integer(),
        "allowed_types": "an integer type",
    },
    "datetime": {
        "check": lambda dtype: dtype == pl.Datetime,
        "allowed_types": f"'{pl.Datetime}'",
    },
    "date": {
        "check": lambda dtype: dtype == pl.Date,
        "allowed_types": f"'{pl.Date}'",
    },
    "time": {
        "check": lambda dtype: dtype == pl.Time,
        "allowed_types": f"'{pl.Time}'",
    },
    "yearmonth": {
        "check": lambda dtype: dtype == pl.Date,
        "allowed_types": f"'{pl.Date}'",
    },
    "geopoint": {
        "check": lambda dtype: (
            isinstance(dtype, pl.Array) and dtype.size == 2 and dtype.inner.is_numeric()
        ),
        "allowed_types": "an array of a numeric type with size 2",
    },
    "duration": _STRING_TYPE_CHECK,
    "object": _STRING_TYPE_CHECK,
    "array": _STRING_TYPE_CHECK,
    "geojson": _STRING_TYPE_CHECK,
    "any": {
        "check": lambda _: True,
        "allowed_types": "any type",
    },
}
