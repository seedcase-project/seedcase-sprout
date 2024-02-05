import csv
from csv import Dialect
from typing import IO

import pandas
from pandas import DataFrame, Series


def read_csv_file(csv_file: IO, row_number: int = 1000) -> DataFrame:
    """
    Reads a csv file and returns a DataFrame with the values.
    It uses pandas.csv_read(), but adds some functionality:
    - finds datetime64 and time_delta64 columns
    - understands boolean-ish values like: Yes, y, 1
    - finds the csv dialect of the file (fx. is delimiter semicolon or comma)
    - removes whitespaces in column names

    Args:
        csv_file: the csv file to parse
        row_number: the number of rows to read from the file

    Returns:
        a pandas dataframe with derived types (dtypes)
    """
    dialect = _derive_csv_dialect(csv_file, row_number)

    df = pandas.read_csv(csv_file, nrows=row_number, dialect=dialect)
    return derive_column_types_and_convert(df)


def _derive_csv_dialect(csv_file, row_number) -> Dialect:
    dialect = csv.Sniffer().sniff(csv_file.read(row_number))
    csv_file.seek(0)
    return dialect


def derive_column_types_and_convert(df: DataFrame) -> DataFrame:
    """
    DataFrame columns are iterated and for every column we evaluate if the column should
    be converted to a different type
    Args:
        df: the dataframe with the csv data

    Returns:
        A dataframe where column types are derived and converted
    """
    df.columns.str.strip()
    for col in df.columns:
        df[col] = _convert_column_if_possible(df[col])

    return df


def _convert_column_if_possible(series: Series) -> Series:
    """
    The default pandas.read_csv is not able to derive datetime, timedelta
    and boolean-ish values.

    Here we try to convert a column to one of these types

    Args:
        series: a pandas Series with column values and metadata

    Returns:
        either an unchanged series or a converted series with dtype datetime,
        timedelta or bool
    """

    for parser in [parse_boolean_ish, parse_timedelta, parse_datetimes]:
        try:
            return parser(series)
        except ValueError:
            pass

    return series


def parse_timedelta(series: Series) -> Series:
    if series.dtype.name != "object":
        raise ValueError
    return pandas.to_timedelta(series)


def parse_datetimes(series: Series) -> Series:
    if series.dtype.name != "object":
        raise ValueError
    series = pandas.to_datetime(series)
    series.attrs["is_date"] = all(check_if_datetime_is_a_date(s) for s in series)
    return series


def check_if_datetime_is_a_date(date_time: pandas.Timestamp):
    return date_time.normalize() == date_time


def parse_boolean_ish(series: Series) -> Series:
    if series.dtype.name not in ("object", "int64"):
        raise ValueError
    return series.apply(parse_boolean)


def parse_boolean(val: str | int) -> bool:
    """
    We want to support boolean-ish values like "yes", "no", "y" and 1.


    Args:
        val: string or integer

    Returns:
        a boolean value based on the string or an ValueError is raised

    Raises:
        ValueError if value is not boolean-ish

    """
    if isinstance(val, int):
        if val == 0:
            return False
        if val == 1:
            return True
        raise ValueError

    if val.lower() in ["true", "yes", "1", "y"]:
        return True
    if val.lower() in ["false", "no", "0", "n"]:
        return False
    raise ValueError
