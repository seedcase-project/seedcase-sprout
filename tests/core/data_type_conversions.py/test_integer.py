import polars as pl
import pyarrow as pa
import pyarrow.parquet as pq

# given a string value, a frictionless type and an arrow type, show me the type and form of that value in parquet

parquet_path = "test.parquet"
values = [
    "5",
    "-5",
    "005",
]
fr_type = "integer"
col_name = f"my_{fr_type}"

# Direct to arrow
arrow_type = pa.int64()

schema = pa.schema([(col_name, arrow_type)])
arrow_table = pa.table({col_name: values}).cast(schema)

pq.write_table(arrow_table, parquet_path)
parquet_file = pq.ParquetFile(parquet_path)

print(parquet_file.schema)
arrow_contents = pq.read_table(parquet_path).column(col_name).to_pylist()
print(arrow_contents)

# via Polars
polars_schema = {col_name: pl.Int64}
polars_df = pl.DataFrame({col_name: values}).cast(polars_schema)
polars_df.write_parquet(parquet_path)
parquet_file = pq.ParquetFile(parquet_path)
print(parquet_file.schema)
polars_contents = pq.read_table(parquet_path).column(col_name).to_pylist()

print(str(arrow_contents) == str(polars_contents))
