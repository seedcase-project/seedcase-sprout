import polars as pl
import pyarrow as pa
import pyarrow.parquet as pq

# given a string value, a frictionless type and an arrow type, show me the type and form of that value in parquet

parquet_path = "test.parquet"
values = [
    "P1Y2M3DT10H30M",
    "P1Y2M3DT10H30M45.343S",
    "P1347Y",
    "P1347M",
    "P1Y2MT2H",
    "P0Y1347M",
    "P0Y1347M0D",
    "-P1347M",
]

fr_type = "duration"
col_name = f"my_{fr_type}"

# Direct to arrow
arrow_type = pa.string()

schema = pa.schema([(col_name, arrow_type)])
print(schema)
arrow_table = pa.table({col_name: values}).cast(schema)
# date_array = pa.compute.replace_substring_regex(values, pattern=r"$", replacement="-01")
# arrow_table = arrow_table.set_column(0, col_name, date_array).cast(schema)

pq.write_table(arrow_table, parquet_path)
parquet_file = pq.ParquetFile(parquet_path)

print(parquet_file.schema)
arrow_contents = pq.read_table(parquet_path).column(col_name).to_pylist()
arrow_contents = [str(d) for d in arrow_contents]
print(arrow_contents)

# via Polars
polars_schema = {col_name: pl.String}
polars_df = pl.DataFrame({col_name: values}).cast(polars_schema)
# polars_df = polars_df.with_columns(
#     pl.col(col_name)
#     .str.replace("Z", "+00:00")
# )
polars_df.write_parquet(parquet_path)
parquet_file = pq.ParquetFile(parquet_path)
print(parquet_file.schema)
polars_contents = pq.read_table(parquet_path).column(col_name).to_pylist()
polars_contents = [str(d) for d in polars_contents]
print(polars_contents)

print(str(arrow_contents) == str(polars_contents))
