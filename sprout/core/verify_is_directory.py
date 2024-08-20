from pathlib import Path


def verify_is_directory(path: Path) -> Path:
    """Verifies if the path is an existing directory.

    Args:
        path: The path to verify

    Raises:
        NotADirectoryError: When the directory in the path doesn't exist.

    Returns:
        A Path object if it is a directory.
    """
    if not path.is_dir():
        raise NotADirectoryError(f"The {path} directory doesn't exist.")

    return path
