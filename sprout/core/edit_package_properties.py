from pathlib import Path

from frictionless.errors import PackageError

from sprout.core.read_json import read_json
from sprout.core.verify_is_file import verify_is_file
from sprout.core.verify_package_properties import (
    verify_package_properties,
)
from sprout.core.verify_properties_are_well_formed import (
    verify_properties_are_well_formed,
)


def edit_package_properties(path: Path, properties: dict) -> dict:
    """Edits the properties of an existing package.

    Values in `properties` overwrite preexisting values on the package.

    Args:
        path: The path to the `datapackage.json` file.
        properties: The new package properties.

    Returns:
        The updated package properties.

    Raises:
        FileNotFound: If the `datapackage.json` file doesn't exist.
        NotPropertiesError: If the new package properties are not correct or the current
            package properties are not well-formed.
        JSONDecodeError: If the `datapackage.json` file couldn't be read.
    """
    verify_is_file(path)
    verify_package_properties(properties)

    current_properties = read_json(path)
    verify_properties_are_well_formed(current_properties, PackageError.type)

    current_properties.update(properties)
    return current_properties
