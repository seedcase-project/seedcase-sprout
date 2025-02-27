import pyarrow as pa

mapping = {
    "integer": pa.int32(),
    "any": pa.string(),
    "string": pa.string(),
    "number": pa.float32(),
    "datetime": pa.timestamp(unit="ms", tz="UTC"),
    "date": pa.date32(),
    "boolean": pa.bool_(),
    "time": pa.time32("s"),
    "duration": pa.duration("s"),
    "year": pa.int32(),
    "yearmonth": pa.date32(),
    "object": pa.string(),
    "array": pa.string(),
    "geopoint": pa.string(),
    "geojson": pa.string(),
}


def get_arrow_schema(fields) -> pa.Schema:
    return pa.schema([(field.name, mapping[field.type]) for field in fields])
