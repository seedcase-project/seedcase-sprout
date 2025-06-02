import polars as pl

from seedcase_sprout.create_resource_properties_template import (
    create_resource_properties_template,
)
from seedcase_sprout.internals.functionals import _map, _map2
from seedcase_sprout.map_data_types import (
    _polars_to_datapackage,
)
from seedcase_sprout.properties import (
    FieldProperties,
    ResourceProperties,
    TableSchemaProperties,
)


def extract_resource_properties(
    data: pl.DataFrame, resource_name: str = ""
) -> ResourceProperties:
    """Extracts resource properties from Polars DataFrame.

    The data types are extracted from the DataFrame's schema and mapped from Polars to
    Data Package data types. For the best results, ensure the DataFrame's schema is as
    expected. Since there are differences between Polars and Data Package data types,
    the mapping may not always be perfect, and some data types might be extracted
    in a simplified way. For example, a year column might be extracted as an integer
    instead of Data Package's `year` type. Review and adjust the extracted properties
    as needed.

    Args:
        data: A Polars DataFrame containing the data to extract properties from.
        resource_name: The name of the new resource. Defaults to "".

    Returns:
        A `ResourceProperties` object.

    Raises:
        ValueError: If the data is empty

    Examples:
        ```{python}
        import seedcase_sprout as sp

        sp.extract_resource_properties(
            data=sp.example_data(),
            resource_name="my-resource",
        )
        ```
    """
    if data.is_empty():
        raise ValueError("Data is empty. Cannot extract resource properties.")

    resource_properties = ResourceProperties(name=resource_name, type="table")
    resource_properties.schema = TableSchemaProperties(fields_match="equal")
    resource_properties.schema.fields = _extract_field_properties(data)

    create_resource_properties_template(
        resource_name=resource_name, fields=resource_properties.schema.fields
    )

    return resource_properties


def _extract_field_properties(data: pl.DataFrame):
    """Extract field properties from a Polars DataFrame."""
    # TODO: add format="binary" to Binary field type?
    field_names = data.columns
    field_types = _map(data.dtypes, _polars_to_datapackage)

    field_properties = _map2(
        field_names,
        field_types,
        lambda name, type: FieldProperties(name=name, type=type),
    )

    return field_properties
