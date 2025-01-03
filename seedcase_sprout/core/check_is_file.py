from pathlib import Path


def check_is_file(path: Path) -> Path:
    """Verifies whether the file given by the path exists or not.

    Args:
        path: The path to verify.

    Returns:
        A Path object if it is a file.

    Raises:
        FileNotFound: If the file in the path doesn't exist or isn't a file.
    """
    if not path.is_file():
        raise FileNotFoundError(f"{path} is not a file.")

    return path
