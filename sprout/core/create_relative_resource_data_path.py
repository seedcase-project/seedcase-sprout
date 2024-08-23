from pathlib import Path
from re import split


def create_relative_resource_data_path(path: Path) -> Path:
    """Create a relative path to the resource data file.

    Args:
        path: Absolute path to the folder of a specific resource

    Returns:
        Relative path from the package root to the resource data file
        E.g., "resources/1/data.parquet"
    """
    relative_resource_path = split(r"packages/[0-9]*/", str(path))[1]

    return Path(relative_resource_path) / "data.parquet"
