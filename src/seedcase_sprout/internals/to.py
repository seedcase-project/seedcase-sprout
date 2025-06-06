def _to_snake_case(name: str) -> str:
    """Creates a snake-case version of a package or resource name.

    Args:
        name: The package or resource name.

    Returns:
        The package or resource name in snake case.

    """
    return name.replace(".", "_").replace("-", "_")
