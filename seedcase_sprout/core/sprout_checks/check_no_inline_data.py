from seedcase_sprout.core.checks.check_error import CheckError
from seedcase_sprout.core.sprout_checks.get_json_path_to_resource_field import (
    get_json_path_to_resource_field,
)


def check_no_inline_data(
    properties: dict, index: int | None = None
) -> list[CheckError]:
    """Checks that the `data` field of a set of resource properties is not set.

    Args:
        properties: The resource properties.
        index: The index of the resource properties. Defaults to None.

    Returns:
        A list of errors. The empty list if no error was found.
    """
    return (
        []
        if properties.get("data") is None
        else [
            CheckError(
                message=(
                    "'data' should not be set. Sprout expects data in separate "
                    "data files specified by 'path'."
                ),
                json_path=get_json_path_to_resource_field("data", index),
                validator="inline-data",
            )
        ]
    )