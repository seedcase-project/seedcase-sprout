from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from frictionless import Resource

from sprout.app.data_access import get_project_or_404
from sprout.app.forms import ResourceForm
from sprout.app.views.projects_id_metadata_id.helpers import create_stepper_url
from sprout.core.repository import upsert_resource


def step_name_and_description(
    request: HttpRequest, resource_name: str | None
) -> HttpResponse | HttpResponseRedirect:
    """Renders step creating/editing metadata name and description."""
    project = get_project_or_404("sample-project")

    form = ResourceForm(data=None)
    resource = Resource()

    if resource_name:
        resource: Resource = project.get_resource(resource_name)
        initial_data = {"name": resource.name, "description": resource.description}
        form = ResourceForm(initial=initial_data)

    if request.method == "POST":
        form = ResourceForm(data=request.POST)
        if resource_name:
            form = ResourceForm(data=request.POST, initial=initial_data)

        if form.is_valid():
            resource.name = form.cleaned_data["name"]
            resource.description = form.cleaned_data["description"]
            upsert_resource(project, resource)

            return redirect(create_stepper_url(2, resource.name))

    context = {
        "form": form,
    }
    return render(request, "projects-id-metadata-create.html", context)
