from pathlib import Path

import seedcase_soil as so

from seedcase_sprout.check_properties import check_properties
from seedcase_sprout.properties import (
    SproutProperties,
)


def write_properties(properties: SproutProperties, path: Path) -> Path:
    """Write the `properties` to the `datapackage.json` file.

    If the `datapackage.json` file already exists, it will be overwritten. If
    not, a new file will be created.

    Args:
        properties: The properties to write. Use the CLI command
            `init-metadata` to create a file with your properties object.
        path: A `Path` to the `datapackage.json` file.

    Returns:
        The path to the updated `datapackage.json` file.

    Raises:
        ExceptionGroup: If there is an error in the properties. A group of
            `CheckError`s, one error for each failed check.
    """
    check_properties(properties)

    return so.write_properties(properties.compact_dict, path)
