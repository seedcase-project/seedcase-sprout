from seedcase_sprout.core.properties import PackageProperties


def create_readme_text(properties: PackageProperties) -> str:
    """Creates a string containing the README text.

    Args:
      properties: An object containing the package and resource properties.

    Returns:
      A string with the README text based on the properties.
    """
    # TODO: Finish this once Properties have been finished.
    # resources = # Python code to convert the resource details in the dict as
    # a Markdown list.

    readme_text = (
        f"# {properties.name}: {properties.title}\n\n"
        f"{properties.description}\n\n"
        f"There are {len(properties.resources or [])} resources in this package."
    )
    return readme_text
