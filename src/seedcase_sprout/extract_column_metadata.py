import polars as pl
from seedcase_soil import fmap, pairwise_fmap

from seedcase_sprout.map_data_types import (
    _polars_to_datapackage,
)
from seedcase_sprout.properties import FieldProperties


def extract_column_metadata(data: pl.DataFrame) -> list[FieldProperties]:
    """Extract metadata on the columns in a Polars DataFrame.

    Args:
        data: A Polars DataFrame containing the data to extract properties
            from.

    Returns:
        A list of `FieldProperties` objects, each representing a field/column
        in the DataFrame.
    """
    column_names = data.columns
    column_types = fmap(data.dtypes, _polars_to_datapackage)

    metadata = pairwise_fmap(
        column_names,
        column_types,
        lambda name, type: FieldProperties(name=name, type=type),
    )

    return metadata
