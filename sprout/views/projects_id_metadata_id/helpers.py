from django.urls import reverse


def create_stepper_url(step: int, table_id: int) -> str:
    """Creates url for a step when creating metadata."""
    qp = "?table_id=" + str(table_id) + "&step=" + str(step)
    return reverse("projects-id-metadata-create") + qp


def update_stepper_url(step: int, table_id: int) -> str:
    """Creates url for a step when creating metadata."""
    qp = "?table_id=" + str(table_id) + "&step=" + str(step)
    return reverse("projects-id-metadata-id-update", args=[table_id]) + qp
