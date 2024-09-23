from pathlib import Path


def create_test_package_structure(root_path: Path, package_id: int):
    """Creates a package file structure (with empty files) for path function tests.

    Args:
        root_path: Root path to create the package structure.
        package_id: ID of the package to create.

    Returns:
        Path of package.
    """
    path_package = root_path / "packages" / str(package_id)
    path_package.mkdir(parents=True)
    (path_package / "datapackage.json").touch()
    (path_package / "database.sql").touch()
    return path_package


def create_test_resource_structure(
    package_path: Path, resource_id: int, raw_files: list[str]
):
    """Creates a resource file structure (with empty files) for path function tests.

    Args:
        package_path: Path to package.
        resource_id: ID of the resource to create.
        raw_files: Name(s) of raw file(s).

    Returns:
        _description_.
    """
    path_resource = package_path / "resources" / str(resource_id)
    (path_resource / "raw").mkdir(parents=True)
    (path_resource / "data.parquet").touch()
    for raw_file in raw_files:
        (path_resource / "raw" / raw_file).touch()
    return path_resource
