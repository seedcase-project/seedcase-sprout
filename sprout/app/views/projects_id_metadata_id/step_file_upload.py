
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from frictionless import FrictionlessException, Resource, describe

from sprout.app.data_access import get_resource_or_404
from sprout.app.views.projects_id_metadata_id.helpers import create_stepper_url
from sprout.core.models import File
from sprout.core.repository import (
    delete_all_files_from_resource,
    delete_file_from_resource,
    link_file_to_resource,
    update_resource,
)
from sprout.core.utils import (
    convert_to_human_readable,
    convert_to_snake_case,
    count_rows,
)


def step_file_upload(
    request: HttpRequest, resource_name: str
) -> HttpResponse | HttpResponseRedirect:
    """Renders the step for uploading a file."""
    if request.method == "POST":
        return handle_post_request_with_file(request, resource_name)

    return render_projects_id_metadata_create(request, resource_name, "")


def handle_post_request_with_file(
    request: HttpRequest, resource_name: str
) -> HttpResponse | HttpResponseRedirect:
    """Validate CSV file in post request.

    The method have two scenarios:
    - If the validation is successful, then we persist the column metadata
      and redirect to the next page in the flow
    - If the validation fails, an exception is raised StopUpload. The page
      is re-rendered with the error message

    Args:
        request: http request from the user/browser
        resource_name: the name of the Resource where the file belongs

    Returns: A HttpResponseRedirect when validation is successful or
    HttpResponse when validation fails

    """
    file = request.FILES.get("uploaded_file", None)

    # Delete exiting files, if user resubmits a file
    resource = get_resource_or_404("sample-project", resource_name)
    delete_all_files_from_resource(resource)

    # To limit memory-usage we persist the file
    file_meta = File.from_file_io(file, resource.package.name)

    try:  
        inferred_resource: Resource = describe(file_meta.server_file_path, type="resource")
        inferred_resource.name = resource.name
        inferred_resource.description = resource.description

        for field in inferred_resource.schema.fields:
            field.custom["extracted_name"] = field.name
            field.custom["machine_readable_name"] = convert_to_snake_case(field.name)
            field.title = convert_to_human_readable(field.name)

        rows_added = count_rows(file.server_file_path)
        inferred_resource = link_file_to_resource(
            file_meta, 
            inferred_resource, 
            rows_added
        )

        update_resource(inferred_resource)
        
    except FrictionlessException as e:
        delete_file_from_resource(file_meta, resource)
        return render_projects_id_metadata_create(request, resource_name, e.args[0])

    return redirect(create_stepper_url(3, resource_name))


def render_projects_id_metadata_create(
    request: HttpRequest, resource_name: str, upload_error: str
) -> HttpResponse:
    """Render page with an error if there is any.

    Args:
        request: The http request
        resource_name: The name of the Resource
        upload_error: The error message if there is any

    Returns:
        HttpResponse: A html page based on the template
    """
    context = {
        "table_name": resource_name,
        "upload_error": upload_error,
    }
    return render(request, "projects-id-metadata-create.html", context)
