"""Tests for forms."""
from django.test import TestCase

from sprout.forms import ColumnMetadataForm
from sprout.models import ColumnDataType, TableMetadata


class ColumnMetadataFormTest(TestCase):
    """Class of tests for the Metadata form."""

    def setUp(self):
        """Creating the data needed for the tests."""
        # Arrange: Create test instances for models
        self.table_metadata = TableMetadata.objects.create(name="TestTableKB")
        self.column_data_type = ColumnDataType.objects.create(
            display_name="TestStringFormat"
        )

    def test_form_invalid_when_no_data(self):
        """Test that a form created without data is invalid."""
        # Arrange: Create an instance of the form without providing any data
        form = ColumnMetadataForm()

        # Act: Check if the form is not valid
        is_valid = form.is_valid()

        # Assert: Ensure the form is not valid
        self.assertFalse(is_valid)

    def test_form_valid_data(self):
        """Test that the validation works on correct data."""
        # Arrange: Create valid form data
        form_data = {
            "table_metadata": self.table_metadata.id,
            "name": "TestName",
            "title": "TestTitle",
            "description": "This is the Description",
            "data_type": self.column_data_type.id,
            "allow_missing_value": True,
            "allow_duplicate_value": False,
        }

        # Act: Create an instance of the form with valid data
        form = ColumnMetadataForm(data=form_data)
        is_valid = form.is_valid()

        # Assert: Ensure the form is valid
        self.assertTrue(is_valid)

    def test_form_invalid_data(self):
        """Test that the validation works on wrong data and throws an error."""
        # Arrange: Create invalid form data
        invalid_form_data = {
            "table_metadata": self.table_metadata.id,
            "name": "",
            "title": "",
            "description": "Description",
            "data_type": self.column_data_type.id,
            "allow_missing_value": True,
            "allow_duplicate_value": False,
        }

        # Act: Create an instance of the form with invalid data
        form = ColumnMetadataForm(data=invalid_form_data)
        is_valid = form.is_valid()

        # Assert: Ensure the form is not valid
        self.assertFalse(is_valid)
