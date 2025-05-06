import polars as pl

from seedcase_sprout.core.internals.functionals import _map, _map2
from seedcase_sprout.core.map_data_types import (
    _polars_to_frictionless,
)
from seedcase_sprout.core.properties import (
    FieldProperties,
    ResourceProperties,
    TableSchemaProperties,
)


def extract_resource_properties(data: pl.DataFrame) -> ResourceProperties:
    """Extracts resource properties from Polars DataFrame.

    The data types are extracted from the DataFrame's schema and mapped from Polars to
    Frictionless data types. For the best results, ensure the DataFrame's schema is as
    expected. Since there are differences between Polars and Frictionless data types,
    the mapping may not always be perfect, and some data types might be extracted
    in a simplified way. For example, a year column might be extracted as an integer
    instead of Frictionless's `year` type. Review and adjust the extracted properties
    as needed.

    Args:
        data: A Polars DataFrame containing the data to extract properties from.

    Returns:
        A `ResourceProperties` object.

    Raises:
        ValueError: If the data is empty

    Examples:
        ```{python}
        import seedcase_sprout.core as sp

        sp.extract_resource_properties(
            data=sp.example_data(),
        )
        ```
    """
    if data.is_empty():
        raise ValueError("Data is empty. Cannot extract resource properties.")

    resource_properties = ResourceProperties()
    resource_properties.type = "table"
    resource_properties.schema = TableSchemaProperties(fields_match="equal")
    resource_properties.schema.fields = _extract_field_properties(data)

    return resource_properties


def _extract_field_properties(data: pl.DataFrame):
    """Extract field properties from a Polars DataFrame."""
    # TODO: add format="binary" to Binary field type?
    field_names = data.columns
    field_types = _map(data.dtypes, _polars_to_frictionless)

    field_properties = _map2(
        field_names,
        field_types,
        lambda field_name, field_type: FieldProperties(
            name=field_name, type=field_type
        ),
    )

    return field_properties
