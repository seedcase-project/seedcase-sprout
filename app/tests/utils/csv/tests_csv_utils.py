import io
from typing import Tuple
from unittest import TestCase
from app.utils.csv import CsvColumnStats, derive_csv_column_types


class CsvUtilsTest(TestCase):

    def test_derive_column_types_from_simple_csv_file(self):
        # Arrange
        csv = io.StringIO(
            'name,      age,    age_float,  modified_at,    is_adult\n'
            '"Philip",  36,     36.5,       2023-01-24,     true'
        )

        # Act
        column_stats = derive_csv_column_types(csv)

        # Assert
        self.assertEqual(5, len(column_stats))
        self.assertColumns(column_stats,
                           ("name", "str"),
                           ("age", "int"),
                           ("age_float", "float"),
                           ("modified_at", "date"),
                           ("is_adult", "bool"))

    def test_max_row_count_3(self):
        csv = io.StringIO('c1\n1\n2\n3\n4\n5')

        columns = derive_csv_column_types(csv, max_row_count=3)

        self.assertEqual(3, columns[0].row_count)

    def test_max_row_count_no_limit(self):
        csv = io.StringIO('c1\n1\n2\n3\n4\n5')

        columns = derive_csv_column_types(csv)

        self.assertEqual(6, columns[0].row_count)

    def test_derive_columns_date_time_and_datetime(self):
        csv = io.StringIO(
            'c1,                    c2,                 c3\n'
            '1987-10-27 12:00,      1987-06-27,         12:00\n'
            '1987-09-27 12:00:00,   1987-06-27,         13:00:01\n'
            '1987-11-27 12:00:00,   1987-06-27 00:00,   00:00'
        )

        # Act
        columns = derive_csv_column_types(csv)

        # Assert
        self.assertColumns(columns, ("c1", "datetime"), ("c2", "date"), ("c3", "time"))

    def assertColumns(self, columns: list[CsvColumnStats], *name_type_list: Tuple[str, str]):
        for idx, name_type in enumerate(name_type_list):
            self.assertColumn(columns[idx], name_type_list[idx])

    def assertColumn(self, column: CsvColumnStats, name_and_type: Tuple[str, str]):
        self.assertEqual(name_and_type[0], column.name)
        self.assertEqual(name_and_type[1], column.parser.type_name, column.name)
