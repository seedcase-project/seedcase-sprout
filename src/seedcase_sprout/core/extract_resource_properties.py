from pathlib import Path

from seedcase_sprout.core.check_is_file import check_is_file
from seedcase_sprout.core.check_is_supported_format import check_is_supported_format
from seedcase_sprout.core.checks import check_resource_properties
from seedcase_sprout.core.extract_properties_from_file import (
    extract_properties_from_file,
)
from seedcase_sprout.core.properties import ResourceProperties


def extract_resource_properties(data_path: Path) -> ResourceProperties:
    """Extracts resource properties from a raw data file.

    This function takes the data file found at the `data_path` location and
    extracts properties from the file into a `ResourceProperties` object. This
    function is often followed by `edit_resource_properties()` to fill in any
    remaining missing fields, like the `path` property field.  Usually, you use
    either this function or the `create_resource_properties()` function to
    create the initial resource properties for a specific (new) data resource.

    Args:
        data_path: The path to a raw data file of a supported format.

    Returns:
        Outputs a `ResourceProperties` object. Use `write_resource_properties()`
            to save the object to the `datapackage.json` file.
    """
    check_is_file(data_path)
    check_is_supported_format(data_path)

    properties = extract_properties_from_file(data_path)
    check_resource_properties(properties)
    return ResourceProperties.from_dict(properties)
