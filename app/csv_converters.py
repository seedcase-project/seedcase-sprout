import pandas
from pandas import Series


def convert_to_timedeltas(series: Series) -> Series:
    """
    Converts to timedeltas or raises ValueError

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


def convert_to_datetimes(series: Series) -> Series:
    """
    Converts to datetimes or raises ValueError
    Args:
        series (Series): The vector to convert:

    Returns:
        Series: A vector converted into a time data type.
    """
    if series.dtype.name != "object":
        raise ValueError
    return pandas.to_datetime(series)


def convert_to_booleans(series: Series) -> Series:
    """
    Converts a list of ints to booleans or raises ValueError
    Args:
        series (Series): The vector to convert:

    Returns:
        Series: A vector converted into booleans
    """
    if series.dtype.name != "int64":
        raise ValueError
    return series.apply(convert_int_to_boolean)


def convert_int_to_boolean(value: int) -> bool:
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
        raise ValueError("The value contains integers that are not 0 or 1, so can't convert to Boolean.")

    raise ValueError(
        "The value contains data that can't be meaningfully converted to a Boolean."
    )
