from typing import Iterator

from jsonschema import ValidationError

from seedcase_sprout.core.checks.check_error import CheckError
from seedcase_sprout.core.checks.unwrap_errors import unwrap_errors

COMPLEX_VALIDATORS = {"allOf", "anyOf", "oneOf"}


def to_check_errors(validation_errors: Iterator[ValidationError]) -> list[CheckError]:
    """Transforms `jsonschema.ValidationError`s to more compact `CheckError`s.

    The list of errors is flattened and summary-type errors triggered by complex
    validators are filtered out.

    Args:
        validation_errors: The `jsonschema.ValidationError`s to transform.

    Returns:
        A list of `CheckError`s.
    """
    return [
        CheckError(
            message=error.message, json_path=error.json_path, validator=error.validator
        )
        for error in unwrap_errors(list(validation_errors))
        if error.validator not in COMPLEX_VALIDATORS
    ]
