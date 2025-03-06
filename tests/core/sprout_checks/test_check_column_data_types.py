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
boolean_bad_values = ["", "yes", "maybe", "99"]
boolean_good_values = list(BOOLEAN_VALUES)

# Yearmonth
yearmonth_bad_values = [
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
yearmonth_good_values = ["2014-12", "0001-01", "0000-01"]

# Date
date_bad_values = [
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
date_good_values = ["2002-10-10", "0001-01-01", "0000-01-01"]

# Time
time_bad_values = [
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
time_good_values = [
    "15:00:59",
    "00:00:00",
    "12:00:00.3",
    "12:00:00.345345",
]

# Integer, Year
integer_bad_values = ["", "12.23", "abc", "2E3", "INF", "NAN"]
integer_good_values = ["12223", "-123", "+4", "000"]

# Number
number_bad_values = ["", "abc", "++4", "2,00"]
number_good_values = [
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
geopoint_bad_values = [
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
geopoint_good_values = [
    "90, 180",
    "-90, -180",
    "0, 0",
    "5, 45",
    "5.9999, 45.0000",
    "5,45",
]

# Array, Object, Geojson
array_good_values = [
    "[]",
    '[{"prop1": "value"}, {"prop2": 123}]',
]
object_good_values = [
    "{}",
    '{"outer": "value", "inner": {"prop1": 123, "prop2": [1, 2, null], "prop3": true}}',
]
object_bad_values = ["not,json,,"] + array_good_values
array_bad_values = ["not,json,,"] + object_good_values


@mark.parametrize(
    "bad_values, good_values, check_fn",
    [
        (boolean_bad_values, boolean_good_values, check_is_boolean),
        (yearmonth_bad_values, yearmonth_good_values, check_is_yearmonth),
        (date_bad_values, date_good_values, check_is_date),
        (time_bad_values, time_good_values, check_is_time),
        (geopoint_bad_values, geopoint_good_values, check_is_geopoint),
        (
            integer_bad_values,
            integer_good_values,
            lambda col: check_is_castable_type(col, "integer"),
        ),
        (
            integer_bad_values,
            integer_good_values,
            lambda col: check_is_castable_type(col, "year"),
        ),
        (
            number_bad_values,
            number_good_values,
            lambda col: check_is_castable_type(col, "number"),
        ),
        (
            array_bad_values,
            array_good_values,
            lambda col: check_is_json(col, list),
        ),
        (
            object_bad_values,
            object_good_values,
            lambda col: check_is_json(col, dict),
        ),
    ],
)
def test_check_data_type(bad_values, good_values, check_fn):
    """Given a column with both correct and incorrect values, it should mark incorrect
    values with null in another column."""
    values = bad_values + [None] + good_values
    expected_nulls = list(range(len(bad_values)))
    df = pl.DataFrame({"my_values": values})

    df = df.with_columns(check_fn("my_values").alias("result"))

    nulls = (
        df.with_row_index()
        .filter(pl.col("result").is_null())
        .get_column("index")
        .to_list()
    )

    assert nulls == expected_nulls


# Datetime
datetime_bad_values_when_timezone = [
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
datetime_good_values_when_timezone = [
    "2002-10-10T12:00:00+01:00",
    "2002-10-10T12:00:40-05:00",
    "2002-10-10T12:00:00.34Z",
    "2002-10-10T12:40:00.34-04:30",
    "2002-10-10T17:00:55Z",
    "0000-01-01T00:00:00Z",
]

datetime_bad_values_when_no_timezone = [
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
datetime_good_values_when_no_timezone = [
    "2002-10-10T12:44:10",
    "2002-10-10T12:00:00.34",
    "0000-01-01T00:00:00",
]


@mark.parametrize(
    "first_value, good_values, bad_values",
    [
        (None, [None], []),
        (
            datetime_good_values_when_timezone[0],
            datetime_good_values_when_timezone,
            datetime_bad_values_when_timezone,
        ),
        (
            datetime_good_values_when_no_timezone[0],
            datetime_good_values_when_no_timezone,
            datetime_bad_values_when_no_timezone,
        ),
        (
            None,
            datetime_good_values_when_no_timezone,
            datetime_good_values_when_timezone,
        ),
        (
            "abc",
            datetime_good_values_when_no_timezone,
            datetime_good_values_when_timezone,
        ),
    ],
)
def test_check_is_datetime(first_value, good_values, bad_values):
    """Given a column with both correct and incorrect datetimes, it should mark
    incorrect datetimes with null in another column. The first value should decide if
    the column is treated as timezone-aware or timezone-naive."""
    good_values.append(None)
    values = [first_value] + good_values + bad_values
    expected_nulls = [i for i, value in enumerate(values) if value not in good_values]
    df = pl.DataFrame({"my_values": values}, schema={"my_values": pl.String})

    df = df.with_columns(check_is_datetime(df, "my_values").alias("result"))

    nulls = (
        df.with_row_index()
        .filter(pl.col("result").is_null())
        .get_column("index")
        .to_list()
    )

    assert nulls == expected_nulls
