"""Tests for the CLI commands."""

from pathlib import Path

import pytest

from seedcase_sprout.cli import app


@pytest.fixture
def mock_read_parquet(mocker):
    return mocker.patch("seedcase_sprout.cli.pl.read_parquet")


@pytest.fixture
def mock_write_file(mocker):
    return mocker.patch("seedcase_sprout.cli.write_file")


@pytest.fixture
def mock_extract_field_properties(mocker):
    return mocker.patch("seedcase_sprout.cli.extract_field_properties")


@pytest.fixture
def mock_create_resource_properties_script_text(mocker):
    return mocker.patch("seedcase_sprout.cli.create_resource_properties_script_text")


def test_extract_metadata_with_default_output_path(
    mock_read_parquet,
    mock_write_file,
    mock_extract_field_properties,
    mock_create_resource_properties_script_text,
):
    app(["extract-metadata", "path/to/data.parquet"], result_action="return_value")

    mock_read_parquet.assert_called_once_with(Path("path/to/data.parquet"))
    mock_write_file.assert_called_once_with(
        mock_create_resource_properties_script_text.return_value,
        Path("data_properties.py"),
    )


def test_extract_metadata_with_custom_output_path(
    mock_read_parquet,
    mock_write_file,
    mock_extract_field_properties,
    mock_create_resource_properties_script_text,
):
    app(
        ["extract-metadata", "path/to/data.parquet", "--output", "path/to/output.py"],
        result_action="return_value",
    )

    mock_read_parquet.assert_called_once_with(Path("path/to/data.parquet"))
    mock_write_file.assert_called_once_with(
        mock_create_resource_properties_script_text.return_value,
        Path("path/to/output.py"),
    )
