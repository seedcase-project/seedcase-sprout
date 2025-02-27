import polars as pl

from seedcase_sprout.core.get_nested_attr import get_nested_attr
from seedcase_sprout.core.properties import FieldProperties, ResourceProperties
from seedcase_sprout.core.sprout_checks.convert_column import get_arrow_schema


def write_parquet_to_raw(
    lazy_frame: pl.LazyFrame, resource_properties: ResourceProperties
):
    fields: list[FieldProperties] = get_nested_attr(
        resource_properties, "schema.fields", default=[]
    )
    # Drop original cols
    # Rename converted cols

    # Cast to py-arrow table with parquet data types
    table = lazy_frame.collect().to_arrow().cast(get_arrow_schema(fields))
    print(table)
