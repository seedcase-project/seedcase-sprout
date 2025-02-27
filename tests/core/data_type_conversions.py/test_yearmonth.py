import polars as pl
import pyarrow as pa
import pyarrow.parquet as pq

# given a string value, a frictionless type and an arrow type, show me the type and form of that value in parquet

parquet_path = "test.parquet"
values = [
    "0005-12",
    # "-0001-05",
    # "-0001-05",
    "1000-05",
    # "10000-05",
    "5000-02",
    "9999-02",
    # "-500099-09",
    # "500099-10",
]
print(sorted(values))

fr_type = "yearmonth"
col_name = f"my_{fr_type}"

# # Direct to arrow
arrow_type = pa.date32()

schema = pa.schema([(col_name, arrow_type)])
arrow_table = pa.table({col_name: values})

date_array = pa.compute.replace_substring_regex(values, pattern=r"$", replacement="-01")
arrow_table = arrow_table.set_column(0, col_name, date_array).cast(schema)
print(arrow_table.schema)
pq.write_table(arrow_table, parquet_path)
parquet_file = pq.ParquetFile(parquet_path)

print(parquet_file.schema)
arrow_contents = pq.read_table(parquet_path).column(col_name).to_pylist()
print(arrow_contents)

# # # via Polars
polars_schema = {col_name: pl.Date}
polars_df = pl.DataFrame({col_name: values})
polars_df = polars_df.with_columns(pl.col(col_name) + "-01").cast(polars_schema)
polars_df.write_parquet(parquet_path)
parquet_file = pq.ParquetFile(parquet_path)
print(parquet_file.schema)
polars_contents = pq.read_table(parquet_path).column(col_name).to_pylist()

print(str(arrow_contents) == str(polars_contents))
