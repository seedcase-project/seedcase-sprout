from pathlib import Path

from sprout.core.create_resource_structure import create_resource_structure


def create_test_package_structure(root_path: Path, package_id: int) -> Path:
    """Creates a package file structure (with empty files) for path function tests.

    Args:
        root_path: Root path to create the package structure.
        package_id: ID of the package to create.

    Returns:
        Path of package.
    """
    # TODO: Use `create_package_structure()` function here when it's implemented.
    path_package = root_path / "packages" / str(package_id)
    path_package.mkdir(parents=True)
    (path_package / "datapackage.json").touch()
    (path_package / "database.sql").touch()

    return path_package


def create_test_resource_structure(
    path_package: Path, raw_files: str | list[str]
) -> list[Path]:
    """Creates a resource file structure (with empty files) for path function tests.

    Args:
        path_package: Path to package.$
        resource_id: ID of the resource to create.
        raw_files: Name(s) of raw file(s).

    Returns:
        List with two Paths: one to the resource, one to it's raw directory.
    """
    path_resources = path_package / "resources"
    if not (path_resources).exists():
        path_resources.mkdir(parents=True)

    path_list_resource = create_resource_structure(path_resources)
    (path_list_resource[0] / "data.parquet").touch()
    for raw_file in raw_files:
        (path_list_resource[1] / raw_file).touch()

    return path_list_resource
