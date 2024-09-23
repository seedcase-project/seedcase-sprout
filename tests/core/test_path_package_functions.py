from pathlib import Path
from re import escape

from pytest import fixture, mark, raises

from sprout.core.path_package_functions import (
    path_package,
    path_package_database,
    path_package_properties,
    path_packages,
)
from tests.core.path_function_test_utils import (
    create_test_package_structure,
)


# Given one package
@fixture
def tmp_sprout_root(monkeypatch, tmp_path):
    """Set up test package folder structure and return temp root directory"""
    SPROUT_ROOT = str(tmp_path)
    monkeypatch.setenv("SPROUT_ROOT", SPROUT_ROOT)
    create_test_package_structure(tmp_path, "1")

    return SPROUT_ROOT


@mark.parametrize(
    "function, expected_path",
    [
        (path_package, "packages/1"),
        (path_package_database, "packages/1/database.sql"),
        (path_package_properties, "packages/1/datapackage.json"),
    ],
)
def test_path_package_functions_return_expected_path(
    tmp_sprout_root, function, expected_path
):
    # When, then
    assert function(package_id=1) == Path(tmp_sprout_root) / expected_path


@mark.parametrize(
    "function, expected_exception",
    [
        (path_package, NotADirectoryError),
        (path_package_database, FileNotFoundError),
        (path_package_properties, FileNotFoundError),
    ],
)
def test_path_package_functions_raise_error_if_package_id_does_not_exist(
    tmp_sprout_root, function, expected_exception
):
    # When, then
    with raises(expected_exception, match=escape("[1]")):
        function(package_id=2)


def test_path_packages_returns_expected_path(tmp_sprout_root):
    # When, then
    assert path_packages() == Path(tmp_sprout_root) / "packages"


def test_path_packages_raises_error_when_no_packages_exist():
    # When, then
    with raises(NotADirectoryError):
        path_packages()
