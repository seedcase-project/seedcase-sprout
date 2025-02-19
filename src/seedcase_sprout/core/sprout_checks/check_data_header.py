import polars as pl


def check_data_header(
    lazy_frame: pl.LazyFrame, expected_columns: list[str]
) -> pl.LazyFrame:
    """Checks that the header in the lazy frame matches the expected column names.

    Args:
        lazy_frame: The lazy frame to check.
        expected_columns: The expected column names.

    Returns:
        The lazy frame, if the column names match.

    Raises:
        polars.exceptions.ShapeError: If the header doesn't match the expected
            column names.
    """
    data_columns = lazy_frame.collect_schema().names()
    if data_columns != expected_columns:
        raise pl.exceptions.ShapeError(
            "Column names in the data file do not match column names in the resource "
            f"properties. Expected {expected_columns}, but found: {data_columns}."
        )
    return lazy_frame
