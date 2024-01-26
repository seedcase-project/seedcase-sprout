import datetime
from unittest import TestCase

from app.utils.csv import CsvColumnStats, parse_boolean, parse_date, parse_datetime, \
    parse_time


class TypeParserTests(TestCase):
    def test_parse_boolean_should_return_true(self):
        self.assertTrue(parse_boolean('True'))
        self.assertTrue(parse_boolean('1'))
        self.assertTrue(parse_boolean('YES'))
        self.assertTrue(parse_boolean('Y'))

    def test_parse_boolean_should_return_false(self):
        self.assertFalse(parse_boolean('False'))
        self.assertFalse(parse_boolean('0'))
        self.assertFalse(parse_boolean('NO'))
        self.assertFalse(parse_boolean('N'))

    def test_parse_time(self):
        self.assertEqual(datetime.time(0, 0, 1), parse_time("00:00:01"))
        self.assertEqual(datetime.time(23, 1, 1), parse_time("23:01:01"))
        self.assertEqual(datetime.time(23, 1, 1, 1), parse_time("23:01:01.000001"))
        self.assertEqual(datetime.time(1, 0), parse_time("01:00"))
        self.assertEqual(datetime.time(0, 1), parse_time("00:01"))
        self.assertEqual(datetime.time(0, 0), parse_time("00:00"))

    def test_parse_time_should_fail(self):
        # Time is very strict it needs to be in the format 12:01:10 or 12:01:10.00001
        self.assertRaises(ValueError, parse_time, "00.00.00")
        self.assertRaises(ValueError, parse_time, "01")
        self.assertRaises(ValueError, parse_time, "1")
        self.assertRaises(ValueError, parse_time, "1")

    def test_parse_date(self):
        self.assertEqual("2024-01-25", str(parse_date("2024-01-25")))
        self.assertEqual("2024-01-25", str(parse_date("2024-01-25 00:00:00")))
        self.assertEqual("2024-01-25", str(parse_date("2024/01/25")))
        self.assertEqual("2024-01-25", str(parse_date("25-01-2024")))
        self.assertEqual("2024-01-25", str(parse_date("25/01/2024")))
        self.assertEqual("2024-01-25", str(parse_date("Thu Jan 25 2024")))
        self.assertEqual("2024-01-25", str(parse_date("25. January 2024")))
        self.assertEqual("2024-01-25", str(parse_date("25. Jan. 2024")))
        self.assertEqual("2024-01-25", str(parse_date("20240125")))
        self.assertEqual("2024-01-25", str(parse_date("2024.01.25")))
        self.assertEqual("2024-01-25", str(parse_date("2024 01 25")))

    def test_parse_date_should_fail(self):
        self.assertRaises(ValueError, parse_date, "2024-01-25 12:00:00")
        self.assertRaises(ValueError, parse_date, "2024-01-25 00:01:00")
        self.assertRaises(ValueError, parse_date, "2024-01-25 00:00:01")
        self.assertRaises(ValueError, parse_date, "2024-01-25 00:00:00:123123")
        self.assertRaises(ValueError, parse_date, "1")
        self.assertRaises(ValueError, parse_date, "2024011")
        self.assertRaises(ValueError, parse_date, "2024.11")

    def test_parse_date_should_fail(self):
        self.assertRaises(ValueError, parse_datetime, "1")
        self.assertRaises(ValueError, parse_datetime, "0")

    def test_datetime_parser(self):
        csv_column = CsvColumnStats("a_column_with_datetime")
        self.assertEqual("date", csv_column.analyze("2024-01-25"))
        self.assertEqual("date", csv_column.analyze("25-01-2024"))
        self.assertEqual("datetime", csv_column.analyze("2024-01-25 12:00:00"))

    def test_parse_boolean_should_raise_error_when_fails(self):
        try:
            parse_boolean("Indeed")
            self.assertTrue(False, "We expect ValueError, so this should never run")
        except ValueError:
            self.assertTrue(True, "We expect to raise ValueError")
