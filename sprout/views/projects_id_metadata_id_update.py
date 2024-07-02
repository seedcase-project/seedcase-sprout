from django.http import HttpRequest, HttpResponse, HttpResponseRedirect

from sprout.views.projects_id_metadata_id.step_columns import step_columns
from sprout.views.projects_id_metadata_id.step_name_and_description import (
    step_name_and_description,
)


def projects_id_metadata_id_update(
    request: HttpRequest, table_id: int
) -> HttpResponse | HttpResponseRedirect:
    """Responsible for rendering a "stepper"-form for creating metadata.

    The user needs to complete several steps for creating metadata. Only one step is
    displayed/validated at the time. This is ensured by a query parameter called "step".

    All steps use the same template "projects_id_metadata_id/create.html" with several
    conditional include-statements: one for each step.

    This function/view is responsible for delegating to the correct view/function based
    on "step".
    """
    step = request.GET.get("step")

    # Step 2
    if step == "2":
        return step_columns(request, table_id, update=True)

    # Step 1
    return step_name_and_description(request, table_id, update=True)
