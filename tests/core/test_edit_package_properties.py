from json import JSONDecodeError
from pathlib import Path

from pytest import mark, raises

from seedcase_sprout.core.edit_package_properties import edit_package_properties
from seedcase_sprout.core.properties import (
    LicenseProperties,
    PackageProperties,
    ResourceProperties,
)
from seedcase_sprout.core.write_json import write_json

full_properties = PackageProperties(
    name="my-package",
    id="123-abc-123",
    title="My Package",
    description="This is my package.",
    version="1.0.0",
    created="2024-05-14T05:00:01+00:00",
    licenses=[LicenseProperties(name="license")],
).compact_dict


def get_properties_path(tmp_path: Path, package_properties: dict) -> Path:
    return write_json(package_properties, tmp_path / "datapackage.json")


@mark.parametrize(
    "properties",
    [
        PackageProperties().compact_dict,
        PackageProperties(name="my-new-package-name").compact_dict,
        full_properties,
    ],
)
def test_edits_only_changed_package_properties(tmp_path, properties):
    """Should only edit package properties and leave unchanged values as is."""
    properties_path = get_properties_path(tmp_path, full_properties)

    new_properties = edit_package_properties(properties_path, properties)

    assert new_properties == full_properties | properties


@mark.parametrize(
    "current_properties",
    [
        PackageProperties().compact_dict,
        PackageProperties(name="my-incomplete-package").compact_dict,
    ],
)
def test_edits_incomplete_package_properties(tmp_path, current_properties):
    """Should edit properties that are incomplete before being edited."""
    properties_path = get_properties_path(tmp_path, current_properties)

    new_properties = edit_package_properties(properties_path, full_properties)

    assert new_properties == full_properties


def test_adds_custom_fields(tmp_path):
    """Should add custom fields to properties."""
    properties_path = get_properties_path(tmp_path, full_properties)
    properties = {"custom": "field"}

    new_properties = edit_package_properties(properties_path, properties)

    assert new_properties == full_properties | properties


def test_resources_not_added_from_incoming_properties(tmp_path):
    """When current properties have no resources, these should not be added from
    incoming properties."""
    properties_path = get_properties_path(tmp_path, full_properties)
    properties = PackageProperties(resources=[ResourceProperties()]).compact_dict

    new_properties = edit_package_properties(properties_path, properties)

    assert new_properties == full_properties


@mark.parametrize(
    "properties",
    [
        PackageProperties().compact_dict,
        PackageProperties(resources=[ResourceProperties()]).compact_dict,
    ],
)
def test_current_resources_not_modified(tmp_path, properties):
    """When current properties have resources, these should not be modified."""
    current_properties = full_properties | {
        "resources": [
            ResourceProperties(
                name="resource-1",
                path=str(Path("resources", "1", "data.parquet")),
                title="Resource 1",
                description="A resource.",
            ).compact_dict
        ]
    }
    properties_path = get_properties_path(tmp_path, current_properties)

    new_properties = edit_package_properties(properties_path, properties)

    assert new_properties == current_properties


def test_throws_error_if_path_points_to_dir(tmp_path):
    """Should throw FileNotFoundError if the path points to a folder."""
    with raises(FileNotFoundError):
        edit_package_properties(tmp_path, {})


def test_throws_error_if_path_points_to_nonexistent_file(tmp_path):
    """Should throw FileNotFoundError if the path points to a nonexistent file."""
    with raises(FileNotFoundError):
        edit_package_properties(tmp_path / "datapackage.json", {})


def test_throws_error_if_properties_file_cannot_be_read(tmp_path):
    """Should throw JSONDecodeError if the properties file cannot be read as JSON."""
    file_path = tmp_path / "datapackage.json"
    file_path.write_text(",,, this is not, JSON")

    with raises(JSONDecodeError):
        edit_package_properties(file_path, full_properties)


def test_throws_error_if_current_properties_have_a_package_error(tmp_path):
    """Should throw a group of `CheckError`s if the current properties have an error
    among the package properties."""
    current_properties = PackageProperties(name="invalid name with spaces").compact_dict
    properties_path = get_properties_path(tmp_path, current_properties)
    properties = PackageProperties(name="my-new-package-name").compact_dict

    with raises(ExceptionGroup) as error_info:
        edit_package_properties(properties_path, properties)

    assert "invalid name with spaces" in error_info.value.message
    errors = error_info.value.exceptions
    assert len(errors) == 1
    assert errors[0].json_path == "$.name"
    assert errors[0].validator == "pattern"


def test_throws_error_if_current_properties_have_a_resource_error(tmp_path):
    """Should throw a group of `CheckError`s if the current properties have an error
    among the resource properties."""
    current_properties = full_properties | {
        "resources": [
            ResourceProperties(
                name="invalid name with spaces",
                path=str(Path("resources", "1", "data.parquet")),
                title="Resource 1",
                description="A resource.",
            ).compact_dict
        ]
    }
    properties_path = get_properties_path(tmp_path, current_properties)
    properties = PackageProperties(name="my-new-package-name").compact_dict

    with raises(ExceptionGroup) as error_info:
        edit_package_properties(properties_path, properties)

    assert "my-package" in error_info.value.message
    assert "invalid name with spaces" in error_info.value.message
    errors = error_info.value.exceptions
    assert len(errors) == 1
    assert errors[0].json_path == "$.resources[0].name"
    assert errors[0].validator == "pattern"


def test_throws_error_if_incoming_package_properties_are_malformed(tmp_path):
    """Should throw a group of `CheckError`s if the incoming package properties are
    malformed."""
    properties_path = get_properties_path(tmp_path, full_properties)
    properties = PackageProperties(name="a name with spaces").compact_dict

    with raises(ExceptionGroup) as error_info:
        edit_package_properties(properties_path, properties)

    assert "a name with spaces" in error_info.value.message
    errors = error_info.value.exceptions
    assert len(errors) == 1
    assert errors[0].json_path == "$.name"
    assert errors[0].validator == "pattern"


def test_throws_error_if_resulting_properties_are_incomplete(tmp_path):
    """Should throw a group of `CheckError`s if the resulting properties have missing
    required fields."""
    current_properties = PackageProperties(name="my-incomplete-package").compact_dict
    properties_path = get_properties_path(tmp_path, current_properties)
    properties = PackageProperties(title="My Incomplete Package").compact_dict

    with raises(ExceptionGroup) as error_info:
        edit_package_properties(properties_path, properties)

    message = error_info.value.message
    assert "my-incomplete-package" in message
    assert "My Incomplete Package" in message
    errors = error_info.value.exceptions
    assert len(errors) == 5
    assert all(error.validator == "required" for error in errors)


def test_throws_error_if_both_current_and_incoming_properties_empty(tmp_path):
    """Should throw a group of `CheckError`s if both current and incoming properties are
    empty."""
    properties_path = get_properties_path(tmp_path, {})

    with raises(ExceptionGroup) as error_info:
        edit_package_properties(properties_path, {})

    assert "{}" in error_info.value.message
    errors = error_info.value.exceptions
    assert len(errors) == 7
    assert all(error.validator == "required" for error in errors)
