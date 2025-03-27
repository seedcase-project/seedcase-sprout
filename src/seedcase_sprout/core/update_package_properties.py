from seedcase_sprout.core.checks.check_error_matcher import CheckErrorMatcher
from seedcase_sprout.core.properties import PackageProperties
from seedcase_sprout.core.sprout_checks.check_package_properties import (
    check_package_properties,
)
from seedcase_sprout.core.sprout_checks.check_properties import check_properties


def update_package_properties(
    current: PackageProperties, updates: PackageProperties
) -> PackageProperties:
    """Updates the properties of an existing package.

    Use this any time you want to update the package's properties.  When you need
    to update the `datapackage.json` file, use this function to ensure the
    properties are correctly structured before they're written. It only updates the
    properties of the package itself, not of the data resources contained within
    the package.

    If the properties in the `updates` argument are correct (i.e., they pass the properties checks), they will overwrite any
    pre-existing properties within the `current` properties.

    Args:
        current: The current properties found in the `datapackage.json` file. Use
            `read_properties()` to get the current properties.
        updates: The new package properties to update from the original. Use
            `PackageProperties` to provide a correctly structured properties
            dictionary. See `help(PackageProperties)` for details on how to use it.

    Returns:
        The updated package properties as a `PackageProperties` object. Use
            `write_package_properties()` to save it back to the `datapackage.json`
            file.

    Raises:
        ExceptionGroup: If there is an error in the current, incoming, or resulting
            package properties. A group of `CheckError`s, one error for each failed
            check.

    Examples:
        ```{python}
        #| eval: false
        # TODO: This needs to be updated to match using `create_package_properties()`.
        import tempfile
        from pathlib import Path

        import seedcase_sprout.core as sp

        # Create a temporary directory for the example
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_path = Path(temp_dir)

            # Create a package structure first
            sp.create_package_properties(
                properties=sp.example_package_properties(),
                path=temp_path
            )

            # Edit package properties
            sp.update_package_properties(
                current=sp.read_properties(temp_path / "1" / "datapackage.json"),
                updates=sp.PackageProperties(
                    title="New Package Title",
                    name="new-package-name",
                    description="New Description",
                )
            )
        ```
    """
    updates.resources = None
    check_package_properties(updates, ignore=[CheckErrorMatcher(validator="required")])

    check_properties(
        current,
        ignore=[CheckErrorMatcher(validator="required")],
    )

    updated_properties = current.compact_dict
    updated.update(updates.compact_dict)

    check_properties(
        updated,
        ignore=[CheckErrorMatcher(validator="required", json_path="resources")],
    )

    return PackageProperties.from_dict(updated)
