from pathlib import Path


def verify_is_directory(path: str):
    """Verifies if the path is an existing directory.

    Args:
        path: The path to verify

    Raises:
        NotADirectoryError: If the path is not an existing directory

    Returns:
        path if it's a directory
    """
    path = Path(path)

    if not path.is_dir():
        raise NotADirectoryError(f"{path} is not an existing directory")

    return path
