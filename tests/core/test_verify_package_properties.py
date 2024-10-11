from pytest import fixture, mark, raises

from sprout.core.not_properties_error import NotPropertiesError
from sprout.core.properties import (
    ContributorProperties,
    LicenseProperties,
    PackageProperties,
    SourceProperties,
)
from sprout.core.verify_package_properties import (
    REQUIRED_PACKAGE_PROPERTIES,
    verify_package_properties,
)


@fixture
def properties():
    return PackageProperties(
        name="my-package",
        id="123-abc-123",
        title="My Package",
        description="This is my package.",
        version="2.0.0",
        created="2024-05-14T05:00:01+00:00",
    ).asdict


def test_accepts_required_fields(properties):
    """Should accept an object containing values for required fields."""
    assert verify_package_properties(properties) == properties


def test_accepts_required_and_optional_fields(properties):
    """Should accept an object containing values for required and optional fields."""
    properties["homepage"] = "www.mypage.com"
    properties["keywords"] = ["a", "b"]
    properties["image"] = "my/image"
    properties["licenses"] = [LicenseProperties(name="a license").asdict]
    properties["sources"] = [SourceProperties().asdict]
    properties["contributors"] = [ContributorProperties().asdict]
    properties["custom1"] = ""
    properties["custom2"] = "test"

    assert verify_package_properties(properties) == properties


def test_rejects_empty_object():
    """Should reject an empty object."""
    with raises(NotPropertiesError) as error:
        verify_package_properties({})

    message = str(error.value)
    for field in REQUIRED_PACKAGE_PROPERTIES:
        assert f"'{field}' is a required property" in message


def test_rejects_properties_not_conform_to_spec(properties):
    """Should reject an object with a value not meeting the Data Package spec."""
    properties["name"] = "an invalid name"

    with raises(NotPropertiesError, match="at property 'name'"):
        verify_package_properties(properties)


@mark.parametrize("field", REQUIRED_PACKAGE_PROPERTIES)
@mark.parametrize("empty_value", ["", None])
def test_rejects_empty_value_for_required_fields(properties, field, empty_value):
    """Should reject an object with a missing or blank required field."""
    properties[field] = empty_value

    with raises(NotPropertiesError, match=f"'{field}' is a required property"):
        verify_package_properties(properties)
