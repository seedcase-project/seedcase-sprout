from pathlib import Path

import polars as pl
from pytest import fixture, raises

from seedcase_sprout.core.sprout_checks.check_data_columns import check_data_columns


@fixture
def data_path(tmp_path) -> Path:
    return tmp_path / "data.csv"


def test_no_error_when_columns_correct():
    """The check should pass when no column has only null values."""
    lazy_frame = pl.LazyFrame({"col1": [1, 2, 3], "col2": [None, "b", None]})

    assert check_data_columns(lazy_frame) is lazy_frame


def test_error_when_column_empty():
    """Should raise an error when there is a column with only null values."""
    lazy_frame = pl.LazyFrame({"col1": [1, 2, 3], "col2": [None, None, None]})

    with raises(pl.exceptions.ShapeError, match="col2"):
        check_data_columns(lazy_frame)


def test_error_when_more_data_columns_than_expected(data_path):
    """Should raise an error if the `collect` operation reveals that the lazy frame
    has more columns than described in the schema."""
    data_path.write_text("col1,col2\na,b\nc,d")
    lazy_frame = pl.scan_csv(data_path, has_header=True, schema={"col1": pl.String})

    with raises(pl.exceptions.ShapeError):
        check_data_columns(lazy_frame)


def test_compute_error_rethrown(data_path):
    """`ComputeError`s should be re-raised if not related to the number of columns."""
    data_path.write_text('"Unescaped quote')
    lazy_frame = pl.scan_csv(data_path, has_header=False)

    with raises(pl.exceptions.ComputeError):
        check_data_columns(lazy_frame)
