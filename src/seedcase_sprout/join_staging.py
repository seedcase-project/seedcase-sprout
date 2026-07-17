import polars as pl

from seedcase_sprout.check_data import check_data
from seedcase_sprout.check_properties import (
    check_resource_properties,
)
from seedcase_sprout.constants import STAGING_TIMESTAMP_COLUMN_NAME
from seedcase_sprout.internals import _get_nested_attr
from seedcase_sprout.properties import ResourceProperties


def join_staging(
    data_list: list[pl.DataFrame], resource_properties: ResourceProperties
) -> pl.DataFrame:
    """Join DataFrames from `staging/` into a single (Polars) DataFrame.

    This function takes a list of DataFrames, joins them together and drops any
    duplicate observational units based on the primary key from `resource_properties`.
    Then, it confirms that the data are correct against the `resource_properties` after
    the join.

    The observational unit is the primary key of the resource. For example, if a person
    is part of a research study and has multiple observations, the person's ID and the
    date of collection would be the observational unit.

    If there are any duplicate observational units in the data, only the most recent
    observational unit will be kept based on the timestamp of the staging file. This way,
    if there are any errors or mistakes in older staging files that have been corrected in
    later files, the mistake will be kept in the staging file, but won't be included in
    the `data.parquet` file.

    Args:
        data_list: A list of Polars DataFrames for all the staging files. Use
            `read_staging()` to get a list of DataFrames that have been
            checked against the properties individually.
        resource_properties: The `ResourceProperties` object that contains the
            properties of the resource to check the data against.

    Returns:
        A single DataFrame object of all the staging data with duplicate
            observational units removed.

    Raises:
        ValueError: If an empty `data_list` is provided.
        polars.exceptions.ShapeError: If the dataframes in data_list have different
            shapes, such as mismatched column names or numbers.
        polars.exceptions.SchemaError: If the dataframes in data_list have
            different schemas, e.g., their column data types don't match.
    """
    check_resource_properties(resource_properties)

    if data_list == []:
        raise ValueError(
            "Could not join DataFrames because the `data_list` is "
            f"empty. The staging folder for the resource '{resource_properties.name}' "
            "may be empty."
        )

    data = pl.concat(data_list)
    primary_key = _get_nested_attr(resource_properties, "schema.primary_key")
    data = _drop_duplicate_obs_units(data, primary_key)

    check_data(data, resource_properties)

    return data


def _drop_duplicate_obs_units(
    data: pl.DataFrame, primary_key: list[str] | str | None
) -> pl.DataFrame:
    """Drop duplicates based on the primary key and keep the latest one."""
    data = data.sort(STAGING_TIMESTAMP_COLUMN_NAME)
    data = data.drop(STAGING_TIMESTAMP_COLUMN_NAME)

    return data.unique(subset=primary_key, keep="last")
