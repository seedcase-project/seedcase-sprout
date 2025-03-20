from pathlib import Path

from seedcase_sprout.core.check_is_file import check_is_file
from seedcase_sprout.core.properties import PackageProperties
from seedcase_sprout.core.read_json import read_json
from seedcase_sprout.core.sprout_checks.check_package_properties import (
    check_package_properties,
)
from seedcase_sprout.core.sprout_checks.check_properties import check_properties


def read_properties(path: Path) -> PackageProperties:
    """Read in the properties from the `datapackage.json` file.

    Reads the `datapackage.json` file, checks that is correct, and then
    outputs a `PackageProperties` object.

    Args:
        path: The path to the `datapackage.json` file. Use `path_properties()`
            to help get the correct path.

    Returns:
        Outputs a `PackageProperties` object with the properties from the
            `datapackage.json` file.

    Examples:
        ```{python}
        import tempfile
        from pathlib import Path

        import seedcase_sprout.core as sp

        # Create a temporary directory for the example
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_path = Path(temp_dir)

            properties_path = Path(temp_path / "datapackage.json")
            # Create a package structure first
            sp.write_package_properties(
                properties=sp.example_package_properties(),
                path=properties_path
            )

            # Edit package properties
            sp.read_properties(properties_path)
        ```

    Raises:
        FileNotFound: If the `datapackage.json` file doesn't exist.
        JSONDecodeError: If the `datapackage.json` file couldn't be read.
    """
    check_is_file(path)
    properties = read_json(path)
    if properties.get("resources"):
        check_properties(properties)
    else:
        check_package_properties(properties)
    return PackageProperties.from_dict(properties)
