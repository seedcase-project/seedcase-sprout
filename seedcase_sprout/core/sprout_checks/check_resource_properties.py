from seedcase_sprout.core import checks
from seedcase_sprout.core.checks.check_error_matcher import CheckErrorMatcher
from seedcase_sprout.core.checks.exclude_errors import exclude_errors
from seedcase_sprout.core.sprout_checks.failed_check_error import FailedCheckError
from seedcase_sprout.core.sprout_checks.get_sprout_resource_errors import (
    get_sprout_resource_errors,
)


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
        FailedCheckError: If at least one check failed.
    """
    errors = checks.check_resource_properties(properties) + get_sprout_resource_errors(
        properties
    )
    errors = exclude_errors(
        errors,
        [
            *ignore,
            CheckErrorMatcher(validator="required", json_path="data"),
            CheckErrorMatcher(
                validator="type", json_path="path", message="not of type 'array'"
            ),
        ],
    )
    errors = sorted(set(errors))

    if errors:
        raise FailedCheckError(
            f"Resource properties check failed on properties\n{properties}", errors
        )

    return properties
