from pytest import mark

from sprout.core.edit_resource_properties_field import edit_resource_properties_field


@mark.parametrize(
    "value", ["new value", 123, [1, 2, 3], {"outer": {"inner": "new value"}}]
)
def test_updates_existing_property(value):
    """Given a properties object with the specified property, should update that
    property to the specified value."""
    properties = {"test": "old value"}
    expected_properties = {"test": value}
    assert (
        edit_resource_properties_field(properties, "test", value) == expected_properties
    )


@mark.parametrize(
    "value", ["new value", 123, [1, 2, 3], {"outer": {"inner": "new value"}}]
)
def test_adds_new_property(value):
    """Given a properties object without the specified property, should add that
    property with the specified value."""
    properties = {}
    expected_properties = {"test": value}
    assert (
        edit_resource_properties_field(properties, "test", value) == expected_properties
    )
