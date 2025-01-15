from pytest import mark

from seedcase_sprout.core.checks.required_fields import RequiredFieldType
from seedcase_sprout.core.sprout_checks.check_list_item_field_not_blank import (
    check_list_item_field_not_blank,
)
from seedcase_sprout.core.sprout_checks.get_blank_value_for_type import (
    get_blank_value_for_type,
)


def test_passes_properties_without_list():
    """Should pass if the properties do not contain the specified list."""
    assert check_list_item_field_not_blank({}, "items", "field") == []


@mark.parametrize("items", [[], [{}, {}], [{"a": 1}, {"a": 2}]])
def test_passes_list_without_field(items):
    """Should pass if list items do not contain the field."""
    properties = {"items": items}

    assert check_list_item_field_not_blank(properties, "items", "field") == []


def test_passes_with_fields_populated():
    """Should pass if all fields are populated."""
    properties = {"items": [{"field": "value"}, {"field": "value"}]}

    assert check_list_item_field_not_blank(properties, "items", "field") == []


def test_passes_with_fields_of_wrong_type():
    """Should pass if the fields are present but of the wrong type."""
    properties = {"items": [{"field": "value"}, {"field": ""}]}

    assert (
        check_list_item_field_not_blank(
            properties, "items", "field", RequiredFieldType.list
        )
        == []
    )


@mark.parametrize(
    "field_type,value",
    [(RequiredFieldType.str, "value"), (RequiredFieldType.list, [1])],
)
def test_fails_item_with_blank_field(field_type, value):
    """Should fail if there is an item with a blank field."""
    properties = {
        "items": [{"field": value}, {"field": get_blank_value_for_type(field_type)}]
    }

    errors = check_list_item_field_not_blank(properties, "items", "field", field_type)

    assert len(errors) == 1
    assert errors[0].message == "'field' should not be blank"
    assert errors[0].json_path == "$.items[1].field"
    assert errors[0].validator == "blank"


@mark.parametrize("field_type", RequiredFieldType)
def test_fails_items_with_blank_field(field_type):
    """Should fail if there are multiple items with a blank field."""
    properties = {"items": [{"field": get_blank_value_for_type(field_type)}] * 2}

    errors = check_list_item_field_not_blank(properties, "items", "field", field_type)

    assert len(errors) == 2
    assert all(
        error.message == "'field' should not be blank" and error.validator == "blank"
        for error in errors
    )
    assert any(error.json_path == "$.items[0].field" for error in errors)
    assert any(error.json_path == "$.items[1].field" for error in errors)
