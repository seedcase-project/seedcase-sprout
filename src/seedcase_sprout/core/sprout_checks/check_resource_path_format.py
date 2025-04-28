import seedcase_sprout.core.check_datapackage as cdp
from seedcase_sprout.core.check_datapackage import CheckError
from seedcase_sprout.core.internals._create_relative_resource_data_path import (
    _create_relative_resource_data_path,
)
from seedcase_sprout.core.sprout_checks.get_json_path_to_resource_field import (
    get_json_path_to_resource_field,
)


def check_resource_path_format(
    properties: dict, index: int | None = None
) -> list[CheckError]:
    """Checks if the data path in the resource properties has the correct format.

    As the path is constructed from the resource name, its format can only be checked
    if the resource name is correct. Type, required, and blank errors are not flagged
    here to avoid flagging them twice.

    Args:
        properties: The resource properties to check.
        index: The index of the resource properties. Defaults to None.

    Returns:
        A list of errors. An empty list if no errors were found.
    """
    name = properties.get("name")
    path = properties.get("path")
    expected_path = _create_relative_resource_data_path(name)

    if (
        # Do not check path if name is incorrect
        not cdp.is_resource_name_correct(name)
        # Do not flag type and required errors twice
        or not isinstance(path, str)
        # Do not flag blank errors twice
        or path == ""
        or path == expected_path
    ):
        return []

    return [
        CheckError(
            message=f"Expected the path to be '{expected_path}' but found '{path}'.",
            json_path=get_json_path_to_resource_field("path", index),
            validator="pattern",
        )
    ]
