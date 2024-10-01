from pytest import mark, raises

from sprout.core.invalid_properties_error import InvalidPropertiesError
from sprout.core.verify_resource_properties import verify_resource_properties


def test_returns_valid_properties():
    """Given a set of valid properties, should return the same set of properties."""
    properties = {
        "name": "test",
        "type": "table",
        "path": "test.csv",
        "scheme": "file",
        "format": "csv",
        "mediatype": "text/csv",
        "encoding": "utf-8",
        "schema": {
            "fields": [
                {"name": "id", "type": "integer", "constraints": {"required": True}},
                {"name": "name", "type": "string"},
                {"name": "dob", "type": "date"},
            ]
        },
    }
    assert verify_resource_properties(properties) == properties


def test_returns_valid_properties_with_custom_field():
    """Given a set of valid properties with a custom field, should return the same
    set of properties."""
    properties = {
        "name": "test",
        "custom": 123,
        "type": "table",
        "path": "test.csv",
        "scheme": "file",
        "format": "csv",
        "mediatype": "text/csv",
        "encoding": "utf-8",
        "schema": {
            "custom": "custom",
            "fields": [
                {"name": "id", "type": "integer", "constraints": {"required": True}},
                {"name": "name", "type": "string"},
                {"name": "dob", "type": "date", "custom": False},
            ],
        },
    }
    assert verify_resource_properties(properties) == properties


@mark.parametrize("properties", [{}, [], 1, None])
def test_rejects_completely_malformed_properties(properties):
    """Given an input which is empty or the wrong type, should throw
    InvalidPropertiesError."""
    with raises(InvalidPropertiesError):
        verify_resource_properties(properties)


def test_rejects_properties_with_single_invalid_field():
    """Given a set of properties with a single invalid field, should throw
    InvalidPropertiesError."""
    properties = {
        "name": "test",
        "type": "unknown type",
        "path": "test.csv",
        "scheme": "file",
        "format": "csv",
        "mediatype": "text/csv",
        "encoding": "utf-8",
        "schema": {
            "fields": [
                {"name": "id", "type": "integer", "constraints": {"required": True}},
                {"name": "name", "type": "string"},
                {"name": "dob", "type": "date"},
            ]
        },
    }

    with raises(
        InvalidPropertiesError,
        match='resource type "unknown type" is not supported',
    ):
        verify_resource_properties(properties)


def test_rejects_properties_with_multiple_invalid_fields():
    """Given a set of properties with multiple invalid fields, should throw
    InvalidPropertiesError."""
    properties = {
        "type": "table",
        "path": "test.csv",
        "scheme": "file",
        "format": 123,
        "mediatype": "text/csv",
        "encoding": "utf-8",
        "schema": {
            "fields": [
                {"name": "id", "type": "integer", "constraints": {"required": True}},
                {"name": "name", "type": "string"},
                {"name": "dob", "type": "date"},
            ]
        },
    }

    with raises(InvalidPropertiesError) as error:
        verify_resource_properties(properties)

    message = str(error.value)
    assert "'name' is a required property" in message
    assert "123 is not of type 'string' at property 'format'" in message
