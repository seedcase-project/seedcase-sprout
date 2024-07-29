"""File with column_review view."""

from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from sprout.core.repository import load_project


def projects_id_metadata_view(request: HttpRequest) -> HttpResponse:
    """View the existing metadata in a project.

    Either create new metadata, update existing metadata, or upload new data.

    Args:
        request: The HTTP request object that contains metadata about the request.

    Returns:
        HTTP response that either renders the projects-id-metadata page or redirects
        to create new metadata, update existing metadata, or upload new data.
    """
    # TODO: get project identifier from request
    project = load_project("sample-project")

    return render(
        request=request,
        template_name="projects-id-metadata-view.html",
        context={"project": project},
    )
