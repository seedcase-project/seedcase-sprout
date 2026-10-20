"""Tests for the CLI commands."""

import polars as pl
from pytest import MonkeyPatch, mark, raises

from seedcase_sprout.cli import app


def create_data_as_parquet(path):
    df = pl.DataFrame(
        {
            "col1": [1, -1, -3, 4],
            "col2": ["b", "c", "d", "a"],
        }
    )
    df.write_parquet(path)
    return path


def create_empty_parquet(path):
    df = pl.DataFrame({"col1": []})
    df.write_parquet(path)
    return path


@mark.parametrize("metadata_type", [["--type", "resource"], ["--type", "package"]])
def test_init_metadata(
    metadata_type,
    tmp_path,
):
    output_path = tmp_path / "metadata-file.py"

    app(
        ["init-metadata", str(output_path), *metadata_type],
        result_action="return_value",
    )

    assert output_path.is_file()


def test_extract_metadata_with_default_output_path(tmp_path, monkeypatch: MonkeyPatch):
    monkeypatch.chdir(tmp_path)
    input_parquet = tmp_path / "fake.parquet"
    create_data_as_parquet(input_parquet)
    app(["extract-metadata", str(input_parquet)], result_action="return_value")
    output_path = tmp_path / "fake_properties.py"
    assert output_path.is_file()


def test_extract_metadata_with_custom_output_path(tmp_path):
    input_parquet = tmp_path / "fake.parquet"
    create_data_as_parquet(input_parquet)
    output_path = tmp_path / "properties.py"
    app(
        ["extract-metadata", str(input_parquet), "--output-path", str(output_path)],
        result_action="return_value",
    )

    assert output_path.is_file()


def test_fail_extract_metadata_with_empty_parquet(tmp_path):
    input_parquet = tmp_path / "fake.parquet"
    create_empty_parquet(input_parquet)
    with raises(ValueError):
        app(
            ["extract-metadata", str(input_parquet)],
            result_action="return_value",
        )
