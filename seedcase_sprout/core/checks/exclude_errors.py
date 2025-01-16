from seedcase_sprout.core.checks.check_error import CheckError
from seedcase_sprout.core.checks.check_error_matcher import CheckErrorMatcher


def exclude_errors(
    errors: list[CheckError], matchers: list[CheckErrorMatcher]
) -> list[CheckError]:
    """Returns a new list of errors, with errors matched by any `matchers` filtered out.

    Args:
        errors: The errors to exclude matching errors from.
        matchers: The matches to exclude.

    Returns:
        A list of errors without any.
    """
    return [
        error
        for error in errors
        if not any(matcher.matches(error) for matcher in matchers)
    ]
