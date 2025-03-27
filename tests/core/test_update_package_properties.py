from dataclasses import replace
from pathlib import Path

from pytest import mark, raises

from seedcase_sprout.core.properties import (
    LicenseProperties,
    PackageProperties,
    ResourceProperties,
)
from seedcase_sprout.core.update_package_properties import update_package_properties

full_properties = PackageProperties(
    name="my-package",
    id="123-abc-123",
    title="My Package",
    description="This is my package.",
    version="1.0.0",
    created="2024-05-14T05:00:01+00:00",
    licenses=[LicenseProperties(name="license")],
)


@mark.parametrize(
    "properties",
    [
        PackageProperties(),
        PackageProperties(name="my-new-package-name"),
        full_properties,
    ],
)
def test_updates_only_change_package_properties(properties):
    """Should only update package properties and leave unchanged values as is."""
    expected_properties = PackageProperties.from_dict(
        full_properties.compact_dict | properties.compact_dict
    )

    updated_properties = update_package_properties(current_properties, new_properties)

    assert new_properties == expected_properties


@mark.parametrize(
    "current_properties",
    [
        PackageProperties(),
        PackageProperties(name="my-incomplete-package"),
    ],
)
def test_updates_incomplete_package_properties(current_properties):
    """Should update properties that were incomplete before they were updated."""
    new_properties = update_package_properties(current_properties, full_properties)

    assert new_properties == full_properties


def test_resources_not_added_from_incoming_properties():
    """When current properties have no resources, these should not be added from
    incoming properties."""
    properties = PackageProperties(resources=[ResourceProperties()])

    new_properties = update_package_properties(full_properties, properties)

    assert new_properties == full_properties


@mark.parametrize(
    "properties",
    [
        PackageProperties(),
        PackageProperties(resources=[ResourceProperties()]),
    ],
)
def test_current_resources_not_modified(properties):
    """When current properties have resources, these should not be modified."""
    current_properties = replace(
        full_properties,
        resources=[
            ResourceProperties(
                name="resource-1",
                path=str(Path("resources", "1", "data.parquet")),
                title="Resource 1",
                description="A resource.",
            )
        ],
    )
    new_properties = update_package_properties(current_properties, properties)

    assert new_properties == current_properties


def test_throws_error_if_current_properties_have_a_package_error():
    """Should throw a group of `CheckError`s if the current properties have an error
    among the package properties."""
    current_properties = PackageProperties(name="invalid name with spaces")
    properties = PackageProperties(name="my-new-package-name")

    with raises(ExceptionGroup) as error_info:
        update_package_properties(current_properties, properties)

    assert "invalid name with spaces" in error_info.value.message
    errors = error_info.value.exceptions
    assert len(errors) == 1
    assert errors[0].json_path == "$.name"
    assert errors[0].validator == "pattern"


def test_throws_error_if_current_properties_have_a_resource_error():
    """Should throw a group of `CheckError`s if the current properties have an error
    among the resource properties."""
    current_properties = replace(
        full_properties,
        resources=[
            ResourceProperties(
                name="invalid name with spaces",
                path=str(Path("resources", "1", "data.parquet")),
                title="Resource 1",
                description="A resource.",
            )
        ],
    )
    properties = PackageProperties(name="my-new-package-name")

    with raises(ExceptionGroup) as error_info:
        update_package_properties(current_properties, properties)

    assert "my-package" in error_info.value.message
    assert "invalid name with spaces" in error_info.value.message
    errors = error_info.value.exceptions
    assert len(errors) == 1
    assert errors[0].json_path == "$.resources[0].name"
    assert errors[0].validator == "pattern"


def test_throws_error_if_incoming_package_properties_are_malformed():
    """Should throw a group of `CheckError`s if the incoming package properties are
    malformed."""
    properties = PackageProperties(name="a name with spaces")

    with raises(ExceptionGroup) as error_info:
        update_package_properties(full_properties, properties)

    assert "a name with spaces" in error_info.value.message
    errors = error_info.value.exceptions
    assert len(errors) == 1
    assert errors[0].json_path == "$.name"
    assert errors[0].validator == "pattern"


def test_throws_error_if_resulting_properties_are_incomplete():
    """Should throw a group of `CheckError`s if the resulting properties have missing
    required fields."""
    current_properties = PackageProperties(name="my-incomplete-package")
    properties = PackageProperties(title="My Incomplete Package")

    with raises(ExceptionGroup) as error_info:
        update_package_properties(current_properties, properties)

    message = error_info.value.message
    assert "my-incomplete-package" in message
    assert "My Incomplete Package" in message
    errors = error_info.value.exceptions
    assert len(errors) == 5
    assert all(error.validator == "required" for error in errors)


def test_throws_error_if_both_current_and_incoming_properties_empty():
    """Should throw a group of `CheckError`s if both current and incoming properties are
    empty."""
    with raises(ExceptionGroup) as error_info:
        update_package_properties(PackageProperties(), PackageProperties())

    assert "{}" in error_info.value.message
    errors = error_info.value.exceptions
    assert len(errors) == 7
    assert all(error.validator == "required" for error in errors)
