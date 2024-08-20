from pathlib import Path
from re import search


def get_ids(path: Path) -> list[int]:
    """Get ids of existing resources or packages in a directory.

    Args:
        path: Directory to search for IDs

    Raises:
        NotADirectoryError: If the path is not a directory

    Returns:
        A list of integers representing the resource ids.
        If no IDs are found, an empty list is returned.
    """
    if not path.is_dir():
        raise NotADirectoryError(f"{path} is not an existing directory")

    # get paths of folders with integers as names
    directories = list(path.glob("[0-9]*/"))

    # extract folder names from directories and convert them to integers
    ids = [int(search(r"([^/]+)/*$", str(dir)).group(0)) for dir in directories]

    return ids
