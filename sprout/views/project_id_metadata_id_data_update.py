import polars as pl
from django.core.files.uploadedfile import UploadedFile
from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, render

from sprout.models import ColumnMetadata, FileMetadata, TableMetadata


def project_id_metadata_id_data_update(
    request: HttpRequest, table_id: int
) -> HttpResponse:
    """Modifies or adds data in a database table for a specific metadata object.

    Args:
        request: Takes the HTTP request from the server.
        table_id: The database Table ID.

    Returns:
        Outputs an HTTP response object.
    """
    table_metadata = get_object_or_404(TableMetadata, id=table_id)
    context = {
        "upload_success": False,
        "table_name": table_metadata.name,
    }
    if request.method == "POST":
        new_uploaded_file = get_uploaded_file(request)
        file_metadata = FileMetadata.create_file_metadata(new_uploaded_file, table_id)
        new_server_file = file_metadata.server_file_path
        # schema = get_schema(id=table_id)
        # data_update = read_csv_file(new_server_file, row_count=None)

        # TODO: Implement these below later
        # Inform if there are columns that exist in the uploaded data,
        # that don't exist in the schema
        # verify_headers(data, schema)
        # verify_data_types(data, schema)
        #   if false delete uploaded file (inside functions?)

        # TODO: We need to set up the database first, which I don't know how to do yet
        # data_current = read_database(path=Paths.database, table_name=table_id)
        # data_updated = data_current.join(other=data_update)  # from polars
        # data_updated.write_database(
        #     table_name=table_metadata.name,
        #     connection=Paths.database,
        #     # TODO: There is also append, but not sure we want to append rather than
        #     # join by ID in the table.
        #     if_table_exists="replace",
        #     # TODO: Not sure which engine to use. Alternative is "adbc"
        #     # engine="sqlalchemy"
        # )
        # TODO: verify that database has been written to.

        context = {
            "table_name": table_metadata.name,
            "upload_success": True,
            "file_metadata": file_metadata,
            "number_rows": count_rows(new_server_file),
        }

    # TODO: Provide context for response instead of redirect?
    # And button in template to move to other page?
    return render(request, "project-id-metadata-id-data-update.html", context)


class Paths:
    """List of paths used throughout Sprout."""

    # TODO: Not sure how this will look like.
    database = "PATH"


def read_database(path: str, table_name: str) -> pl.DataFrame:
    """Read a specific table from the database."""
    # TODO: Don't know how the connection will look like with Postgres
    return pl.read_database(query=f"SELECT * FROM {table_name}", connection=path)


def get_uploaded_file(request: HttpRequest) -> UploadedFile:
    """Get uploaded file name from the HTTP request."""
    return request.FILES.get("uploaded_file")


def count_rows(path: str) -> int:
    """Count the number of rows in a file."""
    # TODO: This might not always be a csv.
    data = pl.scan_csv(path)
    return data.select(pl.len()).collect().item()


def get_schema(id: int) -> ColumnMetadata:
    """Get the schema of a specific table via ColumnMetadata."""
    return ColumnMetadata.objects.get(id=id)
