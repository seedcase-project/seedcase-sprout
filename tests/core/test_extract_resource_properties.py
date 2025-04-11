import polars as pl
from pytest import mark, raises

from seedcase_sprout.core.examples import (
    example_data,
    example_data_all_types,
    example_resource_properties,
    example_resource_properties_all_types,
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
        schema=TableSchemaProperties(fields=fields),
        type="table",
    )


expected_resource_properties_all_types = _keep_extractable_properties(
    example_resource_properties_all_types()
)
# Adjustments based on what Polars detects in the data's schema
for index, field in enumerate(expected_resource_properties_all_types.schema.fields):
    if field.name == "my_year":
        expected_resource_properties_all_types.schema.fields[index].type = "integer"
    elif field.name == "my_yearmonth":
        expected_resource_properties_all_types.schema.fields[index].type = "date"
    elif field.name == "my_geopoint":
        expected_resource_properties_all_types.schema.fields[index].type = "array"
    elif field.name in ["my_duration", "my_object", "my_array", "my_geojson"]:
        expected_resource_properties_all_types.schema.fields[index].type = "string"


@mark.parametrize(
    "data, expected_resource_properties",
    [
        (example_data(), _keep_extractable_properties(example_resource_properties())),
        (
            example_data_all_types(),
            expected_resource_properties_all_types,
        ),
    ],
)
def test_properties_are_extracted_correctly(data, expected_resource_properties):
    """Test that the resource properties are extracted correctly from the data."""
    extracted_resource_properties = extract_resource_properties(data)

    assert isinstance(extracted_resource_properties, ResourceProperties)
    assert (
        extracted_resource_properties.compact_dict.keys()
        == expected_resource_properties.compact_dict.keys()
    )
    assert (
        extracted_resource_properties.schema.compact_dict.keys()
        == expected_resource_properties.schema.compact_dict.keys()
    )
    assert all(
        list(
            map(
                lambda extracted_field, expected_field: extracted_field.compact_dict
                == expected_field.compact_dict,
                extracted_resource_properties.schema.fields,
                expected_resource_properties.schema.fields,
            )
        )
    )


def test_throw_error_with_empty_data():
    """Test that an error is thrown when the data is empty."""
    with raises(ValueError):
        extract_resource_properties(pl.DataFrame([]))
