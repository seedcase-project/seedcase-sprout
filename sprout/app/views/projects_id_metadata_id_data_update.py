from django.core.files.uploadedfile import UploadedFile
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from sprout.app.data_access import get_resource_or_404
from sprout.core.models import File
from sprout.core.repository import link_file_to_resource, update_resource
from sprout.core.utils import count_rows


def projects_id_metadata_id_data_update(
    request: HttpRequest, resource_name: str
) -> HttpResponse:
    """Modifies or adds data in a database table for a specific metadata object.

    Args:
        request: Takes the HTTP request from the server.
        resource_name: The name of the resource.

    Returns:
        Outputs an HTTP response object.
    """
    # TODO: get project identifier from request
    resource = get_resource_or_404("sample-project", resource_name)

    context = {
        "upload_success": False,
        "table_name": resource.name,
    }
    if request.method == "POST":
        new_uploaded_file = get_uploaded_file(request)
        file = File.from_file_io(new_uploaded_file, resource.package.name)

        new_rows_added = count_rows(file.server_file_path)
        resource = link_file_to_resource(file, resource, new_rows_added)
        update_resource(resource)

        context = {
            "table_name": resource.name,
            "upload_success": True,
            "file_metadata": file,
            "number_rows": new_rows_added,
        }

    # TODO: Provide context for response instead of redirect?
    # And button in template to move to other page?
    return render(request, "projects-id-metadata-id-data-update.html", context)


def get_uploaded_file(request: HttpRequest) -> UploadedFile:
    """Get uploaded file name from the HTTP request."""
    return request.FILES.get("uploaded_file")
