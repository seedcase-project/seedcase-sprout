import polars
from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, render

from sprout.csv.csv_reader import read_csv_file
from sprout.helpers.paths import path_databases
from sprout.models import Columns, Files, Tables


def project_id_metadata_id_data_create(
    request: HttpRequest, table_id: int
) -> HttpResponse:
    """Creates a whole new database table for data from a specific metadata object.

    Args:
        request: Takes the HTTP request from the server.
        table_id: The Tables database ID.

    Returns:
        Outputs an HTTP response object.
    """
    tables = get_object_or_404(Tables, id=table_id)
    context = {
        "upload_success": False,
        "table_name": tables.name,
    }
    if request.method == "POST":
        files = Files.objects.get(table_metadata_id=table_id)
        data = read_csv_file(files.server_file_path, row_count=None)

        data_as_db = data.write_database(
            table_name=tables.name,
            # TODO: Connect to all other tables in project
            # TODO: Convert to Postgres
            connection=f"sqlite:///{path_databases()}/project_database.db",
            # TODO: Not sure which engine to use. Alternative is "adbc"
            # Requires sqlalchemy, pandas, and pyarrow
            # engine="sqlalchemy"
        )

        context = {
            "table_name": tables.name,
            "upload_success": True,
            "file_metadata": files,
            "number_rows": data_as_db,
        }

    # TODO: Provide context for response instead of redirect?
    # And button in template to move to other page?
    return render(request, "project-id-metadata-id-data-create.html", context)
