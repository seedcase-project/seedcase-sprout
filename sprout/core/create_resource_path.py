from pathlib import Path


def create_resource_path(path: Path, id: int) -> Path:
    """Create a path for a new resource.

    Args:
        path: Path to the resources folder within the package
        id: ID of the resource

    Returns:
        A path to the resource folder.
    """
    return path / f"{id}"
