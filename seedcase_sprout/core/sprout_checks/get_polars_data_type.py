import polars as pl

from seedcase_sprout.core.properties import FieldType


def get_polars_data_type(field_type: FieldType | None) -> pl.DataType:
    """Maps Frictionless field types to Polars data types.

    If the Frictionless field type has formatting constraints that are not included
    in any specialised Polars data type, the mapping is to string. The formatting
    constraints are then checked without Polars.

    Args:
        field_type: The Frictionless field type to map.

    Returns:
        The Polars data type the field is mapped to.

    Raises:
        NotImplementedError: If Sprout doesn't yet support the Frictionless field type.
    """
    match field_type:
        case "geojson":
            raise NotImplementedError()
        case (
            "string"
            | "boolean"
            | "datetime"
            | "date"
            | "time"
            | "year"
            | "yearmonth"
            | "duration"
            | "list"
            | "array"
            | "object"
            | "geopoint"
        ):
            return pl.String
        case "number":
            return pl.Float64
        case "integer":
            return pl.Int64
        case _:
            return pl.String
