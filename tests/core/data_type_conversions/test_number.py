import polars as pl
import pyarrow as pa
import pyarrow.parquet as pq

changed_values = [
    "9" * 99999,  # > inf, more just causes memory errors
    "0.30000000000000000000000000000000000000000000000010",  # > 0.3
    "12345678912345671",  # 17 signif. digits > ...72
]

# given a string value, a frictionless type and an arrow type, show me the type and form of that value in parquet

parquet_path = "test.parquet"
values = [
    "5",
    "05",
    "50.00",
    "-12.56",
    "+12.56",
    "0.09999999999999999",  # 16
    "00000000.0000099999999999999999",
    "10.09999999999999",
    "1234567891234567",  # 16
    "0.3000000000000000",
    "5E10",
    "5E-10",
    "NaN",
    "nan",
    "NAN",
    "inf",
    "INF",
    "-inf",
    "-INF",
]
fr_type = "number"
col_name = f"my_{fr_type}"

# Direct to arrow
arrow_type = pa.float64()

schema = pa.schema([(col_name, arrow_type)])
arrow_table = pa.table({col_name: values}).cast(schema)

pq.write_table(arrow_table, parquet_path)
parquet_file = pq.ParquetFile(parquet_path)

print(parquet_file.schema)
arrow_contents = pq.read_table(parquet_path).column(col_name).to_pylist()

# via Polars
polars_schema = {col_name: pl.Float64}
polars_df = pl.DataFrame({col_name: values}).cast(polars_schema)
polars_df.write_parquet(parquet_path)

# Check contents
parquet_file = pq.ParquetFile(parquet_path)
print(parquet_file.schema)
polars_contents = pq.read_table(parquet_path).column(col_name).to_pylist()

print(str(arrow_contents) == str(polars_contents))
