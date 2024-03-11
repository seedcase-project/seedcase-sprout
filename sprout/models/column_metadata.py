"""Module defining the ColumnMetadata model."""
from re import sub

import polars
from django.db import models

from sprout.models.column_data_type import ColumnDataType
from sprout.models.table_metadata import TableMetadata


class ColumnMetadata(models.Model):
    """Model representing the metadata of columns."""

    table_metadata = models.ForeignKey(TableMetadata, on_delete=models.CASCADE)
    original_name = models.CharField(max_length=1000)
    name = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    data_type = models.ForeignKey(ColumnDataType, on_delete=models.PROTECT)
    allow_missing_value = models.BooleanField()
    allow_duplicate_value = models.BooleanField()

    @staticmethod
    def create(table_id: int, series: polars.Series) -> "ColumnMetadata":
        """Create ColumnMetadata from polars.Series.

        Args:
            table_id: id of the table
            series: A polars series

        Returns:
            ColumnMetadata: ColumnMetadata instance based on series
        """
        return ColumnMetadata(
            table_metadata_id=table_id,
            original_name=series.name,
            name=_convert_to_snake_case(series.name),
            title=series.name,
            description="",
            data_type=ColumnDataType.get_from_series(series),
            allow_missing_value=True,
            allow_duplicate_value=True,
        )


def _convert_to_snake_case(string: str) -> str:
    """This function takes a string and converts it to snake case.

    Args:
        string: A string to be converted to snake case

    Returns:
        A string that has been converted to snake case
    """
    # Remove trailing white spaces
    altered_string = string.strip()

    # Remove non-alphanumeric characters
    altered_string = sub("[^a-zA-Z0-9\s_-]+", "", altered_string)

    # Replace spaces and hyphens with underscores
    altered_string = sub(r"[\s-]+", "_", altered_string)

    # Convert camelCase to snake_case
    altered_string = sub(r"([a-z0-9])([A-Z])", r"\1_\2", altered_string)

    # Handle consecutive uppercase letters followed by lowercase letters (i.e., CAPS)
    altered_string = sub(r"([A-Z])([A-Z][a-z])", r"\1_\2", altered_string)

    return altered_string.lower()
