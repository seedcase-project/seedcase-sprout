from pathlib import Path


def create_dir(path: Path) -> Path:
    """Creates a directory from a path.

    The path has already been verified as not existing.

    Args:
        path: The path pointing to the new directory to create

    Raises:
        NotADirectoryError: If the directory wasn't created

    Returns:
        path to the newly created directory.
    """
    try:
        path.mkdir(parents=True, exist_ok=False)
    except FileExistsError:
        raise NotADirectoryError(f"Failed to create directory: {path}")
    return path


def create_dirs(paths: list[Path]) -> list[Path]:
    """Creates directories from a list of paths using the function create_dir.

    Args:
        paths: A list of paths pointing to where directories should be created.

    Raises:
        NotADirectoryError: If any of the directories fail to be created throw
        an error and remove any directories already created.

    Returns:
        A list of paths to the newly created directories.
    """
    created_dirs = []
    for path in paths:
        try:
            created_dirs.append(create_dir(path))
        except NotADirectoryError:
            # Clean up already created directories
            for dir_path in created_dirs:
                dir_path.rmdir()
            raise
    return created_dirs
