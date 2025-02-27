import polars as pl
from xmlschema.names import (
    XSD_BASE64_BINARY,
    XSD_DATE,
    XSD_DATETIME,
    XSD_DURATION,
    XSD_GYEAR,
    XSD_GYEAR_MONTH,
    XSD_TIME,
)

from seedcase_sprout.core.properties import FieldProperties
from seedcase_sprout.core.sprout_checks.check_data_types import check_is_xml_type

# https://datapackage.org/standard/table-schema/#boolean
BOOLEAN_VALUES = {"false", "False", "FALSE", "0", "true", "True", "TRUE", "1"}


def check_boolean(value) -> ValueError | None:
    if value not in BOOLEAN_VALUES:
        return ValueError(f"The given value needs to be one of {BOOLEAN_VALUES}.")


def check_time(value) -> ValueError | None:
    if not check_is_xml_type(value, XSD_TIME):
        return ValueError(
            "The given value doesn't seem to be a correctly formatted "
            "time value. The expected format for time values is HH:MM:SS. "
            "See https://www.w3.org/TR/xmlschema-2/#time for more "
            "information."
        )


def check_column(col: pl.Expr, field: FieldProperties, errors: list[Exception]):
    match field.type:
        case "boolean":
            checker = check_boolean

        case "time":
            checker = check_time

    def check_value(value):
        error = checker(value)
        if error:
            errors.append(error)
        return value

    return col.map_elements(check_value, return_dtype=pl.String)
