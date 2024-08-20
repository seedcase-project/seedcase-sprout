from pathlib import Path


def create_dirs(path: list[Path]) -> list[Path]:
    """Creates directories from a list of directories.

    Args:
        path: The path pointing to the new directory to create
    Raises:
        NoDirectoryError: If the directory wasn't created
    Returns:
        path to the newly created directory.
    """
    return [create_dir(p) for p in path]


def create_dir(path: Path) -> Path:
    """Creates a directory from a path.

    Args:
        path: The path pointing to the new directory to create
    Raises:
        NoDirectoryError: If the directory wasn't created
    Returns:
        path to the newly created directory.
    """
    if path.is_dir():
        return path
    else:
        path.mkdir(parents=True, exist_ok=False)
        return path
