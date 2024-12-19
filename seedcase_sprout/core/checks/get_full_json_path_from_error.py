import re

from jsonschema import ValidationError


def get_full_json_path_from_error(error: ValidationError) -> str:
    """Returns a more complete `json_path` to the error, if possible.

    Args:
        error: The error.

    Returns:
        The `json_path`.
    """
    if error.validator == "required":
        match = re.search("'(.*)' is a required property", error.message)
        if match:
            return f"{error.json_path}.{match.group(1)}"
    return error.json_path
