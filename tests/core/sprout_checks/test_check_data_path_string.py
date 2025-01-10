from pytest import mark

from seedcase_sprout.core.sprout_checks.check_data_path_string import (
    check_data_path_string,
)
from seedcase_sprout.core.sprout_checks.get_json_path_to_resource_field import (
    get_json_path_to_resource_field,
)


@mark.parametrize("index", [None, 2])
def test_passes_if_data_path_string(index):
    """Should pass if the path is of type string."""
    properties = {"path": "a string"}

    assert check_data_path_string(properties, index) == []


@mark.parametrize("index", [None, 2])
def test_passes_if_data_path_not_present(index):
    """Should pass if the path is not set."""
    assert check_data_path_string({}, index) == []


@mark.parametrize("index", [None, 2])
def test_fails_if_path_not_string(index):
    """Should fail if the path is not of type string."""
    properties = {"path": 123}

    errors = check_data_path_string(properties, index)

    assert len(errors) == 1
    assert errors[0].message == "123 is not of type 'string'"
    assert errors[0].json_path == get_json_path_to_resource_field("path", index)
    assert errors[0].validator == "type"