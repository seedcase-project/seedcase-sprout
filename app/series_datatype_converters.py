import pandas
from pandas import Series


def convert_to_timedeltas(series: Series) -> Series:
    """
    Converts to timedeltas or raises ValueError

    Args:
        series (Series): The vector to parse.

    Raises:
        ValueError: If not able to convert to timedelta

    Returns:
        Series: A vector converted into a time data type.
    """

    # A string like `12:00:01` is required. A panda `object` is a string
    if series.dtype.name == "object":
        return pandas.to_timedelta(series)

    raise ValueError("Not able to convert to timedelta")


def convert_to_datetimes(series: Series) -> Series:
    """
    Converts to datetimes or raises ValueError
    Args:
        series (Series): The vector to convert:

    Raises:
        ValueError: If not able to convert to datetime

    Returns:
        Series: A vector converted into a time data type.
    """

    # A string like `2024-02-08 12:00:01` is required. A panda `object` is a string
    if series.dtype.name == "object":
        return pandas.to_datetime(series)

    raise ValueError("Not able to convert to datetime")


def convert_to_booleans(series: Series) -> Series:
    """
    Converts a list of ints of 0 or 1 to booleans or raises ValueError
    Args:
        series (Series): The vector to convert:

    Raises:
        ValueError: If not able to convert to booleans

    Returns:
        Series: A vector converted into booleans
    """
    if series.dtype.name == "int64":
        return series.apply(_convert_int_to_boolean_or_raise)

    raise ValueError("Not able to convert to booleans")


def _convert_int_to_boolean_or_raise(value: int) -> bool:
    """
    Converts an int to a boolean value or raises ValueError

    This converts 0 and 1 to actual boolean values.

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
        raise ValueError("Not able to convert to boolean")

    raise ValueError(
        "The value contains data that can't be meaningfully converted to a Boolean."
    )
