import csv
import io
from typing import Any
from unittest import TestCase
import numpy
from pandas import DataFrame, Series, Timedelta

from app.csv_reader import read_csv_file


class CsvTests(TestCase):
    def test_csv_with_simple_types(self):
        """
        Testing that `read_csv_file()` should derive column "i1" as integer, "f1" as float
        and "b1" as a boolean, and that the values are also verified.
        """
        csv_file = io.StringIO(
            "i1,f1,b1\n"
            "1,2.3,true\n"
            "2,2.4,false\n"
            "3,2.6,false"
        )

        df = read_csv_file(csv_file)

        self.assert_types(df, "int64", "float64", "bool")
        self.assert_values(df["i1"], 1, 2, 3)
        self.assert_values(df["f1"], 2.3, 2.4, 2.6)
        self.assert_values(df["b1"], True, False, False)

    def test_csv_with_semicolon_and_whitespace(self):
        """
        Testing a different csv dialect with semicolon and initial whitespace.
        """
        csv_file = io.StringIO(
            "i1;    f1;     b1;     s1\n"
            "10;    5.3;    True;   Hi\n"
            "11;    1.0;    False;  Hello\n"
            "12;    1;      False;  Man"
        )

        df = read_csv_file(csv_file)

        self.assert_types(df, "int64", "float64", "bool", "object")
        self.assert_values(df["i1"], 10, 11, 12)
        self.assert_values(df["f1"], 5.3, 1, 1)
        self.assert_values(df["b1"], True, False, False)
        self.assert_values(df["s1"], "Hi", "Hello", "Man")

    def test_boolean_ish_values(self):
        """
        Testing boolean-ish values are derived as booleans and that the values are
        converted correctly.
        """
        csv_file = io.StringIO(
            "b1,b2,b3,b4\n"
            "0,true,yes,y\n"
            "1,false,no,y\n"
            "0,false,yes,n"
        )

        df = read_csv_file(csv_file)

        self.assert_types(df, "bool", "bool", "bool", "bool")
        self.assert_values(df["b1"], False, True, False)
        self.assert_values(df["b2"], True, False, False)
        self.assert_values(df["b3"], True, False, True)
        self.assert_values(df["b4"], True, True, False)

    def test_boolean_ish_values_should_fallback_to_string(self):
        """
        Testing that columns with values that are not boolean-ish will remain as
        objects/strings
        """
        csv_file = io.StringIO(
            "s1,    s2\n"
            "0,     true\n"
            "YEAH,  REALLY TRUE!\n"
            "0,     false"
        )

        df = read_csv_file(csv_file)

        self.assert_types(df, "object", "object")
        self.assert_values(df["s1"], "0", "YEAH", "0")
        self.assert_values(df["s2"], "true", "REALLY TRUE!", "false")

    def test_datetime(self):
        """
        Testing different date formats (d1, d2, d3) and a single time column (t1).
        """
        csv_file = io.StringIO(
            "d1,                    d2,         d3,             t1\n"
            "1987-10-27 00:00:00,   1987-10-27, 27. Oct 1987,   12:00:00\n"
            "2000-01-28 12:00:00,   2000-01-28, 28. Jan 2000,   13:00:01\n"
            "2024-07-01 12:00:01,   2024-07-01, 1. Jul 2024,    00:00:00"
        )

        df = read_csv_file(csv_file)

        self.assert_types(
            df, "datetime64[ns]", "datetime64[ns]", "datetime64[ns]", "timedelta64[ns]"
        )
        self.assert_dates(
            df["d1"], "1987-10-27", "2000-01-28T12", "2024-07-01T12:00:01"
        )
        self.assert_dates(df["d2"], "1987-10-27", "2000-01-28", "2024-07-01")
        self.assert_dates(df["d3"], "1987-10-27", "2000-01-28", "2024-07-01")
        self.assert_values(
            df["t1"],
            Timedelta("12:00:00"),
            Timedelta("13:00:01"),
            Timedelta("00:00:00"),
        )

    def test_wrongly_formatted_csv(self):
        """
        Testing a wrongly formatted CSV file with
        2 columns but three values in a row.
        A csv.Error is expected

        """
        csv_file = io.StringIO(
            "s1,s2\n"
            "Hello, World, Seedcase"
        )

        self.assertRaises(csv.Error, read_csv_file, csv_file)

    def assert_types(self, df: DataFrame, *expected_types: str):
        """
        Asserts that a DataFrame have the expected_types. This is a shorthand way
        of testing the types

        Args:
            df: The DataFrame with data and types
            *expected_types: a list of types we expect (in order)
        """
        column_names = df.columns.values
        self.assertEqual(len(column_names), len(expected_types), "Missing columns!")
        for column_position in range(0, len(expected_types)):
            column_name = column_names[column_position]
            column_type = df.dtypes[column_name]
            self.assertEqual(
                expected_types[column_position], column_type, "column:" + column_name
            )

    def assert_values(self, s: Series, *expected_values: Any):
        """
        A shorthand function asserting that a Series contain the `expected_values`.

        Args:
            s: A Series is a column of data
            *expected_types: a list of types we expect (in order)
        """
        for value_position in range(0, len(s.values)):
            self.assertEqual(
                s.values[value_position],
                expected_values[value_position],
                "row:" + str(value_position),
            )

    def assert_dates(self, s: Series, *expected_dates: str):
        """
        A shorthand function asserting that a Series contain the expected_dates.

        Args:
            s: A Series is a column of data
            *expected_dates: a list of types we expect (in order)
        """
        for value_position in range(0, len(s.values)):
            date = numpy.datetime64(expected_dates[value_position])
            self.assertEqual(
                s.values[value_position], date, "row:" + str(value_position)
            )
