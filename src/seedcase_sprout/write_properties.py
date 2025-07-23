from pathlib import Path

from seedcase_sprout.check_properties import check_properties
from seedcase_sprout.internals import _to_dedented, _write_json
from seedcase_sprout.paths import PackagePath
from seedcase_sprout.properties import (
    FieldProperties,
    PackageProperties,
    ResourceProperties,
)


def write_properties(properties: PackageProperties, path: Path | None = None) -> Path:
    """Write the `properties` to the `datapackage.json` file.

    If the `datapackage.json` file already exists, it will be overwritten. If not,
    a new file will be created.

    Args:
        properties: The properties to write. Use `create_properties_script()` to
            create a file with your properties object.
        path: A `Path` to the `datapackage.json` file.

    Returns:
        The path to the updated `datapackage.json` file.

    Raises:
        ExceptionGroup: If there is an error in the properties. A group of
            `CheckError`s, one error for each failed check.
    """
    path = path or PackagePath().properties()
    if properties.description:
        properties.description = _to_dedented(properties.description)

    resources = getattr(properties, "resources", None)
    if resources:
        for resource in resources:
            _dedent_if_present(resource, "description")

            schema = getattr(resource, "schema", None)
            if schema and schema.fields:
                for field in schema.fields:
                    _dedent_if_present(field, "description")

    check_properties(properties)
    return _write_json(properties.compact_dict, path)


def _dedent_if_present(
    properties: ResourceProperties | FieldProperties, field: str
) -> None:
    val = getattr(properties, field, None)
    if val:
        setattr(properties, field, _to_dedented(val))
