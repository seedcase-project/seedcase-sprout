from jsonschema import ValidationError

from seedcase_sprout.core.checks.check_object_against_json_schema import (
    check_object_against_json_schema,
)
from seedcase_sprout.core.checks.config import (
    DATA_PACKAGE_SCHEMA_PATH,
    NAME_PATTERN,
    SEMVER_PATTERN,
)
from seedcase_sprout.core.read_json import read_json


def check_package_properties(
    properties: dict, check_recommendations: bool = True
) -> list[ValidationError]:
    """Checks that `properties` matches the Data Package standard.

    Structural, type and format constraints are all checked. All schema violations are
    collected before errors are returned.

    Args:
        properties: The package properties to check.
        check_recommendations: Whether `properties` should be checked against
            recommendations in the Data Package standard. Defaults to True.

    Returns:
        A list of errors. The empty list, if no errors are found.
    """
    schema = read_json(DATA_PACKAGE_SCHEMA_PATH)
    schema["required"] = [field for field in schema["required"] if field != "resources"]
    del schema["properties"]["resources"]["minItems"]
    del schema["properties"]["resources"]["items"]

    # Recommendations from the Data Package standard
    if check_recommendations:
        schema["required"].extend(["name", "id", "licenses"])
        schema["properties"]["name"]["pattern"] = NAME_PATTERN
        schema["properties"]["version"]["pattern"] = SEMVER_PATTERN
        schema["properties"]["contributors"]["items"]["required"] = ["title"]
        schema["properties"]["sources"]["items"]["required"] = ["title"]

    return check_object_against_json_schema(properties, schema)
