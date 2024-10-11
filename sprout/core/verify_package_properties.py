from frictionless.errors import PackageError

from sprout.core.verify_properties_complete import verify_properties_complete
from sprout.core.verify_properties_well_formed import verify_properties_well_formed

REQUIRED_PACKAGE_PROPERTIES = {
    "name",
    "id",
    "title",
    "description",
    "version",
    "created",
}


def verify_package_properties(properties: dict) -> dict:
    """Verifies if a dictionary representation of a set of package properties is valid.

    The package properties are valid if they conform to the Data Package specification
    and they contain non-empty values for all required package properties fields.

    Args:
        properties: The package properties to verify.

    Returns:
        The package properties, if valid.

    Raises:
        NotPropertiesError: If the package properties are not correct.
    """
    verify_properties_complete(properties, PackageError, REQUIRED_PACKAGE_PROPERTIES)
    verify_properties_well_formed(properties)

    return properties
