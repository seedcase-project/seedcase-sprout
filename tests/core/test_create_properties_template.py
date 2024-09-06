import json

from pytest import raises

from sprout.core.create_properties_template import create_properties_template
from sprout.core.verify_package_properties import PACKAGE_REQUIRED_PROPERTIES
from sprout.core.verify_resource_properties import RESOURCE_REQUIRED_PROPERTIES


def test_writes_template_to_file_correctly(tmp_path):
    """Given a file path, should create a file with the expected contents in JSON format
    and return the file path."""
    # given
    file_path_in = tmp_path / "test.test"

    # when
    file_path_out = create_properties_template(file_path_in)

    # then
    assert file_path_out == file_path_in
    assert file_path_out.is_file()

    package = json.loads(file_path_out.read_text())
    assert set(package.keys()) == PACKAGE_REQUIRED_PROPERTIES

    assert package["resources"]
    resource = package["resources"][0]
    assert set(resource.keys()) == RESOURCE_REQUIRED_PROPERTIES


def test_rejects_unresolvable_path(tmp_path):
    """Given a path with a nonexistent parent, should throw FileNotFoundError."""
    with raises(FileNotFoundError):
        create_properties_template(tmp_path / "nonexistent" / "test.test")
