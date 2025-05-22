from seedcase_sprout.check_datapackage.add_package_recommendations import (
    add_package_recommendations,
)
from seedcase_sprout.check_datapackage.add_resource_recommendations import (
    add_resource_recommendations,
)
from seedcase_sprout.check_datapackage.check_error import CheckError
from seedcase_sprout.check_datapackage.check_object_against_json_schema import (
    check_object_against_json_schema,
)
from seedcase_sprout.check_datapackage.constants import DATA_PACKAGE_SCHEMA_PATH
from seedcase_sprout.internals import _read_json


def check_properties(
    properties: dict, check_recommendations: bool = True
) -> list[CheckError]:
    """Checks that `properties` matches the Data Package standard (v2.0).

    Both package and resource properties are checked. Structural, type and format
    constraints are all checked. All schema violations are
    collected before errors are returned.

    The schema loaded or constructed in this function overrides any values specified
    in the `$schema` attribute of `properties`, including the default value.

    Args:
        properties: The full package properties to check, including resource properties.
        check_recommendations: Whether `properties` should be checked against
            recommendations in the Data Package standard in addition to requirements.
            Defaults to True.

    Returns:
        A list of errors. An empty list, if no errors are found.
    """
    schema = _read_json(DATA_PACKAGE_SCHEMA_PATH)

    if check_recommendations:
        add_package_recommendations(schema)
        add_resource_recommendations(schema)

    return check_object_against_json_schema(properties, schema)
