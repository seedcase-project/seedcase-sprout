import polars as pl

import seedcase_sprout.core.check_datapackage as cdp
from seedcase_sprout.core.map_data_types import (
    POLARS_TO_FRICTIONLESS,
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

    cdp.check_resource_properties(
        resource_properties,
    )

    return resource_properties


def _extract_field_properties(data: pl.DataFrame):
    """Extract field properties from a Polars DataFrame."""
    # Simplify by extracting the field type from the Polars base type
    # (so e.g., Datetime(time_unit='us', time_zone='UTC') becomes Datetime)
    field_properties = [
        FieldProperties(name=key, type=POLARS_TO_FRICTIONLESS[value.base_type()])
        for key, value in data.schema.items()
    ]
    # TODO: add format="binary" to Binary field type?
    return field_properties
