from seedcase_sprout.check_properties import (
    check_properties,
)
from seedcase_sprout.properties import PackageProperties


def update_package_properties(
    current_properties: PackageProperties, update_properties: PackageProperties
) -> PackageProperties:
    """Updates the properties of an existing package.

    Use this any time you want to update the package's properties.  When you
    need to update the `datapackage.json` file, use this function to ensure the
    properties are correctly structured before they're written. It only updates
    the properties of the package itself, not of the data resources contained
    within the package.

    If the properties in the `update_properties` argument are correct (i.e.,
    they pass the properties checks), they will overwrite any pre-existing
    properties within the `current` properties.

    Args:
        current_properties: The current properties found in the
            `datapackage.json` file. Use `read_properties()` to get the current
            properties.
        update_properties: The new package properties to update from the current ones.
            Use `PackageProperties` to provide a correctly structured properties
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
        import seedcase_sprout as sp

        sp.update_package_properties(
            current_properties=sp.example_package_properties(),
            update_properties=sp.PackageProperties(
                title="New Package Title",
                name="new-package-name",
                description="New Description",
            ),
        )
        ```
    """
    # In case someone adds a resource to the `update_properties`, we need to
    # remove it since this function doesn't add resources.
    update_properties.resources = None
    check_properties(current_properties)

    updated_properties_dict = current_properties.compact_dict
    updated_properties_dict.update(update_properties.compact_dict)
    updated_properties = PackageProperties.from_dict(updated_properties_dict)

    return check_properties(updated_properties)
