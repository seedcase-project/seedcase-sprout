from seedcase_sprout.core.checks.check_error import CheckError
from seedcase_sprout.core.sprout_checks.remove_not_sprout_related_resource_errors import (  # noqa: E501
    get_sprout_specific_resource_errors,
)


def test_returns_unaltered_empty_list():
    """Should not alter an empty list."""
    assert get_sprout_specific_resource_errors([]) == []


def test_returns_only_sprout_related_errors():
    """Should only remove errors not relevant for Sprout."""
    errors = [
        CheckError(
            message="'data' is a required property",
            json_path="$.data",
            validator="required",
        ),
        CheckError(
            message="'name' is a required property",
            json_path="$.name",
            validator="required",
        ),
        CheckError(
            message="123 is not of type 'array'", json_path="$.path", validator="type"
        ),
        CheckError(
            message="123 is not of type 'string'", json_path="$.path", validator="type"
        ),
        CheckError(
            message="123 is not of type 'array'",
            json_path="$.sources",
            validator="type",
        ),
    ]

    assert get_sprout_specific_resource_errors(errors) == [
        CheckError(
            message="'name' is a required property",
            json_path="$.name",
            validator="required",
        ),
        CheckError(
            message="123 is not of type 'string'", json_path="$.path", validator="type"
        ),
        CheckError(
            message="123 is not of type 'array'",
            json_path="$.sources",
            validator="type",
        ),
    ]
