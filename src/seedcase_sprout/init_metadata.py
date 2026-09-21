from jinja2 import Environment, FileSystemLoader

from seedcase_sprout.constants import TEMPLATES_PATH
from seedcase_sprout.internals.to import _to_snake_case
from seedcase_sprout.properties import FieldProperties, SproutProperties


def init_package_metadata(name: str = "") -> str:
    """Create the text for the properties script.

    Args:
        name: The name of the package.

    Returns:
        The text that will be saved in the Python script.
    """
    env = Environment(loader=FileSystemLoader(TEMPLATES_PATH), autoescape=True)
    template = env.get_template("package_properties.py.jinja2")
    return template.render(properties=SproutProperties.from_default(name=name))


def init_resource_metadata(
    metadata: list[FieldProperties],
    name: str = "",
) -> str:
    """Create the text for the resource properties script.

    Args:
        metadata: The metadata for the columns ("fields") of the new resource.
        name: The name of the new resource.

    Returns:
        The text that will be saved in the Python script.
    """
    env = Environment(loader=FileSystemLoader(TEMPLATES_PATH), autoescape=True)
    env.filters["to_variable_name"] = _create_filename
    template = env.get_template("resource_properties.py.jinja2")
    return template.render(resource_name=name, fields=metadata)


def _create_filename(resource_name: str = "") -> str:
    """Creates the the resource properties script filename.

    Args:
        resource_name: The name of the resource. Defaults to "".

    Returns:
        The filename.
    """
    return f"resource_properties{resource_name and '_'}{_to_snake_case(resource_name)}"
