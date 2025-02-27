import polars as pl
import pyarrow as pa
import pyarrow.parquet as pq

# given a string value, a frictionless type and an arrow type, show me the type and form of that value in parquet

parquet_path = "test.parquet"
values = [
    "true",
    "True",
    "TRUE",
    "1",
    "false",
    "False",
    "FALSE",
    "0",
]
fr_type = "boolean"
col_name = f"my_{fr_type}"

# Direct to arrow
arrow_type = pa.bool_()

schema = pa.schema([(col_name, arrow_type)])
arrow_table = pa.table({col_name: values}).cast(schema)

pq.write_table(arrow_table, parquet_path)
parquet_file = pq.ParquetFile(parquet_path)

print(parquet_file.schema)
arrow_contents = pq.read_table(parquet_path).column(col_name).to_pylist()
print(arrow_contents)

# via Polars
polars_schema = {col_name: pl.Boolean}
polars_df = pl.DataFrame({col_name: values})
polars_df = polars_df.with_columns(
    pl.col(col_name)
    .replace(
        ["true", "True", "TRUE", "1"],
        "1",
    )
    .replace(
        ["false", "False", "FALSE", "0"],
        "0",
    )
    .cast(pl.Int8)
    .cast(pl.Boolean)
)
polars_df.write_parquet(parquet_path)
parquet_file = pq.ParquetFile(parquet_path)
print(parquet_file.schema)
polars_contents = pq.read_table(parquet_path).column(col_name).to_pylist()
print(polars_contents)
print(str(arrow_contents) == str(polars_contents))
