from json import JSONDecodeError
from pathlib import Path

from pytest import fixture, raises

from sprout.core.create_relative_resource_data_path import (
    create_relative_resource_data_path,
)
from sprout.core.not_properties_error import NotPropertiesError
from sprout.core.properties import PackageProperties, ResourceProperties
from sprout.core.read_json import read_json
from sprout.core.write_json import write_json
from sprout.core.write_resource_properties import write_resource_properties


def create_data_path(resource_id: int) -> str:
    return str(create_relative_resource_data_path(Path("resources", str(resource_id))))


@fixture
def resource_properties_1() -> ResourceProperties:
    return ResourceProperties(
        name="resource-1",
        path=create_data_path(1),
        title="My First Resource",
        description="This is my first resource.",
    )


@fixture
def resource_properties_2() -> ResourceProperties:
    return ResourceProperties(
        name="resource-2",
        path=create_data_path(2),
        title="My Second Resource",
        description="This is my second resource.",
    )


@fixture
def package_properties_path(
    tmp_path, resource_properties_1, resource_properties_2
) -> Path:
    package_properties = PackageProperties(
        name="my-package",
        id="123-abc-123",
        title="My Package",
        description="This is my package.",
        version="2.0.0",
        created="2024-05-14T05:00:01+00:00",
        resources=[resource_properties_1, resource_properties_2],
    )
    return write_json(package_properties.asdict, tmp_path / "datapackage.json")


def test_updates_existing_resource_in_package(
    package_properties_path, resource_properties_2
):
    """Given a package with a resource having the same ID, should update the properties
    of this resource."""
    # given
    new_resource_properties = ResourceProperties(
        name="resource-1",
        path=create_data_path(1),
        title="My New Title",
        description="This is my updated resource.",
    )
    expected_resources = [new_resource_properties.asdict, resource_properties_2.asdict]

    # when
    path = write_resource_properties(
        package_properties_path, new_resource_properties.asdict
    )

    # then
    assert path == package_properties_path
    assert len(list(path.parent.iterdir())) == 1
    assert read_json(path)["resources"] == expected_resources


def test_adds_new_resource_to_package(
    package_properties_path, resource_properties_1, resource_properties_2
):
    """Given a package without a resource with a matching ID, should add a new set of
    resource properties."""
    # given
    resource_properties_3 = ResourceProperties(
        name="resource-3",
        path=create_data_path(3),
        title="My Third Resource",
        description="This is my third resource.",
    )
    expected_resources = [
        resource_properties_1.asdict,
        resource_properties_2.asdict,
        resource_properties_3.asdict,
    ]

    # when
    path = write_resource_properties(
        package_properties_path, resource_properties_3.asdict
    )

    # then
    assert path == package_properties_path
    assert len(list(path.parent.iterdir())) == 1
    assert read_json(path)["resources"] == expected_resources


def test_throws_error_if_path_points_to_dir(tmp_path):
    """Should throw FileNotFoundError if the path points to a folder."""
    with raises(FileNotFoundError):
        write_resource_properties(tmp_path, {})


def test_throws_error_if_path_points_to_nonexistent_file(tmp_path):
    """Should throw FileNotFoundError if the path points to a nonexistent file."""
    with raises(FileNotFoundError):
        write_resource_properties(tmp_path / "datapackage.json", {})


def test_throws_error_if_properties_file_cannot_be_read(
    tmp_path, resource_properties_1
):
    """Should throw JSONDecodeError if the properties file cannot be read as JSON."""
    file_path = tmp_path / "datapackage.json"
    file_path.write_text(",,, this is not, JSON")

    with raises(JSONDecodeError):
        write_resource_properties(file_path, resource_properties_1.asdict)


def test_throws_error_if_resource_properties_incorrect(package_properties_path):
    """Should throw NotPropertiesError if the resource properties are incorrect."""
    with raises(NotPropertiesError):
        write_resource_properties(package_properties_path, {})


def test_throws_error_if_data_path_malformed(
    package_properties_path, resource_properties_1
):
    """Should throw NotPropertiesError if the data path of the resource is
    malformed."""
    resource_properties_1.path = str(Path("no", "id"))

    with raises(NotPropertiesError):
        write_resource_properties(package_properties_path, resource_properties_1.asdict)


def test_throws_error_if_package_properties_incorrect(tmp_path, resource_properties_1):
    """Should throw NotPropertiesError if the package properties are incorrect."""
    path = write_json({}, tmp_path / "datapackage.json")

    with raises(NotPropertiesError):
        write_resource_properties(path, resource_properties_1.asdict)
