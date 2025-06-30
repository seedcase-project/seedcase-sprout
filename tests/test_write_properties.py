from pathlib import Path

from pytest import fixture, raises

from seedcase_sprout.examples import (
    example_package_properties,
    example_resource_properties,
)
from seedcase_sprout.internals import _read_json, _write_json
from seedcase_sprout.paths import PackagePath
from seedcase_sprout.properties import (
    PackageProperties,
)
from seedcase_sprout.write_properties import write_properties


@fixture
def properties() -> PackageProperties:
    properties = example_package_properties()
    properties.resources = [example_resource_properties()]
    return properties


@fixture
def path(tmp_path: Path) -> Path:
    return tmp_path / "datapackage.json"


def assert_file_contains(path: Path, expected_properties: PackageProperties) -> None:
    new_properties = _read_json(path)
    assert new_properties == expected_properties.compact_dict


def test_writes_properties_when_file_does_not_exist(path, properties):
    """Should write properties to file when the file doesn't yet exist."""
    assert write_properties(properties, path) == path
    assert_file_contains(path, properties)


def test_overwrites_properties_when_file_exists(path, properties):
    """Should overwrite properties when the file already exists"""
    old_properties = properties.compact_dict | {
        "name": "old-name",
        "resources": [{"name": "old-resource-name"}, {"name": "another-old-resource"}],
    }
    _write_json(old_properties, path)

    assert write_properties(properties, path) == path
    assert_file_contains(path, properties)


def test_writes_properties_using_utf8(path, properties):
    """Should write properties to file using UTF-8."""
    properties.description = (
        "Håkan Ørsted's favourite letters: æ ø å Æ Ø Å é μῆνιν ἄειδε θεὰ"
    )

    write_properties(properties, path)

    assert properties.description in path.read_bytes().decode("utf-8")


def test_throws_error_if_error_in_package_properties(path, properties):
    """Should throw `CheckError`s if there are errors in the package properties."""
    properties.id = None

    with raises(ExceptionGroup):
        write_properties(properties, path)


def test_throws_error_if_error_in_resource_properties(path, properties):
    """Should throw `CheckError`s if there are errors in the resource properties."""
    properties.resources[0].name = "invalid name with spaces"

    with raises(ExceptionGroup):
        write_properties(properties, path)


def test_writes_properties_to_cwd_if_no_path_provided(tmp_cwd, properties):
    """If no path is provided, should use datapackage.json in the cwd."""
    assert write_properties(properties) == PackagePath(tmp_cwd).properties()
