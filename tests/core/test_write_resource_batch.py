import os
import re
from pathlib import Path

import polars as pl
from polars.testing import assert_frame_equal
from pytest import fixture, raises

from seedcase_sprout.core.constants import BATCH_TIMESTAMP_PATTERN
from seedcase_sprout.core.properties import ResourceProperties
from seedcase_sprout.core.write_resource_batch import write_resource_batch


@fixture
def tidy_data() -> pl.DataFrame:
    return pl.DataFrame(
        {
            "id": [0, 1, 2],
            "name": ["anne", "belinda", "catherine"],
        }
    )


@fixture
def resource_properties() -> ResourceProperties:
    return ResourceProperties(
        name="test-resource",
        title="Test Resource",
        description="Description of resource",
        path=str(Path("resources") / "1" / "data.parquet"),
    )


def test_writes_correct_resource_batch_file(tmp_path, tidy_data, resource_properties):
    """Writes tidy resource batch file correctly."""
    # Given
    (tmp_path / "resources" / resource_properties.name).mkdir(parents=True)

    # When
    batch_path = write_resource_batch(tidy_data, resource_properties, tmp_path)
    batch_data = pl.read_parquet(batch_path)

    # Then
    assert batch_path.exists()
    assert f"resources/{resource_properties.name}/batch" in str(batch_path)
    assert len(re.findall(BATCH_TIMESTAMP_PATTERN, batch_path.stem)) == 1
    assert_frame_equal(batch_data, tidy_data, check_exact=True)


def test_writes_correct_resource_batch_file_with_unordered_columns(
    tmp_path, tidy_data, resource_properties
):
    """Writes batch file correctly even if columns aren't in the order expected by the
    resource properties."""
    # Given
    (tmp_path / "resources" / resource_properties.name).mkdir(parents=True)
    tidy_data = tidy_data.select(["name", "id"])

    # When
    batch_path = write_resource_batch(tidy_data, resource_properties, tmp_path)
    batch_data = pl.read_parquet(batch_path)

    # Then
    assert batch_path.exists()
    assert_frame_equal(batch_data, tidy_data, check_exact=True)


def test_throws_error_if_resource_properties_are_incorrect(
    tmp_path, tidy_data, resource_properties
):
    """Throws ExceptionGroup if resources properties are incorrect."""
    # Given
    os.chdir(tmp_path)
    (tmp_path / "resources" / resource_properties.name).mkdir(parents=True)
    resource_properties.description = ""

    # When
    with raises(ExceptionGroup):
        write_resource_batch(tidy_data, resource_properties, tmp_path)


def xtest_throws_error_if_data_do_not_match_resource_properties(
    tmp_path, tidy_data, resource_properties
):
    """Throws ExceptionGroup if data don't match resource properties (extra column)."""
    # Given
    os.chdir(tmp_path)
    (tmp_path / "resources" / resource_properties.name).mkdir(parents=True)

    tidy_data.insert_column(2, pl.Series("extra_column", [1, 2, 3]))

    # When
    # TODO: What type of error will `check_data()` raise?
    with raises(ExceptionGroup):
        write_resource_batch(pl.DataFrame(), resource_properties, tmp_path)
