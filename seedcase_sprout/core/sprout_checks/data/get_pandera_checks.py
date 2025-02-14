import pandera.polars as pa
from pandera import Check
from xmlschema.names import (
    XSD_DATE,
    XSD_DATETIME,
    XSD_DURATION,
    XSD_GYEAR,
    XSD_GYEAR_MONTH,
    XSD_TIME,
)

from seedcase_sprout.core.properties import FieldProperties
from seedcase_sprout.core.sprout_checks.data.data_type_checks import (
    check_binary,
    check_email,
    check_geopoint,
    check_json,
    check_uuid,
    check_xml_type,
)

# https://datapackage.org/standard/table-schema/#boolean
BOOLEAN_VALUES = {"false", "False", "FALSE", "0", "true", "True", "TRUE", "1"}

STRING_FORMAT_CHECKS = {
    "email": pa.Check(
        check_email,
        element_wise=True,
        error="Invalid email address.",
    ),
    "binary": pa.Check(
        check_binary,
        element_wise=True,
        error="Invalid data format. Expected a Base64-encoded string.",
    ),
    "uuid": pa.Check(
        check_uuid,
        element_wise=True,
        error="Invalid UUID format. Expected a valid UUID.",
    ),
}


def get_pandera_checks(field: FieldProperties) -> list[Check]:
    """Returns the Pandera checks appropriate for the field's format and data type.

    Args:
        field: The field to get the checks for.

    Returns:
        The appropriate Pandera checks.
    """
    if field.type == "string" and (
        format_check := STRING_FORMAT_CHECKS.get(field.format, None)
    ):
        return [format_check]

    match field.type:
        case "boolean":
            return [
                pa.Check(
                    lambda value: value in BOOLEAN_VALUES,
                    element_wise=True,
                    error=f"Invalid boolean value. Must be one of {BOOLEAN_VALUES}.",
                )
            ]

        case "time":
            return [
                pa.Check(
                    lambda value: check_xml_type(value, XSD_TIME),
                    element_wise=True,
                    error="Invalid time format. Expected HH:MM:SS.",
                )
            ]

        case "datetime":
            return [
                pa.Check(
                    lambda value: check_xml_type(value, XSD_DATETIME),
                    element_wise=True,
                    error=(
                        "Invalid datetime format. Expected YYYY-MM-DDTHH:MM:SS with "
                        "optional milliseconds and time zone information."
                    ),
                )
            ]

        case "date":
            return [
                pa.Check(
                    lambda value: check_xml_type(value, XSD_DATE),
                    element_wise=True,
                    error="Invalid date format. Expected YYYY-MM-DD.",
                )
            ]

        case "year":
            return [
                pa.Check(
                    lambda value: check_xml_type(value, XSD_GYEAR),
                    element_wise=True,
                    error="Invalid year format. Expected YYYY.",
                )
            ]

        case "yearmonth":
            return [
                pa.Check(
                    lambda value: check_xml_type(value, XSD_GYEAR_MONTH),
                    element_wise=True,
                    error="Invalid yearmonth format. Expected YYYY-MM.",
                )
            ]

        case "duration":
            return [
                pa.Check(
                    lambda value: check_xml_type(value, XSD_DURATION),
                    element_wise=True,
                    error="Invalid duration format. Expected PnYnMnDTnHnMnS.",
                )
            ]

        case "object":
            return [
                pa.Check(
                    lambda value: check_json(value, dict),
                    element_wise=True,
                    error="Could not parse JSON object. Expected a valid JSON object.",
                )
            ]

        case "array":
            return [
                pa.Check(
                    lambda value: check_json(value, list),
                    element_wise=True,
                    error="Could not parse JSON array. Expected a valid JSON array.",
                )
            ]

        case "geopoint":
            return [
                pa.Check(
                    check_geopoint,
                    element_wise=True,
                    error="Invalid geopoint data. Expected LAT, LONG.",
                )
            ]

        case _:
            return []
