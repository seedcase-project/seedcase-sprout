from pathlib import Path

from seedcase_sprout.check_properties import check_properties
from seedcase_sprout.constants import SCRIPTS_FOLDER
from seedcase_sprout.internals import _write_json
from seedcase_sprout.paths import PackagePath
from seedcase_sprout.properties import PackageProperties
from seedcase_sprout.read_properties import read_properties


def use_package_properties_template(
    properties: PackageProperties, template_path: Path
) -> Path:
    """Write package-level properties from the template to the `datapackage.json` file.

    This function writes the given package properties to the `datapackage.json`
    file. It must be called with properties that do not include any `resources`.
    If the target file already exists, its resource properties will not be updated.

    Args:
        properties: Package properties without resource properties.
        template_path: The path to the template in the scripts folder.

    Returns:
        The path to the updated `datapackage.json` file.

    Raises:
        ValueError: If the `resources` field is set on the input properties.
        ValueError: If the template path is incorrect.
        ExceptionGroup: If there is an error in the properties. A group of
            `CheckError`s, one error for each failed check.
    """
    if properties.resources is not None:
        raise ValueError(
            "The `resources` field must not be set. Use the resource template to define"
            "resource properties."
        )
    check_properties(properties)

    properties_path = PackagePath(_get_package_root(template_path)).properties()
    if properties_path.exists():
        properties.resources = read_properties(properties_path).resources

    return _write_json(properties.compact_dict, properties_path)


def _get_package_root(template_path: Path) -> Path:
    """Get the package root from a template path.

    Args:
        template_path: The template path.

    Returns:
        The path to the package root.

    Raises:
        ValueError: If the template is not a Python file.
        ValueError: If the template is not in the correct folder.
    """
    if not template_path.is_file() or template_path.suffix != ".py":
        raise ValueError(
            f"Expected the template to be a Python file but found {template_path}."
        )
    if template_path.parent.name != SCRIPTS_FOLDER:
        raise ValueError(
            "Expected template file to be at "
            f"`{Path('<package_root>', SCRIPTS_FOLDER, template_path.name)}` but it "
            f"is at {template_path}."
        )
    return template_path.parent.parent
