from frictionless import Package

from sprout.core.invalid_properties_error import InvalidPropertiesError
from sprout.core.verify_required_package_properties import (
    verify_required_package_properties,
)


def verify_package_properties(properties: dict) -> dict:
    """Verifies if a dictionary representation of a set of package properties is valid.

    The package properties are valid if they conform to the Data Package specification
    and they contain non-empty values for all required package properties fields.

    Args:
        properties: The package properties to verify.

    Returns:
        The package properties, if valid.

    Raises:
        InvalidPropertiesError: If the package properties are not valid.
    """
    report = Package.validate_descriptor(properties)
    report = verify_required_package_properties(report, properties)

    if not report.valid:
        raise InvalidPropertiesError(report, properties)

    return properties
