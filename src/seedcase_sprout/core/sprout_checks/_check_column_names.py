import polars as pl

from seedcase_sprout.core.get_nested_attr import get_nested_attr
from seedcase_sprout.core.properties import ResourceProperties


def _check_column_names(
    data: pl.DataFrame, resource_properties: ResourceProperties
) -> str:
    """Checks that column names in `data` match those in `resource_properties`.

    Args:
        data: The data to check.
        resource_properties: The resource properties to check against.

    Returns:
        The data if the column names match.

    Raises:
        ValueError: If the column names are not the same as the names in
            `resource_properties`.
    """
    names_in_data = data.schema.names()
    names_in_resource = [
        field.name
        for field in get_nested_attr(resource_properties, "schema.fields", default=[])
    ]

    if names_in_data != names_in_resource:
        raise ValueError(
            _format_column_name_error_message(names_in_data, names_in_resource)
        )

    return data


def _format_column_name_error_message(
    names_in_data: list[str], names_in_resource: list[str]
) -> str:
    extra_columns_in_data = [
        name for name in names_in_data if name not in names_in_resource
    ]
    missing_columns_in_data = [
        name for name in names_in_resource if name not in names_in_data
    ]
    if not extra_columns_in_data and not missing_columns_in_data:
        return (
            "The column names in the data are in the wrong order. Expected"
            f" {names_in_resource} but found {names_in_data}."
        )

    message = (
        "Column names in the data do not match column names in the resource properties:"
    )
    if extra_columns_in_data:
        message += f"\n- Extra columns: {extra_columns_in_data}"
    if missing_columns_in_data:
        message += f"\n- Missing columns: {missing_columns_in_data}"
    return message
