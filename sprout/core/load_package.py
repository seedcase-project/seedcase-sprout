from pathlib import Path

from frictionless import Package


def load_package(project_path: Path) -> "Package":
    """Load a frictionless.Package object from a datapackage.json metadata file.

    Args:
        project_path: path to the project folder

    Returns:
        Package: data package object for the project
    """
    datapackage_path = project_path / Path("datapackage.json")
    return Package(datapackage_path)
