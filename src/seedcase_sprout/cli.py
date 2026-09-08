"""Functions for the exposed CLI."""

from pathlib import Path
from typing import Annotated, Literal

import polars as pl
from cyclopts import Parameter
from seedcase_soil import (
    run_without_tracebacks,
    setup_cli,
)

from seedcase_sprout.extract_field_properties import extract_field_properties
from seedcase_sprout.init import (
    create_properties_text,
    create_resource_properties_text,
)
from seedcase_sprout.write_file import write_file

app = setup_cli(
    name="seedcase-sprout",
    help=(
        "Grow organised and FAIR (findable, accessible, interoperable, and reusable) "
        "data."
    ),
)


@app.command()
def init_metadata(
    output_path: Path,
    /,  # End of positional-only params
    *,  # Start of keyword-only params
    metadata_type: Annotated[
        Literal["package", "resource"], Parameter(name="--type")
    ] = "package",
) -> None:
    """Create a Python script with empty metadata fields.

    Args:
        output_path: The path where the script will be created.
        metadata_type: Whether to create a script for package metadata (i.e.,
            top-level metadata) or resource metadata.
    """
    name = output_path.stem

    if metadata_type == "package":
        script_text = create_properties_text(package_name=name)
    else:
        script_text = create_resource_properties_text(fields=[], resource_name=name)

    write_file(script_text, output_path)


@app.command()
def extract_metadata(
    parquet_path: Path,
    /,  # End of positional-only params
    *,  # Start of keyword-only params
    output_path: Path | None = None,
) -> None:
    """Extract metadata from a Parquet file.

    Args:
        parquet_path: The path to the Parquet file.
        output_path: The path where the extracted metadata should be saved.
            Defaults to `<parquet-filename>_properties.py` in the current
            working directory.
    """
    if output_path is None:
        output_path = Path(f"{parquet_path.stem}_properties.py")

    df = pl.read_parquet(parquet_path)
    script_text = create_resource_properties_text(fields=extract_field_properties(df))
    write_file(script_text, output_path)


def main() -> None:
    """Create an entry point to run the CLI without tracebacks."""
    run_without_tracebacks(app)
