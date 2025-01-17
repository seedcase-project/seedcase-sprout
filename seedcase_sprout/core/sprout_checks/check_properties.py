from seedcase_sprout.core import checks
from seedcase_sprout.core.checks.check_error_matcher import CheckErrorMatcher
from seedcase_sprout.core.checks.exclude_errors import exclude_errors
from seedcase_sprout.core.sprout_checks.failed_check_error import FailedCheckError
from seedcase_sprout.core.sprout_checks.get_sprout_package_errors import (
    get_sprout_package_errors,
)
from seedcase_sprout.core.sprout_checks.get_sprout_resource_errors import (
    get_sprout_resource_errors,
)


def check_properties(properties: dict, ignore: list[CheckErrorMatcher] = []) -> dict:
    """Checks that `properties` matches requirements in Sprout.

    `properties` is checked against the Data Package standard and Sprout-specific
    requirements. Both package and resource properties are checked.

    Args:
        properties: The full package properties to check, including resource properties.
        ignore: A list of matchers for any `CheckErrors` to ignore.

    Returns:
        `properties`, if all checks passed.

    Raises:
        FailedCheckError: If at least one check failed.
    """
    errors = checks.check_properties(properties)
    errors += get_sprout_package_errors(properties)

    for index, resource in enumerate(properties.get("resources", [])):
        errors += get_sprout_resource_errors(resource, index)

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
            f"Properties check failed on properties\n{properties}", errors
        )

    return properties
