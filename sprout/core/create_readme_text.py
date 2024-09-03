import json


def create_readme_text(json_object: json) -> str:
    """Create a json object containing the readme text.

    Args:
      json_object: A JSON object containing the package properties template

    Returns:
      A string with the README text
    """
    readme_text = (
        f"This is the README file for the package.\n\n"
        f"{json.dumps(json_object, indent=4)}"
    )
    return readme_text
