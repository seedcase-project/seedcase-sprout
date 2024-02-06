import pandas as pd
from django.test import TestCase
from app.models import TableMetadata, ColumnMetadata, ColumnDataType
from app.tests.db_test_utils import create_metadata_table_and_column, create_table


class MetadataTests(TestCase):
    def test_create_metadata_for_a_table_and_columns_and_verify_creation(self):
        # Arrange
        table_name = "TableName"
        column_name = "ColumnName"
        create_metadata_table_and_column(table_name, column_name)

        # Act
        table_exists = TableMetadata.objects.filter(name=table_name).exists()
        column_exists = ColumnMetadata.objects.filter(name=column_name).exists()

        # Assert
        self.assertTrue(table_exists, "Table metadata should be created")
        self.assertTrue(column_exists, "Column metadata should be created")

    def test_verify_foreign_key_constraint_by_deleting_table_which_should_delete_column(self):
        # Arrange
        create_metadata_table_and_column()

        # Act
        TableMetadata.objects.first().delete()

        # Assert
        self.assertEqual(0, TableMetadata.objects.count(), "Table should be deleted")
        self.assertEqual(0, ColumnMetadata.objects.count(), "Column should be deleted")

    def test_verify_table_is_not_deleted_when_column_is_deleted(self):
        # Arrange
        create_metadata_table_and_column()

        # Act
        ColumnMetadata.objects.first().delete()

        # Assert
        table_count = TableMetadata.objects.count()
        self.assertEqual(1, table_count, "Table should not be deleted")
        column_count = ColumnMetadata.objects.count()
        self.assertEqual(0, column_count, "Column should be deleted")

    def test_create_table_from_pandas_dataframe(self):
        table_metadata = create_table("TableName")
        table_metadata.save()
        df = pd.DataFrame(data={
            "b": [True, False],
            "s": ["Hi", "World"],
            "f": [1.2, 1.3],
            "i": [1, 2],
            "d": [pd.to_datetime("2024-02-06"), pd.to_datetime("2024-02-07 12:00:01")],
            "t": [pd.to_timedelta("00:00:00"), pd.to_timedelta("12:00:01")]
        })

        table_metadata.create_columns(df)

        self.assertEqual(6, ColumnMetadata.objects.count())
        self.assert_column_exists("b", "bool", "bool")
        self.assert_column_exists("s", "str", "object")
        self.assert_column_exists("f", "float", "float64")
        self.assert_column_exists("i", "int", "int64")
        self.assert_column_exists("d", "datetime", "datetime64[ns]")
        self.assert_column_exists("t", "timedelta", "timedelta64[ns]")

    def assert_column_exists(self, name: str, python_type: str, pandas_type: str):
        data_type = ColumnDataType.objects.filter(python_type=python_type,
                                                  pandas_type=pandas_type).first()
        column = ColumnMetadata.objects.filter(name=name, data_type=data_type).first()

        self.assertTrue(column, f"Was unable to find either type or column in database: {name}, {python_type}, {pandas_type}")
