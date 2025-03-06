import polars as pl
from pytest import mark

from seedcase_sprout.core.sprout_checks.check_column_data_types import (
    BOOLEAN_VALUES,
    check_is_boolean,
    check_is_castable_type,
    check_is_date,
    check_is_datetime,
    check_is_geopoint,
    check_is_json,
    check_is_time,
    check_is_yearmonth,
)

# Boolean
BOOLEAN_BAD_VALUES = ["", "yes", "maybe", "99"]
BOOLEAN_GOOD_VALUES = list(BOOLEAN_VALUES)

# Yearmonth
YEARMONTH_BAD_VALUES = [
    "",
    "2002/10",
    "2002-10-10",
    "2014",
    "2014-01-01",
    "2014-01-01-01",
    "abc",
    "-0100-09",
    "1001-13",
    "10001-11",
    "10-13",
]
YEARMONTH_GOOD_VALUES = ["2014-12", "0001-01", "0000-01"]

# Date
DATE_BAD_VALUES = [
    "",
    "-0001-01-01",
    "--0001-01-01",
    "01-01",
    "99",
    "abc",
    "2002-10-10-05:00",
    "2002-10-10Z",
    "2002-02-31",
    "20022-02-02",
    "2002-02-02T06:00:00",
]
DATE_GOOD_VALUES = ["2002-10-10", "0001-01-01", "0000-01-01"]

# Time
TIME_BAD_VALUES = [
    "15:00:69",
    "-15:00:00",
    "2002-10-10T12:00:00",
    "4",
    "",
    "abc",
    "06:23:22Z",
    "12:00:00-05:00",
    "12:00:00.34-05:00",
]
TIME_GOOD_VALUES = [
    "15:00:59",
    "00:00:00",
    "12:00:00.3",
    "12:00:00.345345",
]

# Integer, Year
INTEGER_BAD_VALUES = ["", "12.23", "abc", "2E3", "INF", "NAN"]
INTEGER_GOOD_VALUES = ["12223", "-123", "+4", "000"]

# Number
NUMBER_BAD_VALUES = ["", "abc", "++4", "2,00"]
NUMBER_GOOD_VALUES = [
    "123",
    "123.123",
    "-23",
    "+45.5",
    "0003",
    "2.0000",
    "NaN",
    "NAN",
    "nan",
    "inf",
    "INF",
    "-inf",
    "-INF",
    "2E3",
    "2E-33",
]

# Geopoint
GEOPOINT_BAD_VALUES = [
    "",
    "45",
    "5 45",
    "5 , 45",
    "180, 90",
    "91, 181",
    "-91, -181",
    "A, B",
    "abc",
    "NAN",
    "INF",
]
GEOPOINT_GOOD_VALUES = [
    "90, 180",
    "-90, -180",
    "0, 0",
    "5, 45",
    "5.9999, 45.0000",
    "5,45",
]

# Array, Object, Geojson
ARRAY_GOOD_VALUES = [
    "[]",
    '[{"prop1": "value"}, {"prop2": 123}]',
]
OBJECT_GOOD_VALUES = [
    "{}",
    '{"outer": "value", "inner": {"prop1": 123, "prop2": [1, 2, null], "prop3": true}}',
]
OBJECT_BAD_VALUES = ["not,json,,"] + ARRAY_GOOD_VALUES
ARRAY_BAD_VALUES = ["not,json,,"] + OBJECT_GOOD_VALUES


@mark.parametrize(
    "bad_values, good_values, check_fn",
    [
        (BOOLEAN_BAD_VALUES, BOOLEAN_GOOD_VALUES, check_is_boolean),
        (YEARMONTH_BAD_VALUES, YEARMONTH_GOOD_VALUES, check_is_yearmonth),
        (DATE_BAD_VALUES, DATE_GOOD_VALUES, check_is_date),
        (TIME_BAD_VALUES, TIME_GOOD_VALUES, check_is_time),
        (GEOPOINT_BAD_VALUES, GEOPOINT_GOOD_VALUES, check_is_geopoint),
        (
            INTEGER_BAD_VALUES,
            INTEGER_GOOD_VALUES,
            lambda col: check_is_castable_type(col, "integer"),
        ),
        (
            INTEGER_BAD_VALUES,
            INTEGER_GOOD_VALUES,
            lambda col: check_is_castable_type(col, "year"),
        ),
        (
            NUMBER_BAD_VALUES,
            NUMBER_GOOD_VALUES,
            lambda col: check_is_castable_type(col, "number"),
        ),
        (
            ARRAY_BAD_VALUES,
            ARRAY_GOOD_VALUES,
            lambda col: check_is_json(col, list),
        ),
        (
            OBJECT_BAD_VALUES,
            OBJECT_GOOD_VALUES,
            lambda col: check_is_json(col, dict),
        ),
    ],
)
def test_check_data_type(bad_values, good_values, check_fn):
    """Given a column with both correct and incorrect values, it should mark incorrect
    values with False in another column."""
    values = bad_values + [None] + good_values
    expected_fails = list(range(len(bad_values)))
    df = pl.DataFrame({"my_values": values})

    df = df.with_columns(check_fn("my_values").alias("result"))

    fails = (
        df.with_row_index()
        .filter(pl.col("result").not_())
        .get_column("index")
        .to_list()
    )

    assert fails == expected_fails


