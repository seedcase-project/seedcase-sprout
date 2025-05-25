import json
from pathlib import Path

from jinja2 import Environment, FileSystemLoader

from seedcase_sprout.constants import TEMPLATES_PATH
from seedcase_sprout.paths import PackagePath
from seedcase_sprout.properties import PackageProperties
from seedcase_sprout.read_properties import read_properties
from seedcase_sprout.write_file import write_file


def sync_package_properties_template(path: Path | None = None):
    """Syncs the package properties template with the package properties.

    Args:
        path: The path to the package folder. Defaults to the current working directory.

    Examples:
        ```{python}
        import seedcase_sprout as sp

        sp.sync_package_properties_template()
        ```
    """
    package_path = PackagePath(path)
    properties_path = package_path.properties()
    package_properties = (
        read_properties(properties_path)
        if properties_path.exists()
        else PackageProperties.from_default()
    )

    env = Environment(loader=FileSystemLoader(TEMPLATES_PATH), autoescape=False)
    env.filters["quote_str"] = lambda value: json.dumps(value, ensure_ascii=False)

    template = env.get_template("package-properties.jinja2")
    text = template.render(properties=package_properties)

    template_path = package_path.package_properties_template()
    template_path.parent.mkdir(exist_ok=True)
    write_file(text, template_path)
