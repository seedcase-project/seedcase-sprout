from django.forms import modelformset_factory
from django.shortcuts import get_object_or_404, redirect, render

from app.forms import ColumnDataTypeForm, ColumnMetadataForm
from app.models import ColumnDataType, ColumnMetadata, TableMetadata


def columndata_review(request):
    """Displays the data type, more of a test than useful.

    This was built as a first try, don't know if we are going to use it
    but keeping it for now.
    """
    ColumnDataTypeFormSet = modelformset_factory(
        ColumnDataType, form=ColumnDataTypeForm
    )
    formset = ColumnDataTypeFormSet(queryset=ColumnDataType.objects.all())

    return render(
        request,
        "columndata-review.html",
        {"formset": formset},
    )


def column_review(request, table_name):
    """Takes the data from ColumnMetadata and displays as a table.

    The table can be edited and the result written back to the db

    Args: Must learn what to write here
        request (_type_): _description_
        table_name (_type_): _description_

    Returns: Must learn what to write here
        _type_: _description_
    """
    table_metadata = get_object_or_404(TableMetadata, name=table_name)
    columns_metadata = ColumnMetadata.objects.filter(table_metadata=table_metadata)

    if request.method == "POST":
        forms = [
            ColumnMetadataForm(request.POST, instance=column, prefix=str(column.id))
            for column in columns_metadata
        ]
        if all(form.is_valid() for form in forms):
            for form in forms:
                form.save()
            return redirect("home")  # Redirect to a success page
        else:
            print([form.errors for form in forms])
    else:
        forms = [
            ColumnMetadataForm(instance=column, prefix=str(column.id))
            for column in columns_metadata
        ]

    return render(
        request,
        "column-review.html",
        {
            "forms": forms,
            "table_metadata": table_metadata,
            "columns_metadata": columns_metadata,
        },
    )
