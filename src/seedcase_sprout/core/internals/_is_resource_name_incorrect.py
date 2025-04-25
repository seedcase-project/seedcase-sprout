from typing import Any

import seedcase_sprout.core.check_datapackage as cdp


def _is_resource_name_incorrect(resource_name: Any) -> bool:
    """Checks if the given resource name is incorrect.

    Args:
        resource_name: The resource name to check.

    Returns:
        Whether the resource name is incorrect.
    """
    return any(
        error
        for error in cdp.check_resource_properties({"name": resource_name})
        if error.json_path == "$.name"
    )
