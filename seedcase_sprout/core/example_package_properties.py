from seedcase_sprout.core.properties import (
    ContributorProperties,
    LicenseProperties,
    PackageProperties,
)
from seedcase_sprout.core.sprout_checks.check_package_properties import (
    check_package_properties,
)


def example_package_properties() -> PackageProperties:
    """Generate an example package properties object.

    Returns:
        Outputs a correctly formatted example `PackageProperties` object.

    Examples:
        ```{python}
        import seedcase_sprout.core as sp
        sp.example_package_properties()
        ```
    """
    default_properties = PackageProperties.default()
    update_properties = PackageProperties(
        name="example-package",
        title="Example fake data package",
        description="Data from a fake data package on something.",
        contributors=[
            ContributorProperties(
                title="Jamie Jones",
                email="jamie_jones@example.com",
                roles=["creator"],
            )
        ],
        licenses=[
            LicenseProperties(
                name="ODC-BY-1.0",
                path="https://opendatacommons.org/licenses/by",
                title="Open Data Commons Attribution License 1.0",
            )
        ],
    ).compact_dict

    update_properties.update(default_properties.compact_dict)

    check_package_properties(update_properties)

    return PackageProperties.from_dict(update_properties)
