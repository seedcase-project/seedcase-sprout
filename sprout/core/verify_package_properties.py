from frictionless import Package
from frictionless.errors import PackageError

from sprout.core.not_properties_error import NotPropertiesError

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
    verify_package_properties_complete(properties)
    verify_package_properties_well_formed(properties)

    return properties


def verify_package_properties_complete(properties: dict) -> dict:
    """Verifies that all required fields are present on `properties` and not empty.

    Args:
        properties: The package properties to verify.

    Returns:
        The package properties, if complete.

    Raises:
        NotPropertiesError: If the package properties are not complete.
    """
    errors = [
        PackageError(note=f"'{field}' is a required property and cannot be empty.")
        for field in REQUIRED_PACKAGE_PROPERTIES
        if properties.get(field) in ["", None]
    ]

    if errors:
        raise NotPropertiesError(errors, properties)

    return properties


def verify_package_properties_well_formed(properties: dict) -> dict:
    """Verifies if the package properties provided have the correct structure.

    This function checks that `properties` contains the fields expected by the Data
    Package spec.
    At this point, empty values are not checked against format constraints.

    Args:
        properties: The package properties to verify.

    Returns:
        The package properties, if well formed.

    Raises:
        NotPropertiesError: If the package properties are not well formed.
    """
    non_empty_properties = {
        key: value for key, value in properties.items() if value != ""
    }
    report = Package.validate_descriptor(non_empty_properties)

    if not report.valid:
        raise NotPropertiesError(report.errors, properties)

    return properties
