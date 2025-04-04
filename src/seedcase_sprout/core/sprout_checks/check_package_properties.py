from seedcase_sprout.core.check_datapackage.check_error_matcher import CheckErrorMatcher
from seedcase_sprout.core.properties import PackageProperties
from seedcase_sprout.core.sprout_checks.check_properties import (
    RESOURCE_FIELD_PATTERN,
    check_properties,
)


def check_package_properties(
    properties: PackageProperties | dict, ignore: list[CheckErrorMatcher] = []
) -> PackageProperties | dict:
    """Checks that package `properties` matches requirements in Sprout.

    `properties` is checked against the Data Package standard and the following
    Sprout-specific requirements:
      - Sprout-specific required fields are present
      - Required fields are not blank

    Only package properties are checked.

    Args:
        properties: The package properties to check.
        ignore: A list of matchers for any `CheckErrors` to ignore.

    Returns:
        `properties` if all checks pass.

    Raises:
        ExceptionGroup: A group of `CheckError`s, one error per failed check.
    """
    return check_properties(
        properties,
        ignore=[
            *ignore,
            CheckErrorMatcher(json_path=RESOURCE_FIELD_PATTERN),
            CheckErrorMatcher(json_path=r"resources$", validator="required"),
        ],
    )
