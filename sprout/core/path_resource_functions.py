from pathlib import Path

from sprout.core import path_package
from sprout.core.path_error_context import (
    verify_is_dir_or_raise_error_with_id_context,
)


def path_resource(package_id: int, resource_id: int) -> Path:
    """Gets the absolute path to a given resource of a given package.

    Args:
        package_id: ID of the package.
        resource_id: ID of the resource.

    Returns:
        A Path to the resource.
    """
    path = path_resources(package_id) / str(resource_id)
    return verify_is_dir_or_raise_error_with_id_context(
        path=path, ids_path=path.parent, context="resource"
    )


def path_resource_data(package_id: int, resource_id: int) -> Path:
    """Gets the absolute path to a given resource's data (i.e., parquet) file.

    Args:
        package_id: ID of the package.
        resource_id: ID of the resource.

    Returns:
        A Path to the resource's data file.
    """
    return path_resource(package_id, resource_id) / "data.parquet"


def path_resource_raw(package_id: int, resource_id: int) -> Path:
    """Gets the absolute path to a given resource's raw folder.

    Args:
        package_id: ID of the package.
        resource_id: ID of the resource.

    Returns:
        A Path to the resource's raw folder.
    """
    return path_resource(package_id, resource_id) / "raw"


def path_resource_raw_files(package_id: int, resource_id: int) -> list[Path]:
    """Gets the absolute path to the raw files of  a resource.

    Args:
        package_id: ID of the package.
        resource_id: ID of the resource.

    Returns:
        A list of Paths to the raw files of the resource.

    Raises:
        NotADirectoryError: If the package_id doesn't exist or the resource_id doesn't
            exist within the package.
    """
    return list(path_resource_raw(package_id, resource_id).iterdir())


def path_resources(package_id: int) -> Path:
    """Gets the absolute path to resources of a given package.

    Args:
        package_id: ID of the package to get the resource path from."

    Returns:
        A Path to the resources within the package.
    """
    path = path_package(package_id) / "resources"
    return verify_is_dir_or_raise_error_with_id_context(
        path=path, ids_path=path, context="resource"
    )
