import polars as pl
import pyarrow as pa
import pyarrow.parquet as pq

# given a string value, a frictionless type and an arrow type, show me the type and form of that value in parquet

parquet_path = "test.parquet"
values = [
    "15:00:59",
    "00:00:00",
    # "06:23:22Z",
    # "12:00:00-05:00",
    "12:00:00.333222",
    "12:00:00.2",
    # "12:00:00.34-05:00",
]
fr_type = "time"
col_name = f"my_{fr_type}"

# Direct to arrow
# arrow_type = pa.time32("ms")

# schema = pa.schema([(col_name, arrow_type)])
# print(schema)
# arrow_table = pa.table({col_name: values})
# time_array = pa.compute.strptime(values, format="%H:%M:%S%.f", unit="ms").cast(
#     arrow_type
# )
# arrow_table = arrow_table.set_column(0, col_name, time_array).cast(schema)

# pq.write_table(arrow_table, parquet_path)
# parquet_file = pq.ParquetFile(parquet_path)

# print(parquet_file.schema)
# arrow_contents = pq.read_table(parquet_path).column(col_name).to_pylist()
# arrow_contents = [str(d) for d in arrow_contents]
# print(arrow_contents)

# via Polars
polars_schema = {col_name: pl.Time}
polars_df = pl.DataFrame({col_name: values})
polars_df = polars_df.with_columns(
    pl.col(col_name).str.to_time(format="%H:%M:%S%.f")
).cast(polars_schema)

arrow_table = polars_df.to_arrow()
print(arrow_table.schema)
pq.write_table(arrow_table, parquet_path)
parquet_file = pq.ParquetFile(parquet_path)
print(parquet_file.schema)
arrow_contents = pq.read_table(parquet_path).column(col_name).to_pylist()
arrow_contents = [str(d) for d in arrow_contents]
print(arrow_contents)


polars_df.write_parquet(parquet_path)
parquet_file = pq.ParquetFile(parquet_path)
print(parquet_file.schema)
polars_contents = pq.read_table(parquet_path).column(col_name).to_pylist()
polars_contents = [str(d) for d in polars_contents]
print(polars_contents)

print(str(arrow_contents) == str(polars_contents))
