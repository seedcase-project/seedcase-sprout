import pathlib

from config.settings import PERSISTENT_STORAGE_PATH


def path_database_dir(project_id: int) -> str:
    """Get path to a specific project's database folder.

    If it doesn't exist, it will be created.

    Args:
        project_id: The integer ID for the project.

    Returns:
        str: A string for the path.
    """
    db_folder = pathlib.Path(path_project_storage(project_id), "databases")
    pathlib.Path(db_folder).mkdir(parents=True, exist_ok=True)
    return db_folder


def path_raw_storage(project_id: int) -> str:
    """Get the path to the raw storage folder.

    If it doesn't exist, it will be created.

    Args:
        project_id: The integer ID for the project.

    Returns:
        str: A string for the path.
    """
    raw_folder = pathlib.Path(path_project_storage(project_id), "raw")
    pathlib.Path(raw_folder).mkdir(parents=True, exist_ok=True)
    return raw_folder


def path_project_storage(project_id: int) -> str:
    """Get path to the persistent storage.

    Args:
        project_id: The integer ID for the project.

    Returns:
        str: A string for the path.
    """
    return pathlib.Path(PERSISTENT_STORAGE_PATH, "project", str(project_id))


def path_database_file(project_id: int) -> str:
    """Get path to a specific project's database.

    Args:
        project_id: The integer ID for the project.

    Returns:
        str: A string for the path.
    """
    return pathlib.Path(path_database_dir(project_id), "project_database.db")
