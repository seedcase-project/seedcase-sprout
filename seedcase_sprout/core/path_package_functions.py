from pathlib import Path

from seedcase_sprout.core.check_is_dir import check_is_dir
from seedcase_sprout.core.check_is_file import check_is_file
from seedcase_sprout.core.check_is_package_dir import check_is_package_dir
from seedcase_sprout.core.create_dirs import create_dir
from seedcase_sprout.core.path_sprout_root import path_sprout_root


def path_package(package_id: int) -> Path:
    """Gets the absolute path to the specific package folder.

    Args:
        package_id: The ID of the package to get the folder path for.

    Returns:
        The absolute path to the package folder.
    """
    path = path_packages() / str(package_id)
    return check_is_package_dir(path)


def path_package_database(package_id: int) -> Path:
    """Gets the absolute path to a given package's SQL database.

    Args:
        package_id: ID of the package.

    Returns:
        A Path to the package's database.
    """
    path = path_package(package_id) / "database.sql"
    return check_is_file(path)


def path_package_properties(package_id: int) -> Path:
    """Gets the absolute path to a given package's properties file.

    Args:
        package_id: ID of the package.

    Returns:
        A Path to the properties file.
    """
    path = path_package(package_id) / "datapackage.json"
    return check_is_file(path)


def path_packages() -> Path:
    """Gets the absolute path to the packages folder.

    Returns:
        A Path to the packages folder.

    Raises:
        NotADirectoryError: If the packages folder doesn't exist.
    """
    path = path_sprout_root() / "packages"
    return create_dir(path) if not path.exists() else check_is_dir(path)
