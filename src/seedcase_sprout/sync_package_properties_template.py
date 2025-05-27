import json
from pathlib import Path

from jinja2 import Environment, FileSystemLoader, select_autoescape

from seedcase_sprout.constants import TEMPLATES_PATH
from seedcase_sprout.internals.functionals import _map
from seedcase_sprout.paths import PackagePath
from seedcase_sprout.properties import PackageProperties
from seedcase_sprout.read_properties import read_properties
from seedcase_sprout.write_file import write_file


def sync_package_properties_template(path: Path | None = None) -> Path:
    """Syncs the package properties template with the package properties.

    Args:
        path: The path to the package folder. Defaults to the current working directory.

    Returns:
        The path to the template file.

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

    env = Environment(
        loader=FileSystemLoader(TEMPLATES_PATH),
        autoescape=select_autoescape(disabled_extensions=("py.jinja2")),
    )
    env.filters["quote_str"] = lambda value: json.dumps(value, ensure_ascii=False)
    env.filters["comment"] = _comment
    env.filters["strip_n"] = lambda text: text.lstrip("\n").rstrip("    ")

    template = env.get_template("package-properties.py.jinja2")
    text = template.render(properties=package_properties)

    template_path = package_path.package_properties_template()
    template_path.parent.mkdir(exist_ok=True)
    return write_file(text, template_path)


def _comment(text: str) -> str:
    """Comments out each line in a block of text."""

    def _comment_line(line: str) -> str:
        content = line.lstrip()
        # Don't change empty lines
        if content == "":
            return line

        # Indentation to keep after `#`: one indent smaller than original
        keep_spaces = line[4 : -len(content)]

        # Uncomment any commented lines
        if content.startswith("# "):
            content = content[2:]

        # Place one indent before `#`
        return f"    #{keep_spaces}{content}"

    return "\n".join(_map(text.splitlines(), _comment_line))
