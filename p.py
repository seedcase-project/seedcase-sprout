from pathlib import Path

import polars as pl
import pyarrow.parquet as pq
from frictionless import Field, Resource, Schema

from seedcase_sprout.core.properties import (
    FieldProperties,
    ResourceProperties,
    TableSchemaProperties,
)

# Define a schema
desc = ResourceProperties(
    name="data",
    path="./data.csv",
    schema=TableSchemaProperties(
        fields=[
            FieldProperties(name="id", type="integer"),
            FieldProperties(name="name", type="string"),
            FieldProperties(name="salary", type="number"),
            FieldProperties(name="avc", type="string"),
            FieldProperties(name="created", type="yearmonth"),
            FieldProperties(name="date", type="date"),
        ]
    ),
).compact_dict
schema = Resource.from_descriptor(desc)

# Create a resource with the schema
resource = Resource(path="data.csv")

target = resource.write("table-output.parq")
# print(parquet_path.read_rows())


parquet_resource = Resource(
    target,
    # schema=schema,
)
print("Frictionless Schema:", parquet_resource.schema.to_descriptor())  # Print schema
print("Frictionless Data:")
print(target.read_rows())
print(target)


df = pl.read_parquet(Path("table-output.parq"))
print(df.schema)  # Print schema
print(df)  # Print contents


# Open the Parquet file
parquet_file = pq.ParquetFile(Path("table-output.parq"))

# Print the schema
print("\n=== Parquet Schema (PyArrow) ===")
print(parquet_file.schema)
