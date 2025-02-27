from pathlib import Path

import polars as pl


def csv_to_data_frame(data_path: Path) -> pl.LazyFrame:
    # what if not csv

    return pl.scan_csv(
        data_path,
        has_header=True,
        infer_schema=False,
        missing_utf8_is_empty_string=True,
    )
