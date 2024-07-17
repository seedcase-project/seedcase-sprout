from django.http import HttpRequest, HttpResponse, HttpResponseRedirect

from sprout.app.views.projects_id_metadata_id.step_columns import step_columns
from sprout.app.views.projects_id_metadata_id.step_confirmation import step_confirmation
from sprout.app.views.projects_id_metadata_id.step_file_upload import step_file_upload
from sprout.app.views.projects_id_metadata_id.step_name_and_description import (
    step_name_and_description,
)


def projects_id_metadata_create(
    request: HttpRequest,
) -> HttpResponse | HttpResponseRedirect:
    """Responsible for rendering a "stepper"-form for creating metadata.

    The user needs to complete several steps for creating metadata. Only one step is
    displayed/validated at the time. This is ensured by a query parameter called "step".

    All steps use the same template "projects_id_metadata_id/create.html" with several
    conditional include-statements: one for each step.

    This function/view is responsible for delegating to the correct view/function based
    on "step".
    """
    table_id = int(request.GET["table_id"]) if "table_id" in request.GET else None
    step = request.GET.get("step")

    # Step 2
    if step == "2":
        return step_file_upload(request, table_id)

    # Step 3
    if step == "3":
        return step_columns(request, table_id)

    # Step 4
    if step == "4":
        return step_confirmation(request, table_id)

    # Step 1
    return step_name_and_description(request, table_id)
