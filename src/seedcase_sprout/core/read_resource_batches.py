import re
from datetime import datetime
from pathlib import Path

import polars as pl

from seedcase_sprout.core.constants import (
    BATCH_TIMESTAMP_COLUMN_NAME,
    BATCH_TIMESTAMP_FORMAT,
    BATCH_TIMESTAMP_PATTERN,
)
from seedcase_sprout.core.internals import _check_is_file
from seedcase_sprout.core.properties import ResourceProperties
from seedcase_sprout.core.sprout_checks.check_data import check_data
from seedcase_sprout.core.sprout_checks.check_properties import (
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

    Raises:
        FileNotFoundError: If a file in the list of paths doesn't exist.
        ValueError: If the batch file name is not in the expected pattern.
        ValueError: If the timestamp column name matches an existing column in the
            DataFrame.

    Examples:
        ``` {python}
        import tempfile
        from pathlib import Path

        import polars as pl

        import seedcase_sprout.core as sp

        # Create a temporary directory for the example
        with tempfile.TemporaryDirectory() as temp_dir:
            tmp_dir = Path(temp_dir)

            # Create folders for the example
            resource_batch_dir = tmp_dir / "resources/1/batch"
            resource_batch_dir.mkdir(parents=True)

            # TODO: Use `write_resource_batch()` to create the batch file
            # Create a temporary batch file
            batch_file_path = resource_batch_dir / "2025-03-26T100346Z-12345678.parquet"
            data = pl.DataFrame(
                {
                    "id": [1, 2, 3],
                    "name": ["anne", "belinda", "charlotte"],
                    "value": [10, 20, 30],
                }
            )
            data.write_parquet(batch_file_path)

            sp.read_resource_batches(
                paths=sp.PackagePath(tmp_dir).resource_batch_files(1),
                resource_properties=sp.example_resource_properties(),
            )
        ```
    """
    list(map(_check_is_file, paths))
    check_resource_properties(resource_properties)
    return [_read_parquet_batch_file(path, resource_properties) for path in paths]


def _read_parquet_batch_file(
    path: Path, resource_properties: ResourceProperties
) -> pl.DataFrame:
    """Reads a Parquet batch file and adds the timestamp as a column.

    This function reads a Parquet batch file into a Polars DataFrame and adds
    a timestamp column to the DataFrame, extracted from the file name.

    Args:
        path: Path to the Parquet batch file.
        resource_properties: The resource properties to check the data against.

    Returns:
        The Parquet file as a DataFrame with a timestamp column added.
    """
    data = pl.read_parquet(path)
    check_data(data, resource_properties)

    timestamp = _extract_timestamp_from_batch_file_path(path)
    _check_batch_file_timestamp(timestamp)
    data = _add_timestamp_as_column(data, timestamp)
    return data


def _extract_timestamp_from_batch_file_path(path: Path) -> str:
    """Extracts the timestamp from the file name.

    Since the batch file name has been created by `create_batch_file_name()`,
    it should contain a timestamp in the format defined by BATCH_TIMESTAMP_PATTERN.

    If multiple timestamps are found in the file name, the first one is used.
    """
    timestamp_list = re.findall(BATCH_TIMESTAMP_PATTERN, path.stem)

    if not timestamp_list:
        raise ValueError(
            f"Batch file name '{path.stem}' does not contain a timestamp in the "
            f"expected format '{BATCH_TIMESTAMP_PATTERN}'."
        )

    return timestamp_list[0]


def _check_batch_file_timestamp(timestamp: str) -> str:
    """Checks the timestamp format and that it is a correct calendar date."""
    try:
        datetime.strptime(timestamp, BATCH_TIMESTAMP_FORMAT)
        return timestamp
    except ValueError as error:
        raise ValueError(
            f"Timestamp '{timestamp}' in the batch file name is not in the "
            f"expected format '{BATCH_TIMESTAMP_FORMAT}' or is not a correct calendar "
            "date (e.g., 30 February)."
        ) from error


def _add_timestamp_as_column(data: pl.DataFrame, timestamp: str) -> pl.DataFrame:
    """Adds the timestamp as a column to the data.

    Args:
        data: Data to add timestamp column to.
        timestamp: Timestamp to add as values in the timestamp column.

    Returns:
        Data with added timestamp column.

    Raises:
        ValueError: If a column with the name BATCH_TIMESTAMP_COLUMN_NAME already exists
        in the data.
    """
    # TODO: We could move this to be a check of the resource properties in
    # `sprout_checks/`
    if BATCH_TIMESTAMP_COLUMN_NAME in data.columns:
        raise ValueError(
            "One or multiple of the provided resource batch files contain a "
            f"column named '{BATCH_TIMESTAMP_COLUMN_NAME}'. This column is used "
            "internally in Sprout to remove duplicate rows across batches. Please "
            "rename it in the batch files and resource properties to read the resource "
            "batches."
        )
    return data.with_columns(pl.lit(timestamp).alias(BATCH_TIMESTAMP_COLUMN_NAME))
