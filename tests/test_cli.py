"""Tests for the CLI commands."""

from pathlib import Path

import pytest
from pytest import mark

from seedcase_sprout.cli import app


@pytest.fixture
def mock_read_parquet(mocker):
    return mocker.patch("seedcase_sprout.cli.pl.read_parquet")


@pytest.fixture
def mock_write_file(mocker):
    return mocker.patch("seedcase_sprout.cli.write_file")


@pytest.fixture
def _mock_extract_field_properties(mocker):
    return mocker.patch("seedcase_sprout.cli.extract_field_properties")


@pytest.fixture
def mock_create_resource_properties_text(mocker):
    return mocker.patch("seedcase_sprout.cli.create_resource_properties_text")


@pytest.fixture
def mock_create_properties_text(mocker):
    return mocker.patch("seedcase_sprout.cli.create_properties_text")


@mark.parametrize("metadata_type", [[], ["--type", "package"]])
def test_init_package_metadata(
    mock_write_file,
    mock_create_properties_text,
    mock_create_resource_properties_text,
    metadata_type,
):
    output_path = Path("path/to/my-package.py")

    app(
        ["init-metadata", str(output_path), *metadata_type],
        result_action="return_value",
    )

    mock_create_properties_text.assert_called_once_with(package_name="my-package")
    mock_create_resource_properties_text.assert_not_called()
    mock_write_file.assert_called_once_with(
        mock_create_properties_text.return_value,
        output_path,
    )


def test_init_resource_metadata(
    mock_write_file,
    mock_create_properties_text,
    mock_create_resource_properties_text,
):
    output_path = Path("path/to/my-resource.py")

    app(
        ["init-metadata", str(output_path), "--type", "resource"],
        result_action="return_value",
    )

    mock_create_resource_properties_text.assert_called_once_with(
        fields=[], resource_name="my-resource"
    )
    mock_create_properties_text.assert_not_called()
    mock_write_file.assert_called_once_with(
        mock_create_resource_properties_text.return_value,
        output_path,
    )


def test_extract_metadata_with_default_output_path(
    mock_read_parquet,
    mock_write_file,
    _mock_extract_field_properties,
    mock_create_resource_properties_text,
):
    app(["extract-metadata", "path/to/data.parquet"], result_action="return_value")

    mock_read_parquet.assert_called_once_with(Path("path/to/data.parquet"))
    mock_write_file.assert_called_once_with(
        mock_create_resource_properties_text.return_value,
        Path("data_properties.py"),
    )


def test_extract_metadata_with_custom_output_path(
    mock_read_parquet,
    mock_write_file,
    _mock_extract_field_properties,
    mock_create_resource_properties_text,
):
    app(
        [
            "extract-metadata",
            "path/to/data.parquet",
            "--output-path",
            "path/to/output.py",
        ],
        result_action="return_value",
    )

    mock_read_parquet.assert_called_once_with(Path("path/to/data.parquet"))
    mock_write_file.assert_called_once_with(
        mock_create_resource_properties_text.return_value,
        Path("path/to/output.py"),
    )
