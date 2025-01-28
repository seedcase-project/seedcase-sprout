from seedcase_sprout.core.checks.check_error_matcher import CheckErrorMatcher
from seedcase_sprout.core.sprout_checks.check_properties import check_properties

PACKAGE_FIELD_PATTERN = r"\$\.\w+$"


def check_resource_properties(
    properties: dict, ignore: list[CheckErrorMatcher] = []
) -> dict:
    """Checks that resource `properties` matches requirements in Sprout.

    `properties` is checked against the Data Package standard and the following
    Sprout-specific requirements:
      - Sprout-specific required fields are present
      - Required fields are not blank
      - `path` is of type string
      - `path` includes resource ID
      - `data` is not set

    Only resource properties are checked.

    Args:
        properties: The resource properties to check.
        ignore: A list of matchers for any `CheckErrors` to ignore.

    Returns:
        `properties`, if all checks passed.

    Raises:
        ExceptionGroup: A group of `CheckError`s, one error per failed check.
    """
    try:
        check_properties(
            {"resources": [properties]},
            ignore=[*ignore, CheckErrorMatcher(json_path=PACKAGE_FIELD_PATTERN)],
        )
    except ExceptionGroup as error_info:
        for error in error_info.exceptions:
            error.json_path = error.json_path.replace("resources[0].", "")
        raise error_info

    return properties
