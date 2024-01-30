import io
from typing import Any
from unittest import TestCase
import numpy
from pandas import DataFrame, Series

from app.csv_parser import read_csv_file


class CsvTests(TestCase):
    def test_csv_with_simple_types(self):
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

    def test_datetime(self):
        csv_file = io.StringIO(
            "d1,                d2,         d3,     d4\n"
            "1987-10-27 00:00:00,1987-06-27,12:00:00,\n"
            "1987-11-28 12:00:00,1987-06-28,13:00:01,\n"
            "1987-11-29 12:00:01,1987-06-29,00:00:00,"
        )

        df = read_csv_file(csv_file)

        self.assert_types(df, "datetime64[ns]", "datetime64[ns]", "timedelta64[ns]")
        self.assert_dates(
            df["d1"], "1987-10-27", "1987-11-28T12", "1987-11-29T12:00:01"
        )
        self.assert_dates(df["d2"], "1987-06-27", "1987-06-28", "1987-06-29")

    def assert_types(self, df: DataFrame, *expected: str):
        column_names = df.columns.values
        self.assertEqual(len(column_names), len(expected), "Check all columns types!")
        for idx in range(0, len(expected)):
            column_name = column_names[idx]
            column_type = df.dtypes[column_name]
            self.assertEqual(expected[idx], column_type, "column:" + column_name)

    def assert_values(self, s: Series, *expected_values: Any):
        for idx in range(0, len(s.values)):
            self.assertEqual(s.values[idx], expected_values[idx], "row:" + str(idx))

    def assert_dates(self, s: Series, *expected_dates: str):
        for idx in range(0, len(s.values)):
            date = numpy.datetime64(expected_dates[idx])
            self.assertEqual(s.values[idx], date, "row:" + str(idx))
