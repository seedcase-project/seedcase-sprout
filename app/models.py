import pandas
from django.db import models
from django.conf import settings


class TableMetadata(models.Model):
    name = models.CharField(max_length=128)
    original_file_name = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, null=True,
                                   on_delete=models.PROTECT, related_name='creator')
    modified_at = models.DateTimeField(auto_now=True)
    modified_by = models.ForeignKey(settings.AUTH_USER_MODEL, null=True,
                                    on_delete=models.PROTECT, related_name='modifier')

    def save_file_name(self, file_name: str) -> None:
        """
        Saves the file name in the table metadata

        Args:
            file_name:
        """
        self.original_file_name = file_name
        self.save()

    def create_columns(self, df: pandas.DataFrame) -> None:
        """
        Creates and persists ColumnMetadata objects based a pandas DataFrame.

        Args:
            df: The pandas.Dataframe used for creating the ColumnMetadata objects
        """
        columns = []
        for column in df.columns:
            columns.append(
                ColumnMetadata.create_column(self.id, df[column])
            )

        ColumnMetadata.objects.bulk_create(columns)



class ColumnDataType(models.Model):
    display_name = models.TextField()
    description = models.TextField()
    pandas_type = models.TextField()
    python_type = models.TextField()


class ColumnMetadata(models.Model):
    table_metadata = models.ForeignKey(TableMetadata, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    description = models.TextField()
    data_type = models.ForeignKey(ColumnDataType, on_delete=models.PROTECT)
    allow_missing_value = models.BooleanField()
    allow_duplicate_value = models.BooleanField()

    @staticmethod
    def create_column(table_id: int, series: pandas.Series) -> 'ColumnMetadata':
        """
        Creates ColumnMetadata based on a pandas.Series

        Args:
            table_id: The id of the table
            series: The pandas.Series used for creating ColumnMetadata
        """
        return ColumnMetadata(
            table_metadata_id=table_id,
            name=series.name,
            title=series.name,
            data_type=ColumnDataType.objects.get(pandas_type=series.dtype.name),
            description="",
            allow_missing_value=True,
            allow_duplicate_value=True,
        )
