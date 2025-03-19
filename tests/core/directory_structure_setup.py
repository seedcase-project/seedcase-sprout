from pathlib import Path

from seedcase_sprout.core import (
    create_resource_structure,
    example_package_properties,
    write_package_properties,
)


def create_test_data_package(tmp_path: Path) -> Path:
    """Creates a package file structure (with empty files) for path function tests.

    Args:
        tmp_path: Path to a temporary folder.

    Returns:
        Path of package.
    """
    tmp_path.mkdir(parents=True, exist_ok=True)
    write_package_properties(
        properties=example_package_properties(), path=tmp_path / "datapackage.json"
    )

    (tmp_path / "README.md").touch()

    return tmp_path


def create_test_global_data_package(global_path: Path, package_id: int) -> Path:
    """Creates a package file structure (with empty files) for path function tests.

    Args:
        global_path: Global path to create the package structure.
        package_id: ID of the package to create.

    Returns:
        Path of package.
    """
    # TODO: Use `write_package_properties()` function here when has been implemented.
    path_package = global_path / "packages" / str(package_id)
    path_package.mkdir(parents=True, exist_ok=True)
    (path_package / "datapackage.json").touch()
    (path_package / "README.md").touch()

    return path_package


def create_test_resource_structure(
    path_package: Path, batch_files: str | list[str]
) -> list[Path]:
    """Creates a resource file structure (with empty files) for path function tests.

    Args:
        path_package: Path to package.
        batch_files: Name(s) of batch file(s).

    Returns:
        List with two Paths: one to the resource, one to its batch directory.
    """
    path_resources = path_package / "resources"
    path_resources.mkdir(parents=True, exist_ok=True)

    path_list_resource = create_resource_structure(path_resources)
    (path_list_resource[0] / "data.parquet").touch()
    for batch_file in batch_files:
        (path_list_resource[1] / batch_file).touch()

    return path_list_resource
