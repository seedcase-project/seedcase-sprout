from pathlib import Path

from sprout.core.path_error_context import (
    verify_is_dir_or_raise_error_with_id_context,
    verify_is_file_or_raise_error_with_id_context,
)
from sprout.core.path_sprout_root import path_sprout_root
from sprout.core.verify_is_dir import verify_is_dir


def path_package(package_id: int) -> Path:
    """Gets the absolute path to the specific package folder.

    Args:
        package_id: The ID of the package to get the folder path for.

    Returns:
        The absolute path to the package folder.
    """
    path = path_sprout_root() / "packages" / str(package_id)
    return verify_is_dir_or_raise_error_with_id_context(path=path, ids_path=path.parent)


def path_package_database(package_id: int) -> Path:
    """Gets the absolute path to a given package's SQL database.

    Args:
        package_id: ID of the package.

    Returns:
        A Path to the package's database.
    """
    path = path_sprout_root() / "packages" / str(package_id) / "database.sql"
    return verify_is_file_or_raise_error_with_id_context(
        path=path, ids_path=path.parent.parent
    )


def path_package_properties(package_id: int) -> Path:
    """Gets the absolute path to a given package's properties file.

    Args:
        package_id: ID of the package.

    Returns:
        A Path to the properties file.
    """
    path = path_sprout_root() / "packages" / str(package_id) / "datapackage.json"
    return verify_is_file_or_raise_error_with_id_context(
        path=path, ids_path=path.parent.parent
    )


def path_packages() -> Path:
    """Gets the absolute path to the packages folder.

    Returns:
        A Path to the packages folder.

    Raises:
        NotADirectoryError: If the packages folder doesn't exist.
    """
    return verify_is_dir(path_sprout_root() / "packages")
