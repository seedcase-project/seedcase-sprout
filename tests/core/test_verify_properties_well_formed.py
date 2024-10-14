from frictionless import errors
from pytest import fixture, raises

from sprout.core.not_properties_error import NotPropertiesError
from sprout.core.properties import PackageProperties, ResourceProperties
from sprout.core.verify_properties_well_formed import verify_properties_well_formed

error_type = errors.PackageError.type


@fixture
def package_properties():
    return PackageProperties(
        name="my-package",
        id="123-abc-123",
        title="My Package",
        description="This is my package.",
        version="2.0.0",
        created="2024-05-14T05:00:01+00:00",
    ).asdict


def test_accepts_default_values():
    """Should accept an object with default values, some of which are blank."""
    properties = PackageProperties().asdict

    assert verify_properties_well_formed(properties, error_type) == properties


def test_accepts_custom_values(package_properties):
    """Should accept a well-formed properties object."""
    assert (
        verify_properties_well_formed(package_properties, error_type)
        == package_properties
    )


def test_rejects_properties_not_conform_to_spec(package_properties):
    """Should reject an object with a value not meeting the Data Package spec."""
    package_properties["name"] = "an invalid name"

    with raises(NotPropertiesError, match="at property 'name'"):
        verify_properties_well_formed(package_properties, error_type)


def test_filters_for_the_specified_error_type(package_properties):
    """Should throw only if errors of the specified type are detected."""
    bad_resource = ResourceProperties(name="a bad name").asdict
    package_properties["resources"].append(bad_resource)

    assert (
        verify_properties_well_formed(package_properties, error_type)
        == package_properties
    )
