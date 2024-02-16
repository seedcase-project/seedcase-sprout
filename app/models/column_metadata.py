"""Module defining the ColumnMetadata model."""
import polars
from django.db import models

from app.models.column_data_type import COLUMN_DATA_TYPES, ColumnDataType
from app.models.table_metadata import TableMetadata


class ColumnMetadata(models.Model):
    """Model representing the metadata of columns."""

    table_metadata = models.ForeignKey(TableMetadata, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    description = models.TextField()
    data_type = models.ForeignKey(ColumnDataType, on_delete=models.PROTECT)
    allow_missing_value = models.BooleanField()
    allow_duplicate_value = models.BooleanField()

    @staticmethod
    def create_column(table_id: int, series: polars.Series) -> "ColumnMetadata":
        """Creates ColumnMetadata based on a pandas.Series.

        Args:
            table_id: The id of the table
            series: The polars.Series used for creating ColumnMetadata
        """
        return ColumnMetadata(
            table_metadata_id=table_id,
            name=series.name,
            title=series.name,
            data_type=ColumnMetadata.find_column_data_type_from_series(series),
            description="",
            allow_missing_value=True,
            allow_duplicate_value=True,
        )

    @staticmethod
    def find_column_data_type_from_series(series: polars.Series) -> ColumnDataType:
        """Finds ColumnDataType from a series dtype.

        Args:
            series: The polars.Series to find ColumnDataType from
        """
        series_polar_type = str(series.dtype.base_type())

        for data_type in COLUMN_DATA_TYPES:
            if series_polar_type in data_type.polars_types.split(","):
                return data_type

        raise ValueError("ColumnMetaData not found for :" + series_polar_type)
