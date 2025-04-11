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
    """Extracts resource properties from a batch data file.

    This function takes a Polars DataFrame and extracts properties from it into a
    `ResourceProperties` object.

    Note that some types may be simplified during the conversion. For example, a
    year might be extracted as an integer instead of using Frictionless's year type.
    Review and adjust the output as needed.

    Args:
        data: A Polars DataFrame containing the data to extract properties from.

    Returns:
        A `ResourceProperties` object. Use `write_resource_properties()`
            to save the object to the `datapackage.json` file.

    Raises:
        ValueError: If the data is empty

    Examples:
        ```{python}
        import seedcase_sprout.core as sp

        extract_resource_properties(
            data=sp.example_data(),
        )
        ```
    """
    resource_properties = ResourceProperties()
    resource_properties.type = "table"
    resource_properties.schema = TableSchemaProperties()
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
    if field_properties == []:
        raise ValueError("Failed to extract field properties from the provided data.")

    return field_properties
