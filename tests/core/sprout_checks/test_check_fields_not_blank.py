from pytest import mark

from seedcase_sprout.core.checks.required_fields import RequiredFieldType
from seedcase_sprout.core.sprout_checks.check_fields_not_blank import (
    check_fields_not_blank,
)
from seedcase_sprout.core.sprout_checks.get_json_path_to_resource_field import (
    get_json_path_to_resource_field,
)

FIELDS = {"name": RequiredFieldType.str, "tags": RequiredFieldType.list}


@mark.parametrize("index", [None, 2])
def test_passes_properties_with_populated_fields(index):
    """Should pass properties with fields populated."""
    properties = {"name": "My name", "tags": ["a", "b"]}

    assert check_fields_not_blank(properties, FIELDS, index) == []


@mark.parametrize("index", [None, 2])
def test_passes_properties_with_fields_missing(index):
    """Should pass properties without the specified fields."""
    assert check_fields_not_blank({}, FIELDS, index) == []


@mark.parametrize("index", [None, 2])
def test_fails_properties_with_blank_field(index):
    """Should fail properties with a blank field."""
    properties = {"name": "My name", "tags": []}

    errors = check_fields_not_blank(properties, FIELDS, index)

    assert len(errors) == 1
    assert errors[0].message == "'tags' should not be blank"
    assert errors[0].json_path == get_json_path_to_resource_field("tags", index)
    assert errors[0].validator == "blank"


@mark.parametrize("index", [None, 2])
def test_fails_properties_with_multiple_blank_fields(index):
    """Should fail properties with multiple blank fields."""
    properties = {"name": "", "tags": []}

    errors = check_fields_not_blank(properties, FIELDS, index)

    assert len(errors) == 2
    assert all(error.validator == "blank" for error in errors)
    assert any(
        error.json_path == get_json_path_to_resource_field("name", index)
        for error in errors
    )
    assert any(
        error.json_path == get_json_path_to_resource_field("tags", index)
        for error in errors
    )