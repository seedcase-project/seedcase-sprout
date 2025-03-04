import polars as pl
import pyarrow as pa
import pyarrow.parquet as pq

# given a string value, a frictionless type and an arrow type, show me the type and form of that value in parquet

parquet_path = "test.parquet"
values = [
    "2002-10-10T12:00:00+01:00",
    "2002-10-10T12:00:00-05:00",
    "2002-10-10T12:00:00.3Z",
    "2002-10-10T12:00:00.345Z",
    "2002-10-10T12:00:00.34-05:00",
    "0022-10-10T12:00:00.34+05:00",
    "1000-10-10T23:00:00-05:30",
    "2002-10-10T12:00:00Z",
    "2002-10-10T17:00:00Z",
    "0001-01-01T00:00:00Z",
]
values = [
    "2002-10-10T12:00:00+01:00",
    "2002-10-10T06:00:30.302+01:00",
    "2002-10-10T11:30:00+01:00",
]

fr_type = "datetime"
col_name = f"my_{fr_type}"
timezone = "UTC"

# Direct to arrow
arrow_type = pa.timestamp(unit="ms", tz=timezone)

schema = pa.schema([(col_name, arrow_type)])
print(schema)
arrow_table = pa.table({col_name: values}).cast(schema)

pq.write_table(arrow_table, parquet_path)
parquet_file = pq.ParquetFile(parquet_path)

print(parquet_file.schema)
arrow_contents = pq.read_table(parquet_path).column(col_name).to_pylist()
arrow_contents = [str(d) for d in arrow_contents]
print(arrow_contents)

# via Polars
polars_schema = {col_name: pl.Datetime}
polars_df = pl.DataFrame({col_name: values})
polars_df = polars_df.with_columns(
    pl.col(col_name)
    .str.replace("Z", "+00:00")
    .str.to_datetime(time_unit="ms", format="%Y-%m-%dT%H:%M:%S%.f%z")
    # .dt.convert_time_zone(time_zone="Africa/Algiers")
)
polars_df.write_parquet(parquet_path)

# Check contents
parquet_file = pq.ParquetFile(parquet_path)
print(parquet_file.schema)
polars_contents = pq.read_table(parquet_path).column(col_name).to_pylist()
polars_contents = [str(d) for d in polars_contents]
print(polars_contents)

print(str(arrow_contents) == str(polars_contents))
