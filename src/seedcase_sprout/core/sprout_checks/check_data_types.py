import polars as pl

from seedcase_sprout.core.get_nested_attr import get_nested_attr
from seedcase_sprout.core.properties import (
    FieldProperties,
    ResourceProperties,
)
from seedcase_sprout.core.sprout_checks.check_column_data_types import (
    FRICTIONLESS_TO_COLUMN_CHECK,
)
from seedcase_sprout.core.sprout_checks.get_field_error_message import (
    get_field_error_message,
)

# Column name for column containing the row index
INDEX_COLUMN = "__row_index__"
# Column name for column containing the result of the check
CHECK_COLUMN_NAME = "{column}_correct"


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


def extract_failed_values(check_result: pl.Expr, field_name: str) -> pl.Expr:
    """Adds a short error message for each value that failed the data type check.

    The error message includes the index of the row and the incorrect value itself.

    Args:
        check_result: The column containing the result of the check.
        field_name: The name of the field to check.

    Returns:
        A Polars expression.
    """
    return (
        pl.when(check_result)
        .then(pl.lit(None))
        .otherwise(
            pl.format(
                "[{}]: '{}'",
                pl.col(INDEX_COLUMN),
                pl.col(field_name),
            )
        )
    )


def check_column(data_frame: pl.DataFrame, field: FieldProperties) -> pl.Expr:
    """Checks that the values in the given column/field are of the correct type.

    This function constructs the appropriate check expression for the field
    based on the field's type.

    Args:
        data_frame: The data frame being operated on.
        field: The field to check.

    Returns:
        A Polars expression for checking the data type of values in the column.
    """
    field_name, field_type = field.name, field.type
    check = FRICTIONLESS_TO_COLUMN_CHECK[field_type]
    return (
        pl.col(field_name)
        .is_null()
        .or_(
            check(data_frame, field_name)
            if field_type == "datetime"
            else check(field_name)
        )
        .cast(pl.Boolean)
    )
