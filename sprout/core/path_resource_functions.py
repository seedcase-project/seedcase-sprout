from pathlib import Path

from sprout.core.get_ids import get_ids
from sprout.core.path_helper_functions import (
    verify_is_dir_or_raise_error_with_id_context,
    verify_is_file_or_raise_error_with_id_context,
)
from sprout.core.path_sprout_root import path_sprout_root
from sprout.core.verify_is_dir import verify_is_dir


def path_resource(package_id: int, resource_id: int) -> Path:
    """Gets the absolute path to a given resource of a given package.

    Args:
        package_id: ID of the package.
        resource_id: ID of the resource.

    Returns:
        A Path to the resource.
    """
    path = (
        path_sprout_root()
        / "packages"
        / str(package_id)
        / "resources"
        / str(resource_id)
    )
    return verify_is_dir_or_raise_error_with_id_context(path=path, ids_path=path.parent)


def path_resource_data(package_id: int, resource_id: int) -> Path:
    """Gets the absolute path to a given resource's data (i.e., parquet) file.

    Args:
        package_id: ID of the package.
        resource_id: ID of the resource.

    Returns:
        A Path to the resource's data file.
    """
    path = (
        path_sprout_root()
        / "packages"
        / str(package_id)
        / "resources"
        / str(resource_id)
        / "data.parquet"
    )
    return verify_is_file_or_raise_error_with_id_context(
        path=path, ids_path=path.parent.parent
    )


def path_resource_raw(package_id: int, resource_id: int) -> Path:
    """Gets the absolute path to a given resource's raw folder.

    Args:
        package_id: ID of the package.
        resource_id: ID of the resource.

    Returns:
        A Path to the resource's raw folder.
    """
    path = (
        path_sprout_root()
        / "packages"
        / str(package_id)
        / "resources"
        / str(resource_id)
        / "raw"
    )
    return verify_is_dir_or_raise_error_with_id_context(
        path=path, ids_path=path.parent.parent
    )


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
    path = (
        path_sprout_root()
        / "packages"
        / str(package_id)
        / "resources"
        / str(resource_id)
        / "raw"
    )

    try:
        verify_is_dir(path)
        return [file for file in path.iterdir()]
    except NotADirectoryError as e:
        raise NotADirectoryError(
            f"Existing ID's are {get_ids(path.parent.parent)}"
        ) from e


def path_resources(package_id: int) -> Path:
    """Gets the absolute path to resources of a given package.

    Args:
        package_id: ID of the package to get the resource path from."

    Returns:
        A Path to the resources within the package.
    """
    path = path_sprout_root() / "packages" / str(package_id) / "resources"
    return verify_is_dir_or_raise_error_with_id_context(path, path.parent.parent)
