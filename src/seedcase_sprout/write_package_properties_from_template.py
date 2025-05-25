from pathlib import Path

from seedcase_sprout.check_properties import check_properties
from seedcase_sprout.internals import _write_json
from seedcase_sprout.paths import PackagePath
from seedcase_sprout.properties import PackageProperties
from seedcase_sprout.read_properties import read_properties


def write_package_properties_from_template(
    properties: PackageProperties, path: Path | None = None
) -> Path:
    """Write package-level properties to the `datapackage.json` file.

    This function writes the given package properties to the `datapackage.json`
    file. It must be called with properties that do not include any `resources`.
    If the target file already exists, its resource properties will not be updated.

    Args:
        properties: Package properties without resource properties.
        path: The path to the `datapackage.json` file. If no path is provided,
            this function looks for the `datapackage.json` file in the current
            working directory.

    Returns:
        The path to the updated `datapackage.json` file.

    Raises:
        ValueError: If the `resources` field is set on the input properties.
        ExceptionGroup: If there is an error in the properties. A group of
            `CheckError`s, one error for each failed check.
    """
    if properties.resources is not None:
        raise ValueError(
            "The `resources` field must not be set. Use the resource template to define"
            "resource properties."
        )
    path = path or PackagePath().properties()
    check_properties(properties)

    if path.exists():
        properties.resources = read_properties(path).resources

    return _write_json(properties.compact_dict, path)
