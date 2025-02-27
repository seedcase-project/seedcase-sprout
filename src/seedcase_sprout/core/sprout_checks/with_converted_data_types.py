import polars as pl
from isodate import parse_duration

from seedcase_sprout.core.get_nested_attr import get_nested_attr
from seedcase_sprout.core.properties import (
    FieldProperties,
    ResourceProperties,
    TableSchemaProperties,
)


def with_converted_data_types(
    lazy_frame: pl.LazyFrame, resource_properties: ResourceProperties
) -> pl.LazyFrame:
    fields: list[FieldProperties] = get_nested_attr(
        resource_properties, "schema.fields", default=[]
    )

    # Prepare for py-arrow cast
    # Create converted cols
    lazy_frame = lazy_frame.with_columns(
        pl.col(field.name).str.to_datetime("%H:%M:%S").dt.time()
        for field in fields
        if field.type == "time"
    )
    lazy_frame = lazy_frame.with_columns(
        pl.col(field.name).map_elements(
            lambda x: int(parse_duration(x).total_seconds()),
            # return_dtype=pl.Int32,
        )
        for field in fields
        if field.type == "duration"
    )
    lazy_frame = lazy_frame.with_columns(
        pl.col(field.name) + "-01" for field in fields if field.type == "yearmonth"
    )

    return lazy_frame
