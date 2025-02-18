from pathlib import Path

import polars as pl
from pytest import fixture, mark, raises

from seedcase_sprout.core.sprout_checks.check_data_header import check_data_header


@fixture
def data_path(tmp_path) -> Path:
    return tmp_path / "data.csv"


def test_check_passes_if_columns_match(data_path):
    """Check should pass if the data header matches the expected columns."""
    data_path.write_text("col1,col2,col3\n1,2,3\n")
    expected_columns = ["col1", "col2", "col3"]

    assert check_data_header(data_path, expected_columns) == data_path


@mark.parametrize(
    "data,columns",
    [
        ("col1,col2\n1,2", ["col1", "col2", "col3"]),
        ("col1,col2,col3\n1,2,3", ["col1", "col2"]),
        ("col2,col1\n1,2", ["col1", "col2"]),
    ],
)
def test_error_if_columns_dont_match(data_path, data, columns):
    """Should raise an error if the data header doesn't match the expected columns."""
    data_path.write_text(data)

    with raises(pl.exceptions.ShapeError):
        check_data_header(data_path, columns)
