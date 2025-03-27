from pathlib import Path
from uuid import uuid4

import polars as pl
from pytest import fixture, raises

from seedcase_sprout.core.properties import (
    FieldProperties,
    ResourceProperties,
    TableSchemaProperties,
)
from seedcase_sprout.core.read_resource_batches import (
    read_resource_batches,
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
    data = read_resource_batches(
        paths=resource_paths, resource_properties=resource_properties
    )
    # When
    timestamp_column = [
        data[0]["_batch_file_timestamp_"],
        data[1]["_batch_file_timestamp_"],
    ]

    # Then
    assert len(data) == 2
    assert data[0].shape == (3, 3) and data[1].shape == (3, 3)
    assert (
        timestamp_column[0].name == "_batch_file_timestamp_"
        and timestamp_column[1].name == "_batch_file_timestamp_"
    )
    assert (
        timestamp_column[0].unique()[0] == "2025-03-26T100346Z"
        and timestamp_column[1].unique()[0] == "2025-03-26T100346Z"
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


def test_raises_error_when_properties_do_not_match_data(resource_paths):
    """Raises errors from checks when the resource properties don't match the data."""
    # Given
    resource_properties.schema.fields[0].name = "not-id"

    # When, Then
    # TODO: Uncomment and add asserts when `check_data()` is implemented.
    # with raises(ExceptionGroup) as error_info:
    #     read_resource_batches(
    #         paths=resource_paths, resource_properties=resource_properties
    #     )

    # errors = error_info.value.exceptions

    assert True


def test_raises_error_with_empty_resource_properties():
    """Raises errors from checks if the resource properties are empty."""
    # When, Then
    # TODO: Uncomment and add asserts when `check_data()` is implemented.
    # with raises(ExceptionGroup) as error_info:
    #     read_resource_batches(
    #         paths=resource_paths, resource_properties=ResourceProperties()
    #     )

    # errors = error_info.value.exceptions

    assert True
