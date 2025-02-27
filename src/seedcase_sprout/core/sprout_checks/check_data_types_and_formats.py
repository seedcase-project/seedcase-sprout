import polars as pl

from seedcase_sprout.core.properties import (
    ResourceProperties,
)
from seedcase_sprout.core.sprout_checks.resource_properties_to_pandera_schema import (
    resource_properties_to_pandera_schema,
)


def check_data_types_and_formats(
    data_frame: pl.DataFrame, resource_properties: ResourceProperties
):
    # Check types and formats
    # For now, use pandera
    schema = resource_properties_to_pandera_schema(resource_properties)
    schema.validate(data_frame, lazy=True)

    return data_frame
