"""Module providing custom validators to be used in forms."""

from django.core.validators import RegexValidator
from django.forms import ValidationError

from app.models import TableMetadata


def validate_no_special_characters(field_name: str, field_value: str) -> None:
    """Validation check for special characters.

    Checks that a field does not include special characters, i.e., characters
    that are not considered numbers or letters.

    Args:
        field_name (str): Name of the field that should be included in the
        error message.
        field_value (str): Field value which will be evaluated with the
        validator.

    Raises:
        ValidationError: If validation fails.

    Returns:
        None: If validation is successful.
    """
    validator = RegexValidator(
        regex=r"^[-a-zA-Z0-9_]+$",
        message=f"Please use only upper or lower case letters (a to z), "
        f"numbers (0 to 9), -, or _ when specifying {field_name}",
        code="invalid_value_special_characters",
    )
    return validator(field_value)


def validate_table_name_does_not_exist(name: str) -> None:
    """Validation check for if table name exists.

    Checks whether a table with the given name does not exist in the database.

    Args:
        name (Str): The name of the table.

    Raises:
        ValidationError: If a table with the name already exists in the db.

    Returns:
        None: If validation is successful.
    """
    if TableMetadata.objects.filter(name=name).exists():
        raise ValidationError(
            message="A table with this name already exists. "
            "Please provide another name.",
            code="invalid_table_name_already_exists",
        )
