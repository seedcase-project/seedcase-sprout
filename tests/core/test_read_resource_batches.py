from pathlib import Path
from uuid import uuid4

import polars as pl
from pytest import fixture, mark, raises

from seedcase_sprout.core.constants import BATCH_TIMESTAMP_COLUMN_NAME
from seedcase_sprout.core.properties import (
    FieldProperties,
    ResourceProperties,
    TableSchemaProperties,
)
from seedcase_sprout.core.read_resource_batches import (
    read_resource_batches,
)
from tests.core.assert_raises_errors import (
    assert_raises_check_errors,
)
from tests.core.directory_structure_setup import (
    create_test_data_package,
)

batch_data_1 = pl.DataFrame(
    {
        "id": [0, 1, 2],
        "name": ["anne", "belinda", "catherine"],
    }
)

batch_data_2 = pl.DataFrame(
    {
        "id": [3, 4, 5],
        "name": ["dorothy", "figaro", "gabrielle"],
    }
)

resource_properties = ResourceProperties(
    name="test-resource",
    path=str(Path("resources", "1", "data.parquet")),
    title="Test resource",
    description="A test resource",
    schema=TableSchemaProperties(
        [
            FieldProperties(name="id", type="integer"),
            FieldProperties(name="name", type="string"),
        ]
    ),
)


@fixture
def test_package(tmp_path):
    # TODO: Switch to using examples
    create_test_data_package(tmp_path)
    batch_path = tmp_path / "resources" / "1" / "batch"
    batch_path.mkdir(parents=True)

    for batch_data in [batch_data_1, batch_data_2]:
        batch_data.write_parquet(
            Path(batch_path / f"2025-03-26T100346Z-{uuid4()}").with_suffix(".parquet")
        )

    return tmp_path


@fixture
def resource_paths(test_package):
    return list((test_package / "resources" / "1" / "batch").iterdir())


def test_reads_resource_batches_correctly(resource_paths):
    """Reads the resource batches correctly with the expected timestamp column."""
    # Given, When
    data_list = read_resource_batches(
        paths=resource_paths, resource_properties=resource_properties
    )
    timestamp_column = [
        data_list[0][BATCH_TIMESTAMP_COLUMN_NAME],
        data_list[1][BATCH_TIMESTAMP_COLUMN_NAME],
    ]

    # Then
    assert len(data_list) == 2
    assert all(data.shape == (3, 3) for data in data_list)
    assert all(len(column.unique()) == 1 for column in timestamp_column)
    assert all(
        column.unique()[0] == "2025-03-26T100346Z" for column in timestamp_column
    )


def test_raises_error_when_file_does_not_exist(resource_paths):
    """Raises FileNotFoundError when a file in the list of paths doesn't exist"""
    # Given
    resource_paths.append(Path("non-existent-file.parquet"))

    # When, Then
    with raises(FileNotFoundError):
        read_resource_batches(
            paths=resource_paths, resource_properties=resource_properties
        )


def test_raises_error_when_timestamp_column_matches_existing_column(resource_paths):
    """Raises ValueError when the timestamp column name matches an existing column."""
    # Given
    batch_path = resource_paths[0].parent

    batch_data = pl.DataFrame(
        {
            "id": [0, 1, 2],
            BATCH_TIMESTAMP_COLUMN_NAME: ["2024-03-26T100346Z"] * 3,
        }
    )
    batch_path = Path(batch_path) / f"2025-03-26T100346Z-{uuid4()}.parquet"
    batch_data.write_parquet(batch_path)

    # When, Then
    with raises(ValueError):
        read_resource_batches(
            paths=[batch_path], resource_properties=resource_properties
        )


@mark.parametrize(
    "incorrect_timestamp",
    [
        "2025-55-26T100346Z",  # incorrect month
        "2025-02-30T100346",  # no timezone
        "2025-03-26T100346",  # incorrect date (30 February)
        "2025-03-26",  # no time
        "T100346Z",  # no date
    ],
)
def test_raises_error_when_file_name_timestamp_does_not_match_pattern(
    resource_paths, incorrect_timestamp
):
    """Raises ValueError when the batch file name is not in the expected pattern."""
    # Given
    batch_path = resource_paths[0].parent
    batch_file_path = Path(batch_path) / f"{incorrect_timestamp}-{uuid4()}.parquet"
    batch_data_1.write_parquet(batch_file_path)

    # When, Then
    with raises(ValueError):
        read_resource_batches(
            paths=[batch_file_path], resource_properties=resource_properties
        )


def test_if_multiple_correct_timestamps_in_file_name_use_first_one(resource_paths):
    """If multiple timestamps are found in the file name, the first one is used."""
    # Given
    batch_path = resource_paths[0].parent
    batch_file_path = (
        Path(batch_path) / f"2025-03-26T100346Z-1990-03-26T100346Z-{uuid4()}.parquet"
    )
    batch_data_1.write_parquet(batch_file_path)

    # When
    data_list = read_resource_batches(
        paths=[batch_file_path], resource_properties=resource_properties
    )

    # Then
    assert data_list[0][BATCH_TIMESTAMP_COLUMN_NAME][0] == "2025-03-26T100346Z"


def test_raises_error_when_properties_do_not_match_data(resource_paths):
    """Raises errors from checks when the resource properties don't match the data."""
    # Given
    resource_properties.schema.fields[0].name = "not-id"

    # When, Then
    with raises(ValueError):
        read_resource_batches(
            paths=resource_paths, resource_properties=resource_properties
        )


def test_raises_error_with_empty_resource_properties(resource_paths):
    """Raises errors from checks if the resource properties are empty."""
    # When, Then
    assert_raises_check_errors(
        lambda: read_resource_batches(
            paths=resource_paths, resource_properties=ResourceProperties()
        )
    )
