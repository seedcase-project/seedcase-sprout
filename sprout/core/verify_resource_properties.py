from frictionless import Resource

from sprout.core.invalid_properties_error import InvalidPropertiesError


def verify_resource_properties(properties: dict) -> dict:
    """Checks if the resource properties provided are valid.

    Args:
        properties: the resource properties to check

    Raises:
        InvalidPropertiesError: if Frictionless finds an error in the properties

    Returns:
        the properties, if valid
    """
    report = Resource.validate_descriptor(properties)
    if not report.valid:
        raise InvalidPropertiesError(report, properties)
    return properties
