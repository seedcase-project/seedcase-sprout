from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, get_object_or_404

from sprout.models import FileMetadata, TableMetadata
import polars as pl


def project_id_data_id_upload(request: HttpRequest, table_id: int) -> HttpResponse:
    """Upload a data file to a specific database table.

    Args:
        request: _description_
        table_id: _description_

    Returns:
        _description_
    """
    table_metadata = get_object_or_404(TableMetadata, id=table_id)
    context = {
        "upload_success": False,
        "table_name": table_metadata.name,
    }
    if request.method == "POST":
        uploaded_file = get_uploaded_file(request)
        file_metadata = FileMetadata.create_file_metadata(uploaded_file, table_id)
        data = pl.scan_csv(file_metadata.server_file_path)
        number_rows = data.select(pl.len()).collect().item()
        context = {
            "table_name": table_metadata.name,
            "upload_success": True,
            "file_metadata": file_metadata,
            "number_rows": number_rows,
        }

    # TODO: Provide context for response instead of redirect?
    # And button in template to move to other page?
    return render(request, "project-id-data-id-upload.html", context)


def get_uploaded_file(request: HttpRequest) -> UploadedFile:
    """Get uploaded file name from request."""
    return request.FILES.get("uploaded_file")


FileMetadata.update(field_name=object)

def get_table_id(metadata: FileMetadata) -> str:

FileMetadata.add_row(column_name=object)
upload(input_path, output_path)
new_data = read_raw_file(input_path)
get_schema(table_id)

# Inform if there are columns that exist in the uploaded data,
# that don't exist in the
validate_column_names_from_schema(data, schema)


validate_data_types_from_schema(data, schema)
read_database(path, table_name)
database.join(other=new_data)  # from polars
create_path(...)
database.write_database(table_name=table_name, connection=path)
