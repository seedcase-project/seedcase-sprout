from pathlib import Path

import polars as pl

from seedcase_sprout.check_data import check_data
from seedcase_sprout.properties import ResourceProperties


def write_resource_data(
    data: pl.DataFrame,
    resource_properties: ResourceProperties,
    data_path: Path,
) -> Path:
    """Check and write the resource data into a file.

    This function takes the `data` obtained after using `join_staging()`,
    checks it against the `resource_properties`, and then writes it to the
    given `data_path`.

    Args:
        data: A DataFrame object with the resources data from the staging
            files.
        resource_properties: The `ResourceProperties` object that contains the
            properties of the resource you want to create the Parquet file for.
        data_path: The path where the data should be written.

    Returns:
        The path of the created Parquet file.
    """
    data_path.parent.mkdir(parents=True, exist_ok=True)
    check_data(data, resource_properties)
    data.write_parquet(data_path)
    return data_path
