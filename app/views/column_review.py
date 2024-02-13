from django.forms import modelformset_factory
from django.shortcuts import get_object_or_404, redirect, render

from app.forms import ColumnDataTypeForm, ColumnMetadataForm
from app.models import ColumnDataType, ColumnMetadata, TableMetadata


def columndata_review(request):
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
    table_metadata = get_object_or_404(TableMetadata, name=table_name)
    columns_metadata = ColumnMetadata.objects.filter(
        table_metadata=table_metadata
    )  # .prefetch_related("data_type") doesn't seem to fetch the display_name from data_type

    if request.method == "POST":
        forms = [
            ColumnMetadataForm(request.POST, instance=column)
            for column in columns_metadata
        ]
        if all(form.is_valid() for form in forms):
            for form in forms:
                form.save()
            return redirect("home")  # Redirect to a success page
        # else:
        #     print([form.errors for form in forms])
    else:
        forms = [
            ColumnMetadataForm(instance=column) for column in columns_metadata
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
