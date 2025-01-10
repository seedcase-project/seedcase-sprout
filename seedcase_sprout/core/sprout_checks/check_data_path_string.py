from seedcase_sprout.core.checks.check_error import CheckError
from seedcase_sprout.core.sprout_checks.get_json_path_to_resource_field import (
    get_json_path_to_resource_field,
)


def check_data_path_string(
    properties: dict, index: int | None = None
) -> list[CheckError]:
    """Checks that the `path` field of a set of resource properties is of type string.

    Args:
        properties: The resource properties.
        index: The index of the resource properties. Defaults to None.

    Returns:
        A list of errors. An empty list if no error was found.
    """
    path = properties.get("path", "")
    return (
        []
        if type(path) is str
        else [
            CheckError(
                message=f"{path} is not of type 'string'",
                json_path=get_json_path_to_resource_field("path", index),
                validator="type",
            )
        ]
    )
