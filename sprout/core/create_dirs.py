from pathlib import Path


def create_dir(path: Path) -> Path:
    """Creates a directory from a path.

    The path has already been verified as not existing.

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


def create_dirs(path: list[Path]) -> list[Path]:
    """Creates directories from a list of paths using the function create_dir.

    Args:
        path: A list of paths pointing to where directories should be created.

    Raises:
        NoDirectoryError: If the directory wasn't created

    Returns:
        A list of paths to the newly created directories
    """
    return [create_dir(p) for p in path]
