"""Module defining forms."""

from django.forms import ModelForm

from sprout.models.table_metadata import TableMetadata
from sprout.validators import (
    validate_no_special_characters,
    validate_table_name_does_not_exist,
)


class TableMetadataForm(ModelForm):
    """ModelForm for creating TableMetaData."""

    class Meta:
        """A class required by Django in a ModelForm.

        Defines which model is used and which fields that are included.
        """

        model = TableMetadata
        fields = ["name", "description"]

    def clean_name(self) -> str:
        """Clean and validate field name.

        Adds extra validations for the field "name" on top of the validations
        defined by the model.

        Raises:
            ValidatorError: If either table name exists in the database or the name
            includes special characters.

        Returns:
            str: The cleaned value of the "name" field.
        """
        name_value = self.cleaned_data.get("name")

        validate_table_name_does_not_exist(name=name_value)

        validate_no_special_characters(field_name="name", field_value=name_value)

        return name_value
