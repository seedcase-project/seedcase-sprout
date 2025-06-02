from pathlib import Path

from jinja2 import Environment, FileSystemLoader

from seedcase_sprout.constants import TEMPLATES_PATH
from seedcase_sprout.internals.create import _in_snake_case
from seedcase_sprout.paths import PackagePath
from seedcase_sprout.properties import FieldProperties
from seedcase_sprout.sprout_checks.is_resource_name_correct import (
    _is_resource_name_correct,
)
from seedcase_sprout.write_file import write_file


def create_resource_properties_template(
    resource_name: str | None = None,
    fields: list[FieldProperties] | None = None,
    path: Path | None = None,
) -> Path:
    """Creates the resource properties template.

    The resource name and the fields' name and type information can be included.

    Args:
        resource_name: The name of the new resource. Defaults to None.
        fields: The fields (columns) of the new resource. Defaults to None.
        path: The path to the package folder. Defaults to the current working directory.

    Returns:
        The path to the template file.

    Raises:
        ValueError: If the resource name is not correct.

    Examples:
        ```{python}
        import seedcase_sprout as sp

        sp.create_resource_properties_template("my-resource")
        ```
    """
    if resource_name and not _is_resource_name_correct(resource_name):
        raise ValueError(
            f"The resource name '{resource_name}' is not correct. Resource names"
            " should only include alphanumeric characters and `.-_`."
        )
    resource_name = resource_name or ""

    env = Environment(loader=FileSystemLoader(TEMPLATES_PATH), autoescape=True)
    env.filters["_in_snake_case"] = _in_snake_case
    template = env.get_template("resource_properties.py.jinja2")
    text = template.render(resource_name=resource_name, fields=fields)

    template_path = PackagePath(path).resource_properties_template(resource_name)
    template_path.parent.mkdir(exist_ok=True)
    return write_file(text, template_path)
