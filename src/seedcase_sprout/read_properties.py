from pathlib import Path

import seedcase_soil as ss

from seedcase_sprout.check_properties import check_properties
from seedcase_sprout.paths import PackagePath
from seedcase_sprout.properties import SproutProperties


def read_properties(path: Path | None = None) -> SproutProperties:
    """Read in the properties from the `datapackage.json` file.

    Reads the `datapackage.json` file, checks that it is correct, and then
    outputs a `SproutProperties` object.

    Args:
        path: The path to the `datapackage.json` file. Use `PackagePath().properties()`
            to help get the correct path. If no path is provided, this function looks
            for the `datapackage.json` file in the current working directory.

    Returns:
        A `SproutProperties` object with the properties from the
            `datapackage.json` file.

    Examples:
        ```{python}
        import seedcase_sprout as sp

        with sp.ExamplePackage():
            sp.read_properties()
        ```

    Raises:
        ss.errors.FileDoesNotExistError: If the file cannot be found.
        ss.errors.JSONFormatError: If the JSON file is malformatted.
    """
    properties_dict = ss.read_properties(
        ss.parse_source(str(path or PackagePath().properties()))
    )
    properties = SproutProperties.from_dict(properties_dict)
    check_properties(properties)
    return properties
