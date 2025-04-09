from dataclasses import replace
from pathlib import Path

from pytest import mark, raises

from seedcase_sprout.core.properties import (
    LicenseProperties,
    PackageProperties,
    ResourceProperties,
)
from seedcase_sprout.core.update_package_properties import update_package_properties

test_properties = PackageProperties(
    name="my-package",
    id="123-abc-123",
    title="My Package",
    description="This is my package.",
    version="1.0.0",
    created="2024-05-14T05:00:01+00:00",
    licenses=[LicenseProperties(name="license")],
)


@mark.parametrize(
    "properties_updates",
    [
        PackageProperties(),
        PackageProperties(name="my-new-package-name"),
        test_properties,
    ],
)
def test_updates_only_change_package_properties(properties_updates):
    """Should only update package properties and leave unchanged values as is."""
    # To make clear it is the current one.
    current_properties = test_properties
    expected_properties = PackageProperties.from_dict(
        current_properties.compact_dict | properties_updates.compact_dict
    )

    updated_properties = update_package_properties(
        current_properties, properties_updates
    )

    assert updated_properties == expected_properties


@mark.parametrize(
    "current_properties",
    [
        PackageProperties(),
        PackageProperties(name="my-incomplete-package"),
    ],
)
def test_updates_incomplete_package_properties(current_properties):
    """Should update properties that were incomplete before they were updated."""
    # To make clear what this is.
    properties_updates = test_properties
    updated_properties = update_package_properties(
        current_properties, properties_updates
    )

    assert updated_properties == properties_updates


def test_resources_not_added_from_incoming_properties():
    """When current properties have no resources, these should not be added from
    incoming properties."""
    properties_updates = PackageProperties(resources=[ResourceProperties()])

    # To make clear what this is.
    current_properties = test_properties
    updated_properties = update_package_properties(
        current_properties, properties_updates
    )

    assert updated_properties == current_properties


@mark.parametrize(
    "properties_updates",
    [
        PackageProperties(),
        PackageProperties(resources=[ResourceProperties()]),
    ],
)
def test_current_resources_not_modified(properties_updates):
    """When current properties have resources, these should not be modified."""
    current_properties = replace(
        test_properties,
        resources=[
            ResourceProperties(
                name="resource-1",
                path=str(Path("resources", "1", "data.parquet")),
                title="Resource 1",
                description="A resource.",
            )
        ],
    )
    updated_properties = update_package_properties(
        current_properties, properties_updates
    )

    assert updated_properties == current_properties


def test_error_for_empty_properties():
    """If current properties is empty, there should be an error."""
    with raises(ExceptionGroup):
        update_package_properties(PackageProperties(), test_properties)
