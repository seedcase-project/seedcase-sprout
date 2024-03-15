from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse

from sprout.forms import ColumnMetadataForm
from sprout.models import ColumnMetadata, TableMetadata


def project_id_data_id_metadata_edit_table(request, table_id):
    """Takes the data from ColumnMetadata and displays as a table.

    The table can be edited and the result written back to the database.

    Args: Must learn what to write here
        request: _description_
        table_name: _description_

    Returns: Must learn what to write here
        _type_: _description_
    """
    table_metadata = get_object_or_404(TableMetadata, id=table_id)
    columns_metadata = ColumnMetadata.objects.filter(table_metadata=table_metadata)

    if request.method == "POST":
        forms = [
            ColumnMetadataForm(request.POST, instance=column, prefix=str(column.id))
            for column in columns_metadata
        ]
        if all(form.is_valid() for form in forms):
            for form in forms:
                form.save()
            return redirect(
                reverse("project-id-data-id-metadata-edit-table", args=[table_id])
            )

    else:
        forms = [
            ColumnMetadataForm(instance=column, prefix=str(column.id))
            for column in columns_metadata
        ]

    return render(
        request,
        "project-id-data-id-metadata-edit-table.html",
        {
            "forms": forms,
            "table_metadata": table_metadata,
            "columns_metadata": columns_metadata,
        },
    )
