from pathlib import Path
from re import escape

from pytest import fixture, mark, raises

from sprout.core.path_resource_functions import (
    path_resource,
    path_resource_data,
    path_resource_raw,
    path_resource_raw_files,
    path_resources,
)
from tests.core.path_test_utils import (
    create_test_package_structure,
    create_test_resource_structure,
)


# Given a package with two resources
@fixture
def tmp_sprout_root(monkeypatch, tmp_path):
    """Set up test package folder structure return temp root directory"""
    SPROUT_ROOT = str(tmp_path)
    monkeypatch.setenv("SPROUT_ROOT", SPROUT_ROOT)

    path_package_1 = create_test_package_structure(tmp_path, "1")
    create_test_resource_structure(path_package_1, "1", ["raw_file_1.csv.gz"])
    create_test_resource_structure(
        path_package_1, "2", ["raw_file_2.csv.gz", "raw_file_3.csv.gz"]
    )

    return SPROUT_ROOT


@mark.parametrize(
    "function, expected_path",
    [
        (path_resource, "packages/1/resources/2"),
        (path_resource_data, "packages/1/resources/2/data.parquet"),
        (path_resource_raw, "packages/1/resources/2/raw"),
    ],
)
def test_path_resource_functions_return_expected_path(
    tmp_sprout_root, function, expected_path
):
    # When, then
    assert (
        function(package_id=1, resource_id=2) == Path(tmp_sprout_root) / expected_path
    )


def test_path_resources_returns_expected_path(tmp_sprout_root):
    # When, then
    assert (
        path_resources(package_id=1)
        == Path(tmp_sprout_root) / "packages" / "1" / "resources"
    )


def test_path_resource_raw_files_returns_expected_list_of_paths(tmp_sprout_root):
    # When
    resource_raw_path = (
        Path(tmp_sprout_root) / "packages" / "1" / "resources" / "2" / "raw"
    )
    # Then
    assert set(path_resource_raw_files(package_id=1, resource_id=2)) == set(
        [
            resource_raw_path / "raw_file_2.csv.gz",
            resource_raw_path / "raw_file_3.csv.gz",
        ]
    )


@mark.parametrize(
    "function, expected_exception",
    [
        (path_resource, NotADirectoryError),
        (path_resource_data, FileNotFoundError),
        (path_resource_raw, NotADirectoryError),
        (path_resource_raw_files, NotADirectoryError),
    ],
)
def test_path_resource_functions_raise_error_if_res_id_does_not_exist(
    tmp_sprout_root, function, expected_exception
):
    """Raises error if package ID exists but resource ID does not"""
    # When, then
    with raises(expected_exception, match=escape("[1, 2]")):
        function(package_id=1, resource_id=3)


@mark.parametrize(
    "function, expected_exception",
    [
        (path_resource, NotADirectoryError),
        (path_resource_data, FileNotFoundError),
        (path_resource_raw, NotADirectoryError),
        (path_resource_raw_files, NotADirectoryError),
    ],
)
def test_raises_error_if_package_id_does_not_exist(
    tmp_sprout_root, function, expected_exception
):
    """Raises error if package ID doesn't exist but resource ID does
    in another package"""
    # When, then
    with raises(expected_exception, match=escape("[]")):
        function(package_id=2, resource_id=1)


def test_path_resources_raises_error_when_package_does_not_exist(tmp_sprout_root):
    # When, then
    with raises(NotADirectoryError, match=escape("[1]")):
        path_resources(package_id=2)
