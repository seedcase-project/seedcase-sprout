from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from sprout.models import Tables


def step_confirmation(
    request: HttpRequest, table_id: int
) -> HttpResponse | HttpResponseRedirect:
    table = Tables.objects.prefetch_related("columns_set").get(pk=table_id)
    context = {"table": table}
    """Renders page final page when creating metadata table."""
    return render(request, "projects_id_metadata_id/create.html", context)
