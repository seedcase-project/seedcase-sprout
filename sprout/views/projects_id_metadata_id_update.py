"""File with column_review view."""
from typing import Dict, List

from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse

from sprout.csv.csv_reader import read_csv_file
from sprout.forms import ColumnMetadataForm
from sprout.models import ColumnMetadata, FileMetadata, TableMetadata


def projects_id_metadata_id_update(request: HttpRequest, table_id: int) -> HttpResponse:
    """Takes the data from ColumnMetadata and displays the metadata to update.

    The metadata can be edited and the result written back to the column metadata
    database.

    Args:
        request: The HTTP request sent from the server (by the user).
        table_id: The ``table_id`` from TableMetadata.

    Returns:
        HttpResponse: A response given back to the server.
    """
    table_metadata = get_object_or_404(TableMetadata, id=table_id)
    columns_metadata = ColumnMetadata.objects.select_related("data_type").filter(
        table_metadata=table_metadata
    )
    data_sample = create_sample_of_unique_values(table_metadata.id)
    forms = [create_form(request, c) for c in columns_metadata]
    columns = [
        {
            "id": c.id,
            "extracted_name": c.extracted_name,
            "machine_readable_name": c.machine_readable_name,
            "display_name": c.display_name,
            "description": c.description,
            "data_type": c.data_type.display_name,
            "data": data_sample[c.extracted_name],
            "form": forms[idx],
        }
        for idx, c in enumerate(columns_metadata)
    ]

    if request.method == "POST":
        for form in forms:
            if form.is_valid():
                form.save()

            # Delete excluded columns
            if form.cleaned_data["excluded"]:
                form.instance.delete()

        return redirect(reverse("projects-id-metadata-id-update", args=[table_id]))

    return render(
        request,
        "projects-id-metadata-id-update.html",
        {
            "forms": forms,
            "table_metadata": table_metadata,
            "columns": columns,
        },
    )


def create_form(request: HttpRequest, column: ColumnMetadata) -> ColumnMetadataForm:
    """Create form based on request can ColumnMetadata.

    Args:
        request: The HttpRequest sent.
        column: Django model data from ColumnMetaData.

    Returns:
        Outputs the ColumnMetadataForm Django model object.
    """
    if request.method == "POST":
        return ColumnMetadataForm(request.POST, instance=column, prefix=str(column.id))
    else:
        return ColumnMetadataForm(instance=column, prefix=str(column.id))


def create_sample_of_unique_values(table_metadata_id: int) -> Dict[str, List]:
    """Create sample of unique values based on the uploaded file for a table.

    The unique values are based on the first 500 rows.

    Args:
        table_metadata_id: The id of the table

    Returns:
        Dict[str, List]: Dictionary of unique sample values grouped by column name.
    """
    file = FileMetadata.objects.get(table_metadata_id=table_metadata_id)
    df = read_csv_file(file.server_file_path, 500)

    # Find unique values, and limit to max 5 different
    return dict(
        [(s.name, s.unique(maintain_order=True).limit(5).to_list()) for s in df]
    )
