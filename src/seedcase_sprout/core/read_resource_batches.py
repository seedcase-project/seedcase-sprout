from datetime import datetime
from pathlib import Path

import polars as pl

from seedcase_sprout.core.check_is_file import check_is_file
from seedcase_sprout.core.properties import ResourceProperties
from seedcase_sprout.core.sprout_checks.check_batch_file_name import (
    check_batch_file_name,
)

# from seedcase_sprout.core.checks.check_data import check_data
from seedcase_sprout.core.sprout_checks.check_resource_properties import (
    check_resource_properties,
)


def read_resource_batches(
    paths: list[Path], resource_properties: ResourceProperties
) -> list[pl.DataFrame]:
    """Reads all the batch resource file(s) into a list of (Polars) DataFrames.

    This function takes the Parquet file(s) given by `paths`, reads them in as Polars
    DataFrames as a list and does some checks on each of the DataFrames in the list
    based on the `resource_properties`. The `resource_properties` object is used
    to check the data and ensure it is correct. While Sprout generally assumes
    that the files stored in the `resources/<id>/batch/` folder are already
    correctly structured and tidy, this function still runs checks to ensure the
    data are correct by comparing to the properties.

    Args:
        paths: A list of paths for all the files in the resource's `batch/` folder.
            Use `path_resource_batch_files()` to help provide the correct paths to the
            batch files.
        resource_properties: The `ResourceProperties` object that contains the
            properties of the resource you want to check the data against.

    Returns:
        Outputs a list of DataFrame objects from all the batch files.

    Examples:
        ``` python
        import seedcase_sprout.core as sp

        sp.read_resource_batches(
            paths=sp.path_resources_batch_files(1),
            resource_properties=sp.example_resource_properties(),
        )
        ```
    """
    map(check_is_file, paths)
    check_resource_properties(resource_properties)

    data_list = list(map(_read_parquet_batch_file, paths))

    # TODO: Uncomment and test when `check_data` is implemented
    # list(map(check_data, data_list, resource_properties))

    return data_list


def _read_parquet_batch_file(path: Path) -> pl.DataFrame:
    """Reads a Parquet batch file and adds the timestamp as a column.

    This function reads a Parquet batch file into a Polars DataFrame and adds
    a timestamp column to the DataFrame, extracted from the file name.

    Args:
        path: Path to the Parquet batch file.

    Returns:
        The Parquet file as a DataFrame with a timestamp column added.
    """
    data = pl.read_parquet(path)
    check_batch_file_name(path)
    timestamp = _extract_timestamp_from_batch_file_path(path)
    data = _add_timestamp_as_column(data, timestamp)
    return data


def _extract_timestamp_from_batch_file_path(path: Path) -> str:
    """Extracts the timestamp from the file name.

    Since the batch file name has been created by `create_batch_file_name()`, with a
    specific format, the timestamp can be extracted by taking the first 18 characters of
    the file name.
    """
    return path.stem[0:18]


def _add_timestamp_as_column(data: pl.DataFrame, timestamp: str) -> pl.DataFrame:
    """Adds the timestamp as a column to the data.

    Args:
        data: Data to add timestamp column to.
        timestamp: Timestamp to add as values in the timestamp column.

    Returns:
        Data with added timestamp column.
    """
    return data.with_columns(pl.lit(timestamp).alias("_batch_file_timestamp_"))
