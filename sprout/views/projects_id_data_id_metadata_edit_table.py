from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse

from sprout.csv.csv_reader import read_csv_file
from sprout.forms import ColumnMetadataForm
from sprout.models import ColumnMetadata, FileMetadata, TableMetadata


def projects_id_data_id_metadata_edit_table(request, table_id):
    """Takes the data from ColumnMetadata and displays as a table.

    The table can be edited and the result written back to the database.

    Args: Must learn what to write here
        request: _description_
        table_name: _description_

    Returns: Must learn what to write here
        _type_: _description_
    """
    table_metadata = get_object_or_404(TableMetadata, id=table_id)
    columns_metadata = ColumnMetadata.objects.select_related("data_type").filter(
        table_metadata=table_metadata
    )
    file = FileMetadata.objects.get(table_metadata=table_metadata)
    df = read_csv_file(file.server_file_path, 5)
    forms = [create_form(request, c) for c in columns_metadata]
    columns = [
        {
            "original_name": c.original_name,
            "title": c.title,
            "name": c.name,
            "description": c.description,
            "data_type": c.data_type.display_name,
            "data": df[c.original_name].to_list(),
            "tab-index": idx,
            "form": forms[idx],
        }
        for idx, c in enumerate(columns_metadata)
    ]

    if request.method == "POST":
        forms = [
            ColumnMetadataForm(request.POST, instance=column, prefix=str(column.id))
            for column in columns_metadata
        ]
        if all(form.is_valid() for form in forms):
            for form in forms:
                form.save()
            return redirect(
                reverse("projects-id-data-id-metadata-edit-table", args=[table_id])
            )

    else:
        forms = [
            ColumnMetadataForm(instance=column, prefix=str(column.id))
            for column in columns_metadata
        ]

    return render(
        request,
        "projects-id-data-id-metadata-edit-table.html",
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
