from pathlib import Path

from pytest import raises

from seedcase_sprout.core.create_batch_file_name import create_batch_file_name
from seedcase_sprout.core.sprout_checks.check_batch_file_name import (
    _check_batch_file_name,
)


def test_file_name_created_by_create_batch_file_name_passes(tmp_path):
    """A batch file name created by `create_batch_file_name` should pass the check."""
    # Given
    batch_file_name = (Path(tmp_path) / _create_batch_file_name()).with_suffix(
        ".parquet"
    )

    # When, Then
    assert check_batch_file_name(batch_file_name) == batch_file_name


def test_file_name_that_does_not_fit_the_expected_format_fails(tmp_path):
    """A batch file name that doesn't fit the expected format should fail the check."""
    # Given
    batch_file_name = (Path(tmp_path) / "data").with_suffix(".parquet")

    # When, Then
    with raises(ValueError):
        _check_batch_file_name(batch_file_name)
