import re

import polars as pl
from polars.testing import assert_frame_equal
from pytest import raises

from seedcase_sprout.core.constants import BATCH_TIMESTAMP_PATTERN
from seedcase_sprout.core.examples import (
    example_data,
    example_resource_properties,
)
from seedcase_sprout.core.write_resource_batch import write_resource_batch


def test_writes_correct_resource_batch_file(tmp_path):
    """Writes tidy resource batch file correctly."""
    # Given
    (tmp_path / "resources" / example_resource_properties().name).mkdir(parents=True)

    # When
    batch_path = write_resource_batch(
        example_data(), example_resource_properties(), tmp_path
    )
    batch_data = pl.read_parquet(batch_path)

    # Then
    assert batch_path.exists()
    assert f"resources/{example_resource_properties().name}/batch" in str(batch_path)
    assert len(re.findall(BATCH_TIMESTAMP_PATTERN, batch_path.stem)) == 1
    assert_frame_equal(batch_data, example_data(), check_exact=True)


def test_writes_correct_resource_batch_file_with_unordered_columns(tmp_path):
    """Writes batch file correctly even if columns aren't in the order expected by the
    resource properties."""
    # Given
    (tmp_path / "resources" / example_resource_properties().name).mkdir(parents=True)
    data = example_data().select(["value", "name", "id"])

    # When
    batch_path = write_resource_batch(data, example_resource_properties(), tmp_path)
    batch_data = pl.read_parquet(batch_path)

    # Then
    assert batch_path.exists()
    assert_frame_equal(batch_data, data, check_exact=True)


def test_throws_error_if_data_do_not_match_example_resource_properties(tmp_path):
    """Throws ValueError if data don't match resource properties."""
    with raises(ValueError):
        write_resource_batch(pl.DataFrame(), example_resource_properties(), tmp_path)
