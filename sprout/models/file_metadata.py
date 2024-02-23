"""Model for a persisted file."""
import uuid
from typing import IO

from django.db import models

from config.settings import PERSISTENT_STORAGE_PATH
from sprout.models.table_metadata import TableMetadata


class FileMetaData(models.Model):
    """Model for a persisted file."""

    original_file_name = models.TextField()
    server_file_path = models.TextField()
    file_extension = models.CharField(max_length=10)

    table_metadata = models.ForeignKey(TableMetadata, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    @staticmethod
    def persist_raw_file(file: IO, table_metadata_id: int) -> "FileMetaData":
        """Persists a file and stores metadata in database.

        Args:
            file: The file to persist
            table_metadata_id: The id of the table

        Returns:
            FileMetaData: The relative path on the server
        """
        file_extension = file.name.split(".")[-1]

        # Unique file path in the raw
        server_file_path = (
            f"{PERSISTENT_STORAGE_PATH}/raw" f"/{uuid.uuid4().hex}.{file_extension}"
        )

        file.seek(0)
        # write to server_file_path
        with open(server_file_path, "wb") as target:
            target.write(file.read())

        file_metadata = FileMetaData.objects.create(
            original_file_name=file.name,
            server_file_path=server_file_path,
            file_extension=file_extension,
            table_metadata_id=table_metadata_id,
        )

        file_metadata.save()
        return file_metadata
