from seedcase_sprout.core.checks.check_error import CheckError
from seedcase_sprout.core.checks.required_fields import RequiredFieldType
from seedcase_sprout.core.sprout_checks.get_blank_value_for_type import (
    get_blank_value_for_type,
)


def check_list_item_field_not_blank(
    properties: dict, list_name: str, field_name: str, field_type=RequiredFieldType.str
) -> list[CheckError]:
    """Checks that the specified field of items in a list is not blank.

    Args:
        properties: The properties object containing the list.
        list_name: The name of the list field.
        field_name: The name of the item field.
        field_type: The type of the item field. Defaults to str.

    Returns:
        A list of errors. An empty list if no errors were found.
    """
    return [
        CheckError(
            message=f"'{field_name}' should not be blank",
            json_path=f"$.{list_name}[{index}].{field_name}",
            validator="blank",
        )
        for index, item in enumerate(properties.get(list_name, []))
        if item.get(field_name) == get_blank_value_for_type(field_type)
    ]
