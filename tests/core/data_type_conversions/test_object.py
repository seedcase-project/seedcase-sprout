import polars as pl
import pyarrow as pa
import pyarrow.parquet as pq

# given a string value, a frictionless type and an arrow type, show me the type and form of that value in parquet

parquet_path = "test.parquet"
values = [
    '{"key": "value"}iuoi',
    '[{"key": "value"}]iuoi',
    '[{"key": "value"}]i,,u,  oi',
]

fr_type = "object"
col_name = f"my_{fr_type}"

# Direct to arrow
arrow_type = pa.json_()

schema = pa.schema([(col_name, arrow_type)])
print(schema)
arrow_table = pa.table({col_name: values}).cast(schema)
# points_array = pa.compute.split_pattern_regex(values, pattern=r",\s?")
# arrow_table = arrow_table.set_column(0, col_name, points_array).cast(schema)

pq.write_table(arrow_table, parquet_path)
parquet_file = pq.ParquetFile(parquet_path)

print(parquet_file.schema)
arrow_contents = pq.read_table(parquet_path).column(col_name).to_pylist()
arrow_contents = [str(d) for d in arrow_contents]
print(arrow_contents)

# via Polars
polars_schema = {col_name: pl.String}
polars_df = pl.DataFrame({col_name: values}).cast(polars_schema)
print(polars_df)
polars_df.write_parquet(parquet_path)

# Check contents
parquet_file = pq.ParquetFile(parquet_path)
print(parquet_file.schema)
polars_contents = pq.read_table(parquet_path).column(col_name).to_pylist()
polars_contents = [str(d) for d in polars_contents]
print(polars_contents)

print(str(arrow_contents) == str(polars_contents))
