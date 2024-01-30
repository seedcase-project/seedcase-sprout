from unittest import TestCase

from app.csv_parser import CsvColumnStats


class CsvColumnTests(TestCase):

    def test_should_derive_int_value(self):
        # Arrange
        column_stats = CsvColumnStats("age")

        # Act
        column_stats.analyze("36")

        # Assert
        self.assertEqual("int", column_stats.type())

    def test_should_derive_float_because_one_is_float(self):
        # Arrange
        column_stats = CsvColumnStats("age")

        # Act
        column_stats.analyze("36", "36.5", "37")

        # Assert
        self.assertEqual("float", column_stats.type())

    def test_should_handle_empty_values(self):
        # Arrange
        column_stats = CsvColumnStats("age")

        # Act
        column_stats.analyze("36", " 12", "12 ", None, "")

        # Assert
        self.assertEqual("int", column_stats.type())
        self.assertEqual(123, column_stats.parser.parse("123"))
        self.assertTrue(column_stats.is_empty_detected)

    def test_should_derive_bool_for_many_boolean_like_strings(self):
        # Arrange
        column_stats = CsvColumnStats("ColumnWithBooleans")

        # Act
        column_stats.analyze("True", "YES", "False", "false", "Y", "NO", "n")

        # Assert
        self.assertEqual("bool", column_stats.type())

    def test_should_derive_string_if_not_valid_bool(self):
        # Arrange
        column_stats = CsvColumnStats("is_adult")

        # Act
        column_stats.analyze("True", "Indeed")

        # Assert
        self.assertEqual('str', column_stats.type())

    def test_should_derive_least_specific_type(self):
        # Arrange
        column_stats = CsvColumnStats("some_column")

        # Several act and assert
        column_stats.analyze("1")
        self.assertEqual("bool", column_stats.type())

        column_stats.analyze("2")
        self.assertEqual("int", column_stats.type())

        column_stats.analyze("2.2")
        self.assertEqual("float", column_stats.type())

        column_stats.analyze("2.2 Text")
        self.assertEqual("str", column_stats.type())

        # Notice that column is still described as string
        column_stats.analyze("2.2")
        self.assertEqual("str", column_stats.type())

        column_stats.analyze("2")
        self.assertEqual("str", column_stats.type())

        column_stats.analyze("1")
        self.assertEqual("str", column_stats.type())
