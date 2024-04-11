"""Module defining the Columns model."""

from re import sub

import polars
from django.db import models

from sprout.models.data_types import DataTypes
from sprout.models.tables import Tables


class Columns(models.Model):
    """Model representing the metadata of columns."""

    tables = models.ForeignKey(Tables, on_delete=models.CASCADE, related_name="columns")
    extracted_name = models.CharField(max_length=1000)
    machine_readable_name = models.CharField(max_length=200)
    display_name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    data_type = models.ForeignKey(DataTypes, on_delete=models.PROTECT)
    allow_missing_value = models.BooleanField()
    allow_duplicate_value = models.BooleanField()

    @staticmethod
    def create(table_id: int, series: polars.Series) -> "Columns":
        """Create Columns from polars.Series.

        Args:
            table_id: id of the table
            series: A polars series

        Returns:
            Columns: Columns instance based on series
        """
        return Columns(
            tables_id=table_id,
            extracted_name=series.name,
            machine_readable_name=_convert_to_snake_case(series.name),
            display_name=_convert_to_human_readable(series.name),
            description="",
            data_type=DataTypes.get_from_series(series),
            allow_missing_value=True,
            allow_duplicate_value=True,
        )


def _convert_to_snake_case(string: str) -> str:
    """This function takes a string and converts it to snake case.

    Args:
        string: A string to be converted to snake case

    Returns:
        A string that has been converted to snake case
    """
    # Remove trailing white spaces
    altered_string = string.strip()

    # Remove non-alphanumeric characters
    altered_string = sub(r"[^a-zA-Z0-9\s_-]+", "", altered_string)

    # Replace spaces and hyphens with underscores
    altered_string = sub(r"[\s-]+", "_", altered_string)

    # Convert camelCase to snake_case
    altered_string = sub(r"([a-z0-9])([A-Z])", r"\1_\2", altered_string)

    # Handle consecutive uppercase letters followed by lowercase letters (i.e., CAPS)
    altered_string = sub(r"([A-Z])([A-Z][a-z])", r"\1_\2", altered_string)

    return altered_string.lower()


def _convert_to_human_readable(string: str) -> str:
    """This function takes a string and converts it to human-readable title.

    Examples:
        snake_case --> Snake Case
        PascalCase --> Pascal Case
        CamelCase --> Camel Case
        lower case  --> Lower Case
        UPPER CASE --> Upper Case
        UPPER_CASE --> Upper Case

    Args:
        string: A string to be converted

    Returns:
        A string converted to human-readable title
    """
    # Add space to snake_case names
    string = sub("_", " ", string)

    # Add space to CamelCase names
    string = sub(r"([a-z])([A-Z])", r"\g<1> \g<2>", string)

    # Capitalize first letter in words
    return string.title()
