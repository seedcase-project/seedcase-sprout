"""Functions for the exposed CLI."""

from pathlib import Path
from typing import Optional

import polars as pl
from seedcase_soil import (
    run_without_tracebacks,
    setup_cli,
)

from seedcase_sprout.create_resource_properties_script import (
    create_resource_properties_script_text,
)
from seedcase_sprout.extract_field_properties import extract_field_properties
from seedcase_sprout.write_file import write_file

app = setup_cli(
    name="seedcase-sprout",
    help=(
        "Grow your research data in a structured, modern way that follows best"
        " practices."
    ),
)


@app.command()
def extract_metadata(
    parquet_path: Path,
    /,  # End of positional-only args
    *,  # Start of keyword-only params
    output_path: Optional[Path] = None,
) -> None:
    """Extract metadata from a Parquet file.

    Args:
        parquet_path: The path to the Parquet file.
        output_path: The path where the extracted metadata should be saved.
            Defaults to `<parquet-filename>_properties.py` in the root folder.
    """
    if output_path is None:
        output_path = Path(f"{parquet_path.stem}_properties.py")

    data = pl.read_parquet(parquet_path)
    script_text = create_resource_properties_script_text(
        fields=extract_field_properties(data)
    )
    write_file(script_text, output_path)


def main() -> None:
    """Create an entry point to run the CLI without tracebacks."""
    run_without_tracebacks(app)
