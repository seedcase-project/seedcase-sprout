from pathlib import Path

import check_datapackage as cdp
from pytest import fixture, mark, raises

from seedcase_sprout.check_properties import (
    DataResourceError,
    check_package_properties,
    check_properties,
    check_resource_properties,
)
from seedcase_sprout.examples import example_resource_properties
from seedcase_sprout.properties import (
    ContributorProperties,
    LicenseProperties,
    PackageProperties,
    ResourceProperties,
    SourceProperties,
)
from seedcase_sprout.sprout_checks.required_fields import (
    PACKAGE_SPROUT_REQUIRED_FIELDS,
    RESOURCE_SPROUT_REQUIRED_FIELDS,
)


@fixture
def properties():
    return PackageProperties(
        name="package-1",
        id="abc1",
        title="Package 1",
        description="A package.",
        version="1.0.0",
        created="2024-05-14T05:00:01+00:00",
        licenses=[LicenseProperties(name="a-license")],
        contributors=[ContributorProperties(title="a contributor")],
        sources=[SourceProperties(title="a source")],
        resources=[
            ResourceProperties(
                name="resource-1",
                title="Resource 1",
                description="A resource.",
            ),
            ResourceProperties(
                name="resource-2",
                title="Resource 2",
                description="A second resource.",
            ),
        ],
    )


def test_passes_correct_properties(properties):
    """Should pass if all required properties are present and correct."""
    assert check_properties(properties) == properties
    assert check_package_properties(properties) == properties
    assert check_resource_properties(properties.resources[0]) == properties.resources[0]
    assert check_resource_properties(properties.resources[1]) == properties.resources[1]

    # Even when resources isn't there.
    delattr(properties, "resources")
    assert check_properties(properties) == properties


def test_error_incorrect_argument():
    """Should be an error if it isn't a `*Properties` object."""
    with raises(TypeError):
        check_properties(ResourceProperties())

    with raises(TypeError):
        check_resource_properties(PackageProperties())

    with raises(TypeError):
        check_properties("")

    with raises(TypeError):
        check_properties([1, 2, 3])

    with raises(TypeError):
        check_package_properties([1, 2, 3])

    with raises(TypeError):
        check_package_properties("")

    with raises(TypeError):
        check_resource_properties([1, 2, 3])

    with raises(TypeError):
        check_resource_properties("")


@mark.parametrize("field", PACKAGE_SPROUT_REQUIRED_FIELDS)
def test_error_missing_required_package_properties(properties, field):
    """Should be an error if a required package properties is missing."""
    delattr(properties, field)

    # All properties checks
    with raises(cdp.DataPackageError):
        check_properties(properties)

    # Package only checks
    with raises(cdp.DataPackageError):
        check_package_properties(properties)


@mark.parametrize(
    "item,value,validator",
    [
        ("name", "a name with spaces", "pattern"),
        ("title", 123, "type"),
        ("homepage", "not a URL", "format"),
        ("resources", 123, "type"),
    ],
)
def test_error_incorrect_property_values(properties, item, value, validator):
    """Should be an error when the property value is incorrect."""
    setattr(properties, item, value)

    # All properties checks
    with raises(cdp.DataPackageError):
        check_properties(properties)

    # Package only checks
    with raises(cdp.DataPackageError):
        check_package_properties(properties)


@mark.parametrize("name", PACKAGE_SPROUT_REQUIRED_FIELDS)
@mark.parametrize("value", ["", []])
def test_error_blank_package_properties(properties, name, value):
    """Should be an error when a required package field is blank."""
    setattr(properties, name, value)

    # All properties checks
    with raises(cdp.DataPackageError):
        check_properties(properties)

    # Package only checks
    with raises(cdp.DataPackageError):
        check_package_properties(properties)


def test_error_missing_required_nested_properties(properties):
    """Should have errors when the nested required properties are missing."""
    setattr(properties, "licenses", [{}])
    setattr(properties, "contributors", [{}])
    setattr(properties, "sources", [{}])

    # All properties checks
    with raises(cdp.DataPackageError):
        check_properties(properties)

    # Package only checks
    with raises(cdp.DataPackageError):
        check_package_properties(properties)


# Resource properties specific --------------------------------------------


@mark.parametrize(
    "field",
    RESOURCE_SPROUT_REQUIRED_FIELDS,
)
def test_error_missing_required_resource_properties(properties, field):
    """Should be an error if a required resource properties is missing."""
    delattr(properties.resources[0], field)

    # All properties checks
    with raises(cdp.DataPackageError):
        check_properties(properties)

    # Resource only checks
    with raises(DataResourceError):
        check_resource_properties(properties.resources[0])


@mark.parametrize("name", RESOURCE_SPROUT_REQUIRED_FIELDS)
@mark.parametrize("value", ["", []])
def test_error_blank_resource_properties(properties, name, value):
    """Should be an error when one required resource field is blank."""
    setattr(properties.resources[0], name, value)

    # All properties checks
    with raises(cdp.DataPackageError):
        check_properties(properties)

    # Resource only checks
    with raises(DataResourceError):
        check_resource_properties(properties.resources[0])


def test_errors_flagged_for_fields_with_multipart_name():
    """Errors should be flagged when the name of the field has more than one word."""
    properties = example_resource_properties()
    assert properties.schema
    properties.schema.primary_key = []

    with raises(DataResourceError):
        check_resource_properties(properties)


def test_error_incorrect_resource_property_values(properties):
    """Should be an error when the property value is incorrect."""
    properties.resources[0].title = 123

    # All properties checks
    with raises(cdp.DataPackageError):
        check_properties(properties)

    # Resource only checks
    with raises(DataResourceError):
        check_resource_properties(properties.resources[0])


@mark.parametrize(
    "path", ["", [], 123, str(Path("resources", "1")), "/bad/path/data.csv"]
)
def test_error_no_resource_name_in_path(properties, path):
    """Should be an error when the resource name isn't in the `path` or is empty."""
    properties.resources[0].path = path

    # All properties checks
    with raises(cdp.DataPackageError):
        check_properties(properties)

    # Resource only checks
    with raises(DataResourceError):
        check_resource_properties(properties.resources[0])
