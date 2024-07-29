from django.http import Http404
from frictionless import FrictionlessException, Package, Resource

from sprout.core.repository import load_project, load_resource


def get_project_or_404(project_name: str) -> "Package":
    try:
        return load_project(project_name)
    except FrictionlessException as e:
        raise Http404(e)

def get_resource_or_404(project_name: str, resource_name: str) -> "Resource":
    try:
        return load_resource(project_name, resource_name)
    except FrictionlessException as e:
        raise Http404(e)
