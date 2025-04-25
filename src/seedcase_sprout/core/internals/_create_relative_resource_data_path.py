from pathlib import Path
from typing import Any

from seedcase_sprout.core.internals._is_resource_name_incorrect import (
    _is_resource_name_incorrect,
)


def _create_relative_resource_data_path(resource_name: Any) -> str | None:
    """Creates a stringified relative path to the resource data file based on the name.

    The path is created only if the resource name is correct.

    Args:
        resource_name: The name of the resource.

    Returns:
        The relative path from the package root to the resource data file.
            E.g., "resources/test-resource/data.parquet"
    """
    return (
        None
        if _is_resource_name_incorrect(resource_name)
        else str(Path("resources", resource_name, "data.parquet"))
    )
