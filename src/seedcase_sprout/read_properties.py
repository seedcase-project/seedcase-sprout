from pathlib import Path

import seedcase_soil as so

from seedcase_sprout.check_properties import check_properties
from seedcase_sprout.properties import SproutProperties


def read_properties(path: Path) -> SproutProperties:
    """Read in the properties from the `datapackage.json` file.

    Reads the `datapackage.json` file, checks that it is correct, and then
    outputs a `SproutProperties` object.

    Args:
        path: The path to the `datapackage.json` file.

    Returns:
        A `SproutProperties` object with the properties from the
            `datapackage.json` file.

    Raises:
        so.errors.FileDoesNotExistError: If the file cannot be found.
        so.errors.JSONFormatError: If the JSON file is malformatted.
    """
    properties_dict = so.read_properties(so.parse_source(str(path)))
    properties = SproutProperties.from_dict(properties_dict)
    check_properties(properties)
    return properties
