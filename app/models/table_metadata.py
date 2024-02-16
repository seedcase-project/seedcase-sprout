"""Module defining the TableMetaData model."""
import polars
from django.conf import settings
from django.db import models

import app


class TableMetadata(models.Model):
    """Model representing the table metadata."""

    name = models.CharField(max_length=128)
    original_file_name = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=True,
        on_delete=models.PROTECT,
        related_name="creator",
    )
    modified_at = models.DateTimeField(auto_now=True)
    modified_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=True,
        on_delete=models.PROTECT,
        related_name="modifier",
    )

    def save_original_file_name(self, original_file_name: str) -> None:
        """Saves the original file name to the model.

        Args:
            original_file_name: Name of the file used for deriving column types
        """
        self.original_file_name = original_file_name
        self.save()

    def create_columns(self, df: polars.DataFrame) -> None:
        """Creates and persists ColumnMetaData based on a DataFrame.

        Args:
            df: A DataFrame of series which should be mapped to ColumMetaData
        """
        for column in df.columns:
            app.models.ColumnMetadata.create_column(self.id, df[column]).save()
