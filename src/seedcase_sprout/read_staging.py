import re
from datetime import datetime
from pathlib import Path

import polars as pl
from seedcase_soil import fmap

from seedcase_sprout.constants import (
    STAGING_TIMESTAMP_COLUMN_NAME,
    STAGING_TIMESTAMP_FORMAT,
    STAGING_TIMESTAMP_PATTERN,
)
from seedcase_sprout.internals import _check_is_file


def read_staging(paths: list[Path]) -> list[pl.DataFrame]:
    """Read all staging file(s) into a list of (Polars) DataFrames.

    Use this function to read the Parquet file(s) specified in `paths` into a
    list of Polars DataFrames.

    Args:
        paths: A list of paths for all the Parquet files in `staging/` folder.

    Returns:
        A list of DataFrame objects from all the staging files.

    Raises:
        ValueError: If the staging file name is not in the expected pattern.
        ValueError: If the timestamp column name matches an existing column in
            the DataFrame.
    """
    fmap(paths, _check_is_file)
    return fmap(paths, _read_staging_parquet)


def _read_staging_parquet(path: Path) -> pl.DataFrame:
    if path.suffix != ".parquet":
        raise ValueError(
            "Failed to read the staging file. Expected a file with a "
            f"`.parquet` extension but found {path}."
        )
    data = pl.read_parquet(path)

    timestamp = _extract_timestamp_from_staging_path(path)
    _check_staging_file_timestamp(timestamp)
    data = _add_timestamp_as_column(data, timestamp)
    return data


def _extract_timestamp_from_staging_path(path: Path) -> str:
    timestamp_list: list[str] = re.findall(STAGING_TIMESTAMP_PATTERN, path.stem)

    if not timestamp_list:
        raise ValueError(
            f"Staging file name '{path.stem}' does not contain a timestamp in the "
            f"expected format '{STAGING_TIMESTAMP_PATTERN}'."
        )

    return timestamp_list[0]


def _check_staging_file_timestamp(timestamp: str) -> str:
    try:
        datetime.strptime(timestamp, STAGING_TIMESTAMP_FORMAT).astimezone()
        return timestamp
    except ValueError as error:
        raise ValueError(
            f"Timestamp '{timestamp}' in the staging file name is not in the "
            f"expected format '{STAGING_TIMESTAMP_FORMAT}' or is not a correct"
            "calendar date (e.g., 30 February)."
        ) from error


def _add_timestamp_as_column(data: pl.DataFrame, timestamp: str) -> pl.DataFrame:
    # TODO: We could move this to be a check of the resource properties in
    # `sprout_checks/`
    if STAGING_TIMESTAMP_COLUMN_NAME in data.columns:
        raise ValueError(
            "One or multiple of the provided resource staging files contain a "
            f"column named '{STAGING_TIMESTAMP_COLUMN_NAME}'. This column is used "
            "internally in Sprout to remove duplicate rows across staging. Please "
            "rename it in the staging files and resource properties to read the "
            "staging files."
        )
    return data.with_columns(pl.lit(timestamp).alias(STAGING_TIMESTAMP_COLUMN_NAME))
