import polars as pl

from seedcase_sprout.core.properties import FieldType

# Mapping from Frictionless data types to Polars data types.
# See https://sprout.seedcase-project.org/docs/design/interface/data-types
# for more information.
FRICTIONLESS_TO_POLARS: dict[FieldType, pl.DataType] = {
    "string": pl.String,
    "boolean": pl.Boolean,
    "integer": pl.Int64,
    "number": pl.Float64,
    "year": pl.Int32,
    "datetime": pl.Datetime,
    "date": pl.Date,
    "time": pl.Time,
    "yearmonth": pl.Date,
    "geopoint": pl.Array(pl.Float64, 2),
    "duration": pl.String,
    "object": pl.String,
    "array": pl.String,
    "geojson": pl.String,
    "any": pl.String,
}

# Mapping from Polars data types to Frictionless data types
# Polars data types from https://docs.pola.rs/api/python/stable/reference/datatypes.html
# Note that this mapping does not cover all Frictionless data types, but is a simplified
# version for extracting field properties from pl.DataFrames.
# Missing Frictionless data types are: `year`, `yearmonth`, and `geojson`.
POLARS_TO_FRICTIONLESS = {
    # Numeric
    **{type: "number" for type in [pl.Decimal, pl.Float32, pl.Float64]},
    **{
        type: "integer"
        for type in [
            pl.Int8,
            pl.Int16,
            pl.Int32,
            pl.Int64,
            pl.Int128,
            pl.UInt8,
            pl.UInt16,
            pl.UInt32,
            pl.UInt64,
        ]
    },
    # Temporal
    pl.Date: "date",
    pl.Datetime: "datetime",
    pl.Duration: "duration",
    pl.Time: "time",
    # Nested
    pl.Array: "array",
    pl.List: "any",
    pl.Field: "object",
    pl.Struct: "object",
    # String
    **{type: "string" for type in [pl.String, pl.Categorical, pl.Enum, pl.Utf8]},
    # Other
    pl.Binary: "binary",
    pl.Boolean: "boolean",
    pl.Null: None,
    pl.Object: "object",
    pl.Unknown: "any",
}
