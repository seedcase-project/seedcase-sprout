import os
from pathlib import Path

import polars as pl
from polars.testing import assert_frame_equal
from pytest import fixture, raises

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
    os.chdir(tmp_path)
    (Path("resources") / "1").mkdir(parents=True, exist_ok=True)

    # When
    batch_path = write_resource_batch(tidy_data, resource_properties)
    batch_data = pl.read_parquet(batch_path)

    # Then
    assert batch_path.exists()
    assert assert_frame_equal(batch_data, tidy_data, check_exact=True) is None


def test_throws_error_if_resource_properties_are_incorrect(
    tmp_path, tidy_data, resource_properties
):
    """Throws ExceptionGroup if resources properties are incorrect."""
    # Given
    os.chdir(tmp_path)
    (Path("resources") / "1").mkdir(parents=True, exist_ok=True)
    resource_properties.description = ""

    # When
    with raises(ExceptionGroup):
        write_resource_batch(tidy_data, resource_properties)


def xtest_throws_error_if_data_do_not_match_resource_properties(
    tmp_path, resource_properties
):
    """Throws ExceptionGroup if the data don't match the resource properties."""
    # Given
    os.chdir(tmp_path)
    (Path("resources") / "1").mkdir(parents=True, exist_ok=True)

    # When
    with raises(ExceptionGroup):
        write_resource_batch(pl.DataFrame(), resource_properties)
