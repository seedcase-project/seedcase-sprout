import polars as pl

from seedcase_sprout.core.get_nested_attr import get_nested_attr
from seedcase_sprout.core.properties import (
    FieldProperties,
    ResourceProperties,
)


def with_missing_values_null(
    lazy_frame: pl.LazyFrame, resource_properties: ResourceProperties
):
    fields: list[FieldProperties] = get_nested_attr(
        resource_properties, "schema.fields", default=[]
    )

    # Set missing values to null
    schema_missing_values = get_nested_attr(
        resource_properties, "schema.missing_values", default=[""]
    )
    return lazy_frame.with_columns(
        pl.col(field.name).replace(
            schema_missing_values
            if field.missing_values is None
            else field.missing_values,
            None,
        )
        for field in fields
    )
