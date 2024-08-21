import re
from pathlib import Path


def get_ids(path: Path) -> list[int]:
    """Get ids of existing resources or packages in a directory.

    Args:
        path: Directory to search for IDs.

    Returns:
        A list of integers representing the ids of the subdirectories.
        If no IDs are found, an empty list is returned.
    """
    # Keep only directories
    directories = list(path.glob("*/"))
    ids = list(map(get_number, directories))
    # Drop any empty items
    ids = list(filter(None, ids))

    return ids


def get_number(path: Path) -> int | None:
    """Get only the number from directory.

    Args:
      path: Directory to extract the number from.
    
    Returns:
    	A single integer.
    """
    directory_name = path.name
    if re.match(r"^\d+$", directory_name):
        return int(directory_name)
