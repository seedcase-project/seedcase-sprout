from json import JSONDecodeError
from pathlib import Path

from pytest import raises

from seedcase_sprout.core.example_package_properties import example_package_properties
from seedcase_sprout.core.read_properties import read_properties
from seedcase_sprout.core.write_package_properties import write_package_properties


def test_reads_in_as_package_properties(tmp_path):
    """Should read in the properties from the `datapackage.json` file."""

    properties = example_package_properties()
    properties_path = tmp_path / "datapackage.json"
    properties_path = write_package_properties(properties_path, properties)
    properties = read_properties(properties_path)

    assert properties == properties


def test_throws_error_if_path_points_to_dir(tmp_path):
    """Should throw FileNotFoundError if the path points to a folder."""
    with raises(FileNotFoundError):
        read_properties(tmp_path)


def test_throws_error_if_path_points_to_nonexistent_file(tmp_path):
    """Should throw FileNotFoundError if the path points to a nonexistent file."""
    with raises(FileNotFoundError):
        read_properties(tmp_path / "datapackage.json")


def test_throws_error_if_properties_file_cannot_be_read(tmp_path):
    """Should throw JSONDecodeError if the properties file cannot be read as JSON."""
    file_path = Path(tmp_path / "datapackage.json")
    file_path.write_text(",,, this is not, JSON")

    with raises(JSONDecodeError):
        read_properties(file_path)
