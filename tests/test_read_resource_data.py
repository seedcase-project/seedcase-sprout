import polars as pl
from pytest import raises

from seedcase_sprout import ExamplePackage, example_data, read_resource_data


def test_read_resource_data():
    """Very basic check that it runs."""
    with ExamplePackage():
        data = read_resource_data("example-resource")
        assert isinstance(data, pl.DataFrame)
        assert data.shape == example_data().shape


def test_read_resource_data_with_package_path():
    """Check how it works when given a path."""
    with ExamplePackage() as package_path:
        data = read_resource_data("example-resource", package_path.root())
        assert isinstance(data, pl.DataFrame)
        assert data.shape == example_data().shape


def test_read_resource_data_with_wrong_resource():
    with raises(FileNotFoundError):
        read_resource_data("wrong-name")
