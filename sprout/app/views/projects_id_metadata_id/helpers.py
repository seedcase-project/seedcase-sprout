from django.urls import reverse


def create_stepper_url(step: int, resource_name: str) -> str:
    """Creates url for a step when creating metadata."""
    qp = "?resource_name=" + resource_name + "&step=" + str(step)
    return reverse("projects-id-metadata-create") + qp
