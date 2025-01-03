from pathlib import Path


def check_is_dir(path: Path) -> Path:
    """Verifies whether the directory given by the path exists or not.

    Args:
        path: The path to verify

    Returns:
        The path if it is a directory.

    Raises:
        NotADirectoryError: If path either doesn't exist or isn't a directory.
    """
    if not path.is_dir():
        raise NotADirectoryError(f"{path} either isn't a directory or doesn't exist.")

    return path