# Datetime
DATETIME_BAD_VALUES_WHEN_TIMEZONE = [
    "",
    "2002-10-10T12:00:00",
    "2002-10-10T12:00:00",
    "-0001-01-01T00:00:00",
    "--0001-01-01T00:00:00",
    "2023-01-01",
    "2023-01-01T",
    "04:04:22",
    "2002-13-01T00:00:00",
    "2002-11-01T99:00:00",
    "2002-11-01 T 06:00:00",
    "2002-10-10T17:00:00X",
    "T",
    "4",
    "abc",
]
DATETIME_GOOD_VALUES_WHEN_TIMEZONE = [
    "2002-10-10T12:00:00+01:00",
    "2002-10-10T12:00:40-05:00",
    "2002-10-10T12:00:00.34Z",
    "2002-10-10T12:40:00.34-04:30",
    "2002-10-10T17:00:55Z",
    "0000-01-01T00:00:00Z",
]

DATETIME_BAD_VALUES_WHEN_NO_TIMEZONE = [
    "",
    "2002-10-10T12:00:00+01:00",
    "2002-10-10T12:00:40-05:00",
    "2002-10-10T12:00:00.34Z",
    "-0001-01-01T00:00:00",
    "--0001-01-01T00:00:00",
    "2023-01-01",
    "2023-01-01T",
    "04:04:22",
    "2002-13-01T00:00:00",
    "2002-11-01T99:00:00",
    "2002-11-01 T 06:00:00",
    "2002-10-10T17:00:00X",
    "T",
    "4",
    "abc",
]
DATETIME_GOOD_VALUES_WHEN_NO_TIMEZONE = [
    "2002-10-10T12:44:10",
    "2002-10-10T12:00:00.34",
    "0000-01-01T00:00:00",
]


@mark.parametrize(
    "first_value, good_values, bad_values",
    [
        (None, [None], []),
        (
            DATETIME_GOOD_VALUES_WHEN_TIMEZONE[0],
            DATETIME_GOOD_VALUES_WHEN_TIMEZONE,
            DATETIME_BAD_VALUES_WHEN_TIMEZONE,
        ),
        (
            DATETIME_GOOD_VALUES_WHEN_NO_TIMEZONE[0],
            DATETIME_GOOD_VALUES_WHEN_NO_TIMEZONE,
            DATETIME_BAD_VALUES_WHEN_NO_TIMEZONE,
        ),
        (
            None,
            DATETIME_GOOD_VALUES_WHEN_NO_TIMEZONE,
            DATETIME_GOOD_VALUES_WHEN_TIMEZONE,
        ),
        (
            "abc",
            DATETIME_GOOD_VALUES_WHEN_NO_TIMEZONE,
            DATETIME_GOOD_VALUES_WHEN_TIMEZONE,
        ),
    ],
)
def test_check_is_datetime(first_value, good_values, bad_values):
    """Given a column with both correct and incorrect datetimes, it should mark
    incorrect datetimes with False in another column. The first value should decide if
    the column is treated as timezone-aware or timezone-naive."""
    good_values.append(None)
    values = [first_value] + good_values + bad_values
    expected_fails = [i for i, value in enumerate(values) if value not in good_values]
    df = pl.DataFrame({"my_values": values}, schema={"my_values": pl.String})

    df = df.with_columns(check_is_datetime(df, "my_values").alias("result"))

    fails = (
        df.with_row_index()
        .filter(pl.col("result").not_())
        .get_column("index")
        .to_list()
    )

    assert fails == expected_fails
