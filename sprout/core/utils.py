from pathlib import Path
from re import sub

from config.settings import PERSISTENT_STORAGE_PATH

DATAPACKAGE_FILE_NAME = "datapackage.json"

def count_rows(path: str) -> int:
    with open(path) as file:
        return sum(1 for _ in file)

def get_project_path(project_name: str) -> "Path":
    return Path(PERSISTENT_STORAGE_PATH, "projects", project_name)

def get_datapackage_path(project_name: str) -> "Path":
    return Path(get_project_path(project_name), DATAPACKAGE_FILE_NAME)

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

def optional_bool_to_bool(optional_bool: bool | None, default: bool) -> bool:
    return default if optional_bool is None else optional_bool
