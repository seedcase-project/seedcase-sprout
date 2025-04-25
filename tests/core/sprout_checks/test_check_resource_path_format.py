from pathlib import Path

from pytest import mark

from seedcase_sprout.core.sprout_checks.check_resource_path_format import (
    check_resource_path_format,
)
from seedcase_sprout.core.sprout_checks.get_json_path_to_resource_field import (
    get_json_path_to_resource_field,
)


@mark.parametrize("index", [None, 2])
def test_passes_if_data_path_well_formed(index):
    """Should pass if the path contains the resource name."""
    properties = {
        "name": "test",
        "path": str(Path("resources", "test", "data.parquet")),
    }

    assert check_resource_path_format(properties, index) == []


@mark.parametrize("index", [None, 2])
@mark.parametrize("name", [None, "", 123, "with spaces"])
def test_passes_if_name_incorrect(index, name):
    """Should pass with any path if the name is not correct."""
    assert check_resource_path_format({"name": name, "path": "bad/path"}, index) == []


@mark.parametrize("index", [None, 2])
def test_passes_if_data_path_not_present(index):
    """Should pass if the path is not set."""
    assert check_resource_path_format({"name": "test"}, index) == []


@mark.parametrize("index", [None, 2])
@mark.parametrize("data_path", [123, []])
def test_passes_if_path_of_wrong_type(index, data_path):
    """Should pass if path is of the wrong type."""
    properties = {"name": "test", "path": data_path}

    assert check_resource_path_format(properties, index) == []


@mark.parametrize("index", [None, 2])
@mark.parametrize(
    "data_path",
    [
        Path("resources", "x", "data.parquet"),
        Path("test", "data.parquet"),
        Path("resources", "test", "data.parquet", "test"),
    ],
)
def test_returns_error_if_data_path_is_malformed(index, data_path):
    """Returns list of `CheckError`s if the data path has the wrong format."""
    properties = {"path": str(data_path), "name": "test"}

    errors = check_resource_path_format(properties, index)

    assert len(errors) == 1
    assert errors[0].message
    assert errors[0].json_path == get_json_path_to_resource_field("path", index)
    assert errors[0].validator == "pattern"
