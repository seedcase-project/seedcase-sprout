from pytest import mark

from seedcase_sprout.core.check_datapackage.is_resource_name_correct import (
    is_resource_name_correct,
)


@mark.parametrize(
    "name, expected",
    [
        (None, False),
        ("", False),
        ("space a", False),
        ("CAPITAL", False),
        (123, False),
        ("a-name99", True),
    ],
)
def test_checks_resource_name(name, expected):
    """Should decide if a resource name is correctly formatted."""
    assert is_resource_name_correct(name) is expected
