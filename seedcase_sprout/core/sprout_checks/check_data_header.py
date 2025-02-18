from pathlib import Path

import polars as pl


def check_data_header(data_path: Path, expected_columns: list[str]) -> Path:
    """Checks that the header in the given CSV file matches `expected_columns` exactly.

    Args:
        data_path: The path to the CSV file with a header.
        expected_columns: The expected column names.

    Returns:
        The data path if the check passed.

    Raises:
        polars.exceptions.ShapeError: If the header doesn't match the expected column
            names.
    """
    header = pl.read_csv(data_path, n_rows=1).columns
    if header != expected_columns:
        raise pl.exceptions.ShapeError(
            f"Column names do not match. Found: {header}, Expected: {expected_columns}"
        )
    return data_path
