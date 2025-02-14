import json
import re
import uuid

import xmlschema

# Data types for validating time and date values
XML_SCHEMA_TYPES = xmlschema.XMLSchema11(
    '<xsd:schema xmlns:xsd="http://www.w3.org/2001/XMLSchema"/>'
).types


def check_xml_type(value: str, xml_type: str) -> bool:
    """Checks if the given `value` is formatted as a valid XML data type.

    The Frictionless Data Package standard follows the definitions at
    https://www.w3.org/TR/xmlschema-2/ for time and date-related data types.
    This function is for checking values against these XML data type definitions.

    Args:
        value: The value to check.
        xml_type: The XML data type to check against.

    Returns:
        True if the value is valid as the given type, False otherwise.
    """
    try:
        XML_SCHEMA_TYPES[xml_type].decode(value)
        return True
    except (xmlschema.XMLSchemaDecodeError, KeyError):
        return False


def check_json(value: str, expected_type: type[list | dict]) -> bool:
    """Checks if the given `value` is formatted as a valid JSON object or array.

    Args:
        value: The value to check.
        expected_type: The expected JSON type: an object or an array.

    Returns:
        True if the value is valid as the given JSON type, False otherwise.
    """
    try:
        return isinstance(json.loads(value), expected_type)
    except json.JSONDecodeError:
        return False


def check_geopoint(value: str) -> bool:
    """Checks if the given `value` is a valid geographic point.

    Args:
        value: The value to check.

    Returns:
        True if the value is a valid geographic point, False otherwise.
    """
    try:
        lat, long = value.split(",")
        return abs(float(lat.strip())) <= 90 and abs(float(long.strip())) <= 180
    except ValueError:
        return False


EMAIL_PATTERN = r"^[^@\s]+@[^@\s]+\.[^@\s]+$"


def check_email(value: str) -> bool:
    """Checks if `value` meets the main format constraints of email addresses.

    Args:
        value: The value to check.

    Returns:
        True if the value meets the main format constraints, False otherwise.
    """
    return bool(re.match(EMAIL_PATTERN, value)) and len(value) <= 254


# https://stackoverflow.com/q/475074
BASE64_PATTERN = r"^[-A-Za-z0-9+/]*={0,3}$"


def check_binary(value: str) -> bool:
    """Checks if `value` looks like a Base64-encoded string.

    Args:
        value: The value to check.

    Returns:
        True if the value looks like a Base64-encoded string, False otherwise.
    """
    return bool(re.match(BASE64_PATTERN, value))


def check_uuid(value: str) -> bool:
    """Checks if `value` can be parsed as a valid UUID.

    Args:
        value: The value to check.

    Returns:
        True if the value can be parsed as a UUID, False otherwise.
    """
    try:
        uuid.UUID(value)
        return True
    except ValueError:
        return False
