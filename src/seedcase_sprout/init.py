from jinja2 import Environment, FileSystemLoader

from seedcase_sprout.constants import TEMPLATES_PATH
from seedcase_sprout.internals.to import _to_snake_case
from seedcase_sprout.properties import SproutProperties


def create_properties_text(package_name: str = "") -> str:
    """Create the text for the properties script.

    Args:
        package_name: The name of the package.

    Returns:
        The text that will be saved in the Python script.
    """
    env = Environment(loader=FileSystemLoader(TEMPLATES_PATH), autoescape=True)
    template = env.get_template("package_properties.py.jinja2")
    return template.render(properties=SproutProperties.from_default(name=package_name))


from seedcase_sprout.properties import FieldProperties


def create_resource_properties_text(
    fields: list[FieldProperties],
    resource_name: str = "",
) -> str:
    """Create the text for the resource properties script.

    Args:
        fields: The fields (columns) of the new resource.
        resource_name: The name of the new resource.

    Returns:
        The text that will be saved in the Python script.
    """
    env = Environment(loader=FileSystemLoader(TEMPLATES_PATH), autoescape=True)
    env.filters["to_variable_name"] = _create_resource_properties_script_filename
    template = env.get_template("resource_properties.py.jinja2")
    return template.render(resource_name=resource_name, fields=fields)


def _create_resource_properties_script_filename(resource_name: str = "") -> str:
    """Creates the the resource properties script filename.

    Args:
        resource_name: The name of the resource. Defaults to "".

    Returns:
        The filename.
    """
    return f"resource_properties{resource_name and '_'}{_to_snake_case(resource_name)}"
