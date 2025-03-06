import polars as pl

from seedcase_sprout.core.get_nested_attr import get_nested_attr
from seedcase_sprout.core.properties import (
    FieldProperties,
    ResourceProperties,
)
from seedcase_sprout.core.sprout_checks.check_column_data_types import (
    check_is_boolean,
    check_is_castable_type,
    check_is_date,
    check_is_datetime,
    check_is_geopoint,
    check_is_json,
    check_is_time,
    check_is_yearmonth,
)
from seedcase_sprout.core.sprout_checks.get_field_error_message import (
    get_field_error_message,
)

# Column name for column containing the row index
INDEX_COLUMN = "__row_index__"
# Column name for column containing the result of the check
CHECK_COLUMN_NAME = "{column}_error"


def check_data_types(data_frame: pl.DataFrame, resource_properties: ResourceProperties):
    """Checks that all data items match their data type given in `resource_properties`.

    Each value in each data frame column is checked against the data type given in the
    resource properties for the corresponding field. This function expects the column
    names of the data frame to be correct and assumes that missing values are
    represented by null.

    Args:
        data_frame: The data frame to check.
        resource_properties: The resource properties to check against.

    Returns:
        The data frame, if all data type checks passed.

    Raises:
        ExceptionGroup[ValueError]: One error for each column/field where any values
            failed the data type check. Each error lists all failed values together
            with their row index.
    """
    fields: list[FieldProperties] = get_nested_attr(
        resource_properties, "schema.fields", default=[]
    )

    # Add column with failed values for each field
    df_checked = data_frame.with_row_index(INDEX_COLUMN).with_columns(
        check_column(data_frame, field)
        .pipe(extract_failed_values, field.name)
        .alias(CHECK_COLUMN_NAME.format(column=field.name))
        for field in fields
    )

    # Collect failed values into one error per field
    errors = []
    for field in fields:
        failed_values = (
            df_checked.get_column(CHECK_COLUMN_NAME.format(column=field.name))
            .drop_nulls()
            .to_list()
        )
        if failed_values:
            errors.append(ValueError(get_field_error_message(field, failed_values)))

    if errors:
        raise ExceptionGroup(
            "Some columns contain values that do not match the column's data type.",
            errors,
        )

    return data_frame


def extract_failed_values(this_column: pl.Expr, field_name: str) -> pl.Expr:
    """Adds a short error message for each value that failed the data type check.

    The error message includes the index of the row and the incorrect value itself.

    Args:
        this_column: The column being operated on.
        field_name: The name of the field to check.

    Returns:
        A Polars expression.
    """
    return (
        pl.when(this_column.is_null())
        .then(
            pl.format(
                "[{}]: '{}'",
                pl.col(INDEX_COLUMN),
                pl.col(field_name),
            )
        )
        .otherwise(pl.lit(None))
    )


def check_column(data_frame: pl.DataFrame, field: FieldProperties) -> pl.Expr:
    """Checks that the values in the given column/field are of the correct type.

    This function selects and returns the appropriate check expression for the field
    based on the field's type.

    Args:
        data_frame: The data frame being operated on.
        field: The field to check.

    Returns:
        A Polars expression for checking the data type of values in the column.
    """
    field_name, field_type = field.name, field.type
    match field_type:
        case "boolean":
            return check_is_boolean(field_name)

        case "integer" | "number" | "year":
            return check_is_castable_type(field_name, field.type)

        case "yearmonth":
            return check_is_yearmonth(field_name)

        case "datetime":
            return check_is_datetime(data_frame, field_name)

        case "date":
            return check_is_date(field_name)

        case "time":
            return check_is_time(field_name)

        case "geopoint":
            return check_is_geopoint(field_name)

        case "array":
            return check_is_json(field_name, list)

        case "object" | "geojson":
            return check_is_json(field_name, dict)

        # Catches: string, any, duration
        case _:
            return pl.col(field_name)
