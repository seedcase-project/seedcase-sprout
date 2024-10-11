from frictionless import validate

from sprout.core.not_properties_error import NotPropertiesError


def verify_properties_well_formed(properties: dict) -> dict:
    """Verifies if the properties provided have the correct structure.

    This function checks that `properties` contains the fields expected by the Data
    Package spec.
    At this point, empty values are not checked against format constraints.

    Args:
        properties: The properties to verify.

    Returns:
        The properties, if well formed.

    Raises:
        NotPropertiesError: If the properties are not well formed.
    """
    non_empty_properties = {
        key: value for key, value in properties.items() if value != ""
    }
    report = validate(non_empty_properties)

    if not report.valid:
        raise NotPropertiesError(report.errors, properties)

    return properties
