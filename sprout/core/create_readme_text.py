import json

def create_readme_text(properties: dict) -> str:
    """Create a json object containing the readme text.

    Args:
      properties: An object containing the package and resource properties.

    Returns:
      A string for the README text
    """
    properties = json.loads(properties)
    resources = # Python code to convert the resource details in the dict as
    # a Markdown list. 

    readme_text = (
        f"This is the README file for the package.\n\n"
        f"{properties.name}: {properties.title}\n\n"
        f"Within this data package contains:\n\n"
        f"{properties.resources}"
    )
    return readme_text
