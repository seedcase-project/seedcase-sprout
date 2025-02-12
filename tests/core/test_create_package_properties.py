from pytest import raises

from seedcase_sprout.core import (
    ContributorProperties,
    LicenseProperties,
    PackageProperties,
)
from seedcase_sprout.core.create_package_properties import create_package_properties
from seedcase_sprout.core.read_json import read_json

package_properties = PackageProperties(
    name="test-package",
    title="Test of data package",
    description="Data for a test data package.",
    contributors=[
        ContributorProperties(
            title="Luke",
            email="luke@example.com",
            roles=["creator"],
        )
    ],
    licenses=[
        LicenseProperties(
            name="ODC-BY-1.0",
            path="https://opendatacommons.org/licenses/by",
            title="Open Data Commons Attribution License 1.0",
        )
    ],
)


def test_creates_folder_and_file_correctly(tmp_path):
    """Given a path, should create the correct folder and file."""
    # given
    expected_package_path = tmp_path / "test-package"
    expected_properties_path = expected_package_path / "datapackage.json"

    # when
    path = create_package_properties(package_properties, tmp_path)

    # then
    assert len(list(tmp_path.iterdir())) == 1
    assert expected_package_path.is_dir()
    assert len(list(expected_package_path.iterdir())) == 1
    assert path == expected_properties_path
    assert expected_properties_path.is_file()


def test_writes_nonempty_files(tmp_path):
    """The files written should not be empty. The properties file should be parsable as
    JSON."""
    properties_path = create_package_properties(package_properties, tmp_path)

    assert read_json(properties_path)


def test_throws_error_if_path_points_to_file(tmp_path):
    """Raises NotADirectoryError if the input path points to a file."""
    file_path = tmp_path / "datapackage.json"
    file_path.touch()

    with raises(NotADirectoryError):
        create_package_properties(package_properties, file_path)
