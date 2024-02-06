import csv
from csv import Dialect
from typing import IO

import pandas
from pandas import DataFrame, Series

from app.csv_converters import convert_to_booleans, convert_to_datetimes, \
    convert_to_timedeltas


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

    Raises:
        csv.Error: An error is raised if we are unable to parse the CSV

    Returns:
        DataFrame: A Pandas DataFrame with the derived data types (`dtypes`).
    """
    dialect = _derive_csv_dialect(csv_file, row_number)

    df = pandas.read_csv(csv_file,
                         nrows=row_number,
                         dialect=dialect,
                         true_values=["yes", "Yes", "YES", "y"],
                         false_values=["no", "No", "NO", "n"])

    if len(df.columns) == 0:
        raise csv.Error("No columns were found")

    if len(df[df.columns[0]]) == 0:
        raise csv.Error("No rows where found")

    return derive_column_types_and_convert(df)


def _derive_csv_dialect(csv_file: IO, row_number: int = 1000) -> Dialect:
    """
    Extract the "dialect" of the CSV file.

    Dialect meaning whether the separator is a comma or a semicolon.

    Args:
        csv_file (IO): The CSV file.
        row_number (int, optional): Number of rows to scan. Defaults to 1000.

    Raises:
        csv.Error: if unable to parse CSV dialect

    Returns:
        Dialect: A Dialect object containing information on the separator for the columns in the CSV file.
    """
    content = csv_file.read(row_number)
    if isinstance(content, bytes):
        content = content.decode("utf-8")

    dialect = csv.Sniffer().sniff(content)
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
        df[column] = _convert_column_if_possible(df[column])

    return df


def _convert_column_if_possible(series: Series) -> Series:
    """
    Convert columns to specific types not provided by `pandas.read_csv()`.

    The default `pandas.read_csv()` does not derive date/datetime, timedelta,
    and boolean-ish values. This function tries to convert relevant columns to
    those certain types.

    Args:
        series: A pandas Series with column values and metadata

    Returns:
        Either an unchanged series or a converted series with dtype datetime,
        timedelta or bool
    """

    for parser in [convert_to_booleans, convert_to_timedeltas, convert_to_datetimes]:
        try:
            return parser(series)
        except ValueError:
            pass

    return series
