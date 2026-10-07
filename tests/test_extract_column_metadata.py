import seedcase_soil as so

from seedcase_sprout.examples import (
    example_data_all_polars_types,
    example_resource_properties_all_polars_types,
)
from seedcase_sprout.extract_column_metadata import (
    extract_column_metadata,
)
from seedcase_sprout.properties import FieldProperties, ResourceProperties


def _keep_extractable_properties(
    example_properties: ResourceProperties,
) -> list[FieldProperties]:
    """Filter example properties to only keep the extractable properties."""
    assert example_properties.schema
    assert example_properties.schema.fields
    return so.fmap(
        example_properties.schema.fields,
        lambda field: FieldProperties(name=field.name, type=field.type),
    )


def test_properties_are_extracted_correctly():
    """Test that the resource properties are extracted correctly from the data."""
    # Given, when
    extracted_field_properties = extract_column_metadata(
        example_data_all_polars_types()
    )
    expected_field_properties = _keep_extractable_properties(
        example_resource_properties_all_polars_types()
    )
    # Then
    assert extracted_field_properties == expected_field_properties
