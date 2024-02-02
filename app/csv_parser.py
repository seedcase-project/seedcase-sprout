import csv
from csv import Dialect
from typing import IO, Callable

import pandas
from pandas import DataFrame, Series


def read_csv_file(csv_file: IO, row_number: int = 1000) -> DataFrame:
    """
    Reads a CSV file and returns a DataFrame with the data types of the columns.

    It uses `pandas.csv_read()`, but adds some additional functionality:

    - Finds `datetime64`, date (converted from the `datetime64`), and `timedelta64` columns
    - Understands boolean-ish values like: Yes, y, 1
    - Finds the CSV dialect of the file (for example, the delimiter is semicolon or comma)
    - Removes whitespaces in column names

    Args:
        csv_file: The CSV file to read.
        row_number: The number of rows to scan from the file. You don't need many to determine the data type of the column.

    Returns:
        DataFrame: A Pandas DataFrame with the derived data types (`dtypes`).
    """
    dialect = _derive_csv_dialect(csv_file, row_number)

    df = pandas.read_csv(csv_file, nrows=row_number, dialect=dialect)
    return derive_column_types_and_convert(df)


def _derive_csv_dialect(csv_file: IO, row_number: int = 1000) -> Dialect:
    """
    Extract the "dialect" of the CSV file.

    Dialect meaning whether the separator is a comma or a semicolon.

    Args:
        csv_file (IO): The CSV file.
        row_number (int, optional): Number of rows to scan. Defaults to 1000.

    Returns:
        Dialect: A Dialect object containing information on the separator for the columns in the CSV file.
    """
    dialect = csv.Sniffer().sniff(csv_file.read(row_number))
    csv_file.seek(0)
    return dialect


def derive_column_types_and_convert(df: DataFrame) -> DataFrame:
    """
    Evaluate DataFrame columns to determine they should be converted to a specific type.

    Args:
        df (DataFrame): The DataFrame with the CSV data.

    Returns:
        DataFrame: A DataFrame where the column types are obtained and converted.
    """
    df.columns.str.strip()
    for column in df.columns:
        _convert_column_if_possible(df, column)

    return df


def _convert_column_if_possible(df: DataFrame, column_name: str) -> None:
    """
    Convert columns to specific types not provided by `pandas.read_csv()`.

    The default `pandas.read_csv()` does not derive date/datetime, timedelta,
    and boolean-ish values. This function tries to convert relevant columns to
    those certain types.

    Args:
        df: The DataFrame
        column_name: The name of the column to process and convert.

    Returns:
        None: Used for the side effect of processing the columns.
    """
    if _try_convert(df, column_name, parse_boolean_ish):
        return
    if _try_convert(df, column_name, parse_timedelta):
        return
    if _try_convert(df, column_name, parse_datetimes):
        return


def _try_convert(
    df: DataFrame, column: str, parser: Callable[[Series], Series]
) -> bool:
    """
    Try to convert a column in a DataFrame using a function.

    We try to convert a column to a certain format with a parser function. The
    `parser` will raise a `ValueError` if not possible convert.

    Args:
        df: The entire DataFrame.
        column: The column to parse.
        parser: Function to convert a Pandas `Series` to another Pandas `Series`.

    Returns:
        bool: `True` if we are able to parse the column with the supplied parser,
        `False` if the parser fails by raising `ValueError`.
    """
    try:
        df[column] = parser(df[column])
        return True
    except ValueError:
        return False


def parse_timedelta(series: Series) -> Series:
    """
    Parse values into a time object.

    Args:
        series (Series): The vector to parse.

    Raises:
        ValueError: If the `series` object isn't an "object" Pandas data type.

    Returns:
        Series: A vector converted into a time data type.
    """
    if series.dtype.name != "object":
        raise ValueError("This series isn't an `object` data type, can't convert to a time vector.")
    return pandas.to_timedelta(series)


def parse_datetimes(series: Series) -> Series:
    if series.dtype.name != "object":
        raise ValueError
    return pandas.to_datetime(series)


def parse_boolean_ish(series: Series) -> Series:
    if series.dtype.name not in ("object", "int64"):
        raise ValueError
    return series.apply(parse_boolean)


def parse_boolean(value: str | int) -> bool:
    """
    Parse values and convert to a boolean value.

    This converts boolean-ish values like "yes", "no", "y" and 1 to actual boolean values.

    Args:
        value (str | int): A character or integer.

    Raises:
        ValueError: If the `value` is an integer that has values other than 0 or
        1, it can't convert to boolean.
        ValueError: If the `value` is a character but has values that can't be
        meaningfully converted into a Boolean (e.g. isn't something like "yes" or "no").

    Returns:
        bool: Returns True/False value.
    """
    if isinstance(value, int):
        if value == 0:
            return False
        if value == 1:
            return True
        raise ValueError(
            "The value contains integers that are not 0 or 1, so can't convert to Boolean."
        )

    if value.lower() in ["true", "yes", "1", "y"]:
        return True

    if value.lower() in ["false", "no", "0", "n"]:
        return False

    raise ValueError(
        "The value contains data that can't be meaningfully converted to a Boolean."
    )
