import polars as pl
from pytest import raises

from seedcase_sprout.core.examples import (
    example_data_all_polars_types,
    example_resource_properties_all_polars_types,
)
from seedcase_sprout.core.extract_resource_properties import (
    extract_resource_properties,
)
from seedcase_sprout.core.properties import (
    FieldProperties,
    ResourceProperties,
    TableSchemaProperties,
)


def _keep_extractable_properties(
    example_properties: ResourceProperties,
) -> ResourceProperties:
    """Filter example properties to only keep the extractable properties."""

    fields = list(
        map(
            lambda field: FieldProperties(name=field.name, type=field.type),
            example_properties.schema.fields,
        )
    )

    return ResourceProperties(
        schema=TableSchemaProperties(fields=fields, fields_match="equal"),
        type="table",
    )


def test_properties_are_extracted_correctly():
    """Test that the resource properties are extracted correctly from the data."""
    extracted_resource_properties = extract_resource_properties(
        example_data_all_polars_types()
    )

    assert extracted_resource_properties == _keep_extractable_properties(
        example_resource_properties_all_polars_types()
    )


def test_throw_error_with_empty_data():
    """Test that an error is thrown when the data is empty."""
    with raises(ValueError):
        extract_resource_properties(pl.DataFrame([]))
