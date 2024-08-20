from pathlib import Path


def create_resource_raw_dir(path: Path) -> Path:
    """Create raw directory for a resource.

    Args:
        path: Directory to create the new resource directory in.

    Returns:
        Directory for the new resource.
    """
    resource_raw_dir = path / "raw"
    resource_raw_dir.mkdir()

    return resource_raw_dir
