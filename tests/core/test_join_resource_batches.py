import polars as pl
from polars.testing import assert_frame_equal
from pytest import fixture

from seedcase_sprout.core.constants import BATCH_TIMESTAMP_COLUMN_NAME
from seedcase_sprout.core.examples import example_resource_properties
from seedcase_sprout.core.join_resource_batches import join_resource_batches
from seedcase_sprout.core.properties import (
    ResourceProperties,
)


@fixture
def data_list() -> list[pl.DataFrame]:
    return [
        pl.DataFrame(
            {
                "id": [0, 1],
                "name": ["anne", "belinda"],
                "value": [0.0, 1.1],
                # timestamp col from `read_resource_batches`
                BATCH_TIMESTAMP_COLUMN_NAME: ["2025-03-26T100000Z"] * 2,
            }
        ),
        pl.DataFrame(
            {
                "id": [2, 3, 0, 0, 0],
                "name": ["catherine", "dorothy", "anne", "anne", "alberta"],
                "value": [2.2, 3.3, 0.0, 9.9, 0.0],
                # timestamp col from `read_resource_batches` (different year than above)
                BATCH_TIMESTAMP_COLUMN_NAME: ["2024-03-26T100000Z"] * 5,
            }
        ),
    ]


@fixture
def resource_properties() -> ResourceProperties:
    """Fixture for resource_properties."""
    return example_resource_properties()


def test_batches_are_joined_correctly(data_list, resource_properties):
    """Test that the batches are joined correctly."""
    # Given
    resource_properties.schema.primary_key = ["id"]

    # When
    joined_batches = join_resource_batches(
        data_list=data_list,
        resource_properties=resource_properties,
    )

    # Then
    expected_joined_batches = pl.DataFrame(
        {
            # only one row with id 0 is kept, the latest one (it is unique in terms of
            # id, ignoring timestamp)
            "id": [1, 2, 3, 0],
            "name": ["belinda", "catherine", "dorothy", "anne"],
            "value": [1.1, 2.2, 3.3, 0.0],
        }
    )

    assert_frame_equal(
        joined_batches,
        expected_joined_batches,
        check_row_order=False,
    )


def test_batches_are_joined_correct_with_no_primary_key(data_list, resource_properties):
    """Duplicate rows (all cells are identical except timestamp) are removed when there
    isn't a primary key."""
    # Given
    resource_properties.schema.primary_key = None

    # When
    joined_batches = join_resource_batches(
        data_list=data_list,
        resource_properties=resource_properties,
    )
    # Then
    expected_joined_batches = pl.DataFrame(
        {
            # three rows with id 0 are kept (they are unique, ignoring timestamp)
            "id": [1, 2, 3, 0, 0, 0],
            "name": [
                "belinda",
                "catherine",
                "dorothy",
                "anne",
                "anne",
                "alberta",
            ],
            "value": [1.1, 2.2, 3.3, 0.0, 9.9, 0.0],
        }
    )

    assert_frame_equal(
        joined_batches,
        expected_joined_batches,
        check_row_order=False,
    )


def test_batches_joined_correctly_when_primary_key_is_multiple_fields(
    data_list, resource_properties
):
    """Batches are joined correctly when the primary key is multiple fields."""
    # Given
    resource_properties.schema.primary_key = ["id", "value"]

    # When
    joined_batches = join_resource_batches(
        data_list=data_list,
        resource_properties=resource_properties,
    )
    # Then
    expected_joined_batches = pl.DataFrame(
        {
            # two rows with id 0 are kept (they are unique in terms of id and value,
            # ignoring timestamp)
            "id": [1, 2, 3, 0, 0],
            "name": [
                "belinda",
                "catherine",
                "dorothy",
                "anne",
                "anne",
            ],
            "value": [1.1, 2.2, 3.3, 0.0, 9.9],
        }
    )

    assert_frame_equal(joined_batches, expected_joined_batches, check_row_order=False)
