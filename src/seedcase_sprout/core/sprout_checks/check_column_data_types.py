import json

import polars as pl

from seedcase_sprout.core.map_data_types import FRICTIONLESS_TO_POLARS
from seedcase_sprout.core.properties import FieldType

# https://datapackage.org/standard/table-schema/#boolean
BOOLEAN_VALUES = {"false", "False", "FALSE", "0", "true", "True", "TRUE", "1"}


def check_is_boolean(field_name: str) -> pl.Expr:
    """Checks if the column contains only boolean values.

    Failed values are marked with False.

    Args:
        field_name: The name of the column to check.

    Returns:
        A Polars expression for checking the column.
    """
    return pl.col(field_name).is_in(BOOLEAN_VALUES)


def check_is_castable_type(field_name: str, field_type: FieldType) -> pl.Expr:
    """Checks if the column contains only values of the given type.

    The check is done by attempting to cast to the appropriate Polars data type.
    Failed values are marked with False.

    Args:
        field_name: The name of the column to check.
        field_type: The type of the field.

    Returns:
        A Polars expression for checking the column.
    """
    return (
        pl.col(field_name)
        .cast(FRICTIONLESS_TO_POLARS[field_type], strict=False)
        .is_not_null()
    )


def check_is_yearmonth(field_name: str) -> pl.Expr:
    """Checks if the column contains only yearmonth values.

    Failed values are marked with False.

    Args:
        field_name: The name of the column to check.

    Returns:
        A Polars expression for checking the column.
    """
    return (
        pl.col(field_name).str.starts_with("-").not_()
        & (pl.col(field_name) + "-01")
        .fill_null("0001-01-01")
        .str.to_date(format="%Y-%m-%d", strict=False)
        .is_not_null()
    )


def check_is_datetime(data_frame: pl.DataFrame, field_name: str) -> pl.Expr:
    """Checks if the column contains only datetime values.

    Mixing values with and without timezone information is not allowed.
    Mixing values with different timezones is allowed, as they will be standardised
    before saving to Parquet.

    Failed values are marked with False.

    Args:
        data_frame: The data frame being operated on.
        field_name: The name of the column to check.

    Returns:
        A Polars expression for checking the column.
    """
    first_datetime = (
        data_frame.get_column(field_name)
        .drop_nulls()
        .str.to_datetime(strict=False)
        .first()
    )
    has_timezone = bool(first_datetime.tzinfo) if first_datetime else False
    default_datetime = "0001-01-01T00:00:00" + ("Z" if has_timezone else "")
    datetime_format = "%Y-%m-%dT%H:%M:%S%.f" + ("%z" if has_timezone else "")

    return (
        pl.col(field_name).str.starts_with("-").not_()
        & pl.col(field_name)
        .fill_null(default_datetime)
        .str.replace("Z", "+00:00")
        .str.to_datetime(time_unit="ms", format=datetime_format, strict=False)
        .dt.convert_time_zone(time_zone="UTC")
        .is_not_null()
    )


def check_is_date(field_name: str) -> pl.Expr:
    """Checks if the column contains only date values.

    Failed values are marked with False.

    Args:
        field_name: The name of the column to check.

    Returns:
        A Polars expression for checking the column.
    """
    return (
        pl.col(field_name).str.starts_with("-").not_()
        & pl.col(field_name)
        .fill_null("0001-01-01")
        .str.to_date(format="%Y-%m-%d", strict=False)
        .is_not_null()
    )


def check_is_time(field_name: str) -> pl.Expr:
    """Checks if the column contains only time values.

    Failed values are marked with False.

    Args:
        field_name: The name of the column to check.

    Returns:
        A Polars expression for checking the column.
    """
    return (
        pl.col(field_name)
        .fill_null("00:00:00")
        .str.to_time(format="%H:%M:%S%.f", strict=False)
        .is_not_null()
    )


# https://stackoverflow.com/a/18690202
GEOPOINT_PATTERN = (
    r"^(?:[-+]?(?:[1-8]?\d(?:\.\d+)?|90(?:\.0+)?)),\s*"
    r"(?:[-+]?(?:180(?:\.0+)?|(?:1[0-7]\d|[1-9]?\d)(?:\.\d+)?))$"
)


def check_is_geopoint(field_name: str) -> pl.Expr:
    """Checks if the column contains only geopoint values.

    Failed values are marked with False.

    Args:
        field_name: The name of the column to check.

    Returns:
        A Polars expression for checking the column.
    """
    return pl.col(field_name).str.contains(GEOPOINT_PATTERN)


def check_is_json(field_name: str, expected_type: type[list | dict]) -> pl.Expr:
    """Checks if the column contains only JSON values.

    Failed values are marked with False.

    Warning: uses `map_elements` to check the formatting of each value and may run
    slowly on large datasets.

    Args:
        field_name: The name of the column to check.
        expected_type: The expected JSON type: an object or an array.

    Returns:
        A Polars expression for checking the column.
    """
    return pl.col(field_name).map_elements(
        lambda value: check_value_is_json(value, expected_type),
        return_dtype=pl.Boolean,
    )


def check_value_is_json(value: str, expected_type: type[list | dict]) -> bool:
    """Checks if the `value` is correctly formatted as a JSON object or array.

    Args:
        value: The value to check.
        expected_type: The expected JSON type: an object or an array.

    Returns:
        True if the value is a correct JSON type, False otherwise.
    """
    try:
        return isinstance(json.loads(value), expected_type)
    except json.JSONDecodeError:
        return False


FRICTIONLESS_TO_COLUMN_CHECK = {
    "boolean": check_is_boolean,
    "integer": lambda col_name: check_is_castable_type(col_name, "integer"),
    "number": lambda col_name: check_is_castable_type(col_name, "number"),
    "year": lambda col_name: check_is_castable_type(col_name, "year"),
    "yearmonth": check_is_yearmonth,
    "datetime": check_is_datetime,
    "date": check_is_date,
    "time": check_is_time,
    "geopoint": check_is_geopoint,
    "array": lambda value: check_is_json(value, list),
    "object": lambda value: check_is_json(value, dict),
    "geojson": lambda value: check_is_json(value, dict),
    "string": lambda _: pl.lit(True),
    "any": lambda _: pl.lit(True),
    "duration": lambda _: pl.lit(True),
}
