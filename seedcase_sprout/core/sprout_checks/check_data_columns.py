import polars as pl


def check_data_columns(lazy_frame: pl.LazyFrame) -> pl.LazyFrame:
    """Checks if a lazy frame has the same number of columns in each row.

    An error is thrown if the lazy frame has more or fewer columns than its header.
    Columns that are completely empty (i.e. have only null values) are counted as
    missing.

    Args:
        lazy_frame: The lazy frame to check.

    Returns:
        The lazy frame if the check passed.

    Raises:
        polars.exceptions.ShapeError: If the lazy frame has more or fewer columns than
            its header.
        polars.exceptions.ComputeError: If the data file cannot be read.
    """
    try:
        is_column_empty = (
            lazy_frame.select(pl.all().is_null().all()).collect().to_dict()
        )
    except pl.exceptions.ComputeError as error:
        if "found more fields than defined" in str(error):
            raise pl.exceptions.ShapeError(
                "The data file contains more columns than the resource properties."
            ) from error
        raise error

    empty_columns = [name for name, is_empty in is_column_empty.items() if is_empty[0]]
    if empty_columns:
        raise pl.exceptions.ShapeError(
            "The data file contains fewer columns than the resource properties. "
            f"The following columns are missing: {empty_columns}"
        )
    return lazy_frame
