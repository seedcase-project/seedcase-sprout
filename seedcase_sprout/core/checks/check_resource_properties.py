from jsonschema import ValidationError

from seedcase_sprout.core.checks.check_object_against_json_schema import (
    check_object_against_json_schema,
)
from seedcase_sprout.core.checks.config import DATA_PACKAGE_SCHEMA_PATH, NAME_PATTERN
from seedcase_sprout.core.read_json import read_json


def check_resource_properties(
    properties: dict, check_recommendations: bool = True
) -> list[ValidationError]:
    """Checks that `properties` matches the Data Resource standard.

    Structural, type and format constraints are all checked. All schema violations are
    collected before errors are returned.

    Args:
        properties: The resource properties to check.
        check_recommendations: Whether `properties` should be checked against
            recommendations in the Data Resource standard. Defaults to True.

    Returns:
        A list of errors. The empty list, if no errors are found.
    """
    schema = read_json(DATA_PACKAGE_SCHEMA_PATH)
    schema = schema["properties"]["resources"]["items"]

    # Recommendations from the Data Package standard
    if check_recommendations:
        schema["properties"]["name"]["pattern"] = NAME_PATTERN

    return check_object_against_json_schema(properties, schema)
