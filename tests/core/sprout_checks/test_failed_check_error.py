from seedcase_sprout.core.checks.check_error import CheckError
from seedcase_sprout.core.sprout_checks.failed_check_error import FailedCheckError

check_errors = [
    CheckError(
        message="'path' is a required field", json_path="$.path", validator="required"
    ),
    CheckError(
        message="'name' is not of type 'string'", json_path="$.name", validator="type"
    ),
]
error = FailedCheckError("Summary error message!", check_errors)


def test_error_stringified_correctly():
    """Should stringify error correctly."""
    assert str(error) == (
        "Summary error message!\nThe following checks failed:"
        f"\n{check_errors[0]}\n{check_errors[1]}"
    )


def test_error_represented_correctly():
    """Should generate the developer-friendly representation correctly."""
    assert repr(error) == (
        "FailedCheckError(message='Summary error message!', "
        f"errors={repr(check_errors)})"
    )
