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
def mock_init_resource_metadata(mocker):
    return mocker.patch("seedcase_sprout.cli.init_resource_metadata")


@pytest.fixture
def mock_init_package_metadata(mocker):
    return mocker.patch("seedcase_sprout.cli.init_package_metadata")


@mark.parametrize("metadata_type", [[], ["--type", "package"]])
def test_init_package_metadata(
    mock_write_file,
    mock_init_package_metadata,
    mock_init_resource_metadata,
    metadata_type,
):
    output_path = Path("path/to/my-package.py")

    app(
        ["init-metadata", str(output_path), *metadata_type],
        result_action="return_value",
    )

    mock_init_package_metadata.assert_called_once_with(name="my-package")
    mock_init_resource_metadata.assert_not_called()
    mock_write_file.assert_called_once_with(
        mock_init_package_metadata.return_value,
        output_path,
    )


def test_init_resource_metadata(
    mock_write_file,
    mock_init_package_metadata,
    mock_init_resource_metadata,
):
    output_path = Path("path/to/my-resource.py")

    app(
        ["init-metadata", str(output_path), "--type", "resource"],
        result_action="return_value",
    )

    mock_init_resource_metadata.assert_called_once_with(metadata=[], name="my-resource")
    mock_init_package_metadata.assert_not_called()
    mock_write_file.assert_called_once_with(
        mock_init_resource_metadata.return_value,
        output_path,
    )


def test_extract_metadata_with_default_output_path(
    mock_read_parquet,
    mock_write_file,
    _mock_extract_field_properties,
    mock_init_resource_metadata,
):
    app(["extract-metadata", "path/to/data.parquet"], result_action="return_value")

    mock_read_parquet.assert_called_once_with(Path("path/to/data.parquet"))
    mock_write_file.assert_called_once_with(
        mock_init_resource_metadata.return_value,
        Path("data_properties.py"),
    )


def test_extract_metadata_with_custom_output_path(
    mock_read_parquet,
    mock_write_file,
    _mock_extract_field_properties,
    mock_init_resource_metadata,
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
        mock_init_resource_metadata.return_value,
        Path("path/to/output.py"),
    )
