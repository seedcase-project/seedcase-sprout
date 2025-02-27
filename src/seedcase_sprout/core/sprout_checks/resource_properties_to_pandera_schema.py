import pandera.polars as pap
import polars as pl

from seedcase_sprout.core.get_nested_attr import get_nested_attr
from seedcase_sprout.core.properties import (
    FieldProperties,
    FieldType,
    ResourceProperties,
)
from seedcase_sprout.core.sprout_checks.get_pandera_checks import (
    get_pandera_checks,
)


def resource_properties_to_pandera_schema(
    resource_properties: ResourceProperties,
) -> pap.DataFrameSchema:
    """Converts a set of resource properties to a Pandera schema.

    Args:
        resource_properties: The resource properties to convert.

    Returns:
        The resulting Pandera schema.
    """
    fields: list[FieldProperties] = get_nested_attr(
        resource_properties,
        "schema.fields",
        default=[],
    )

    columns = {
        field.name: pap.Column(
            dtype=get_polars_data_type(field.type),
            checks=get_pandera_checks(field),
            nullable=True,
            coerce=True,
        )
        for field in fields
    }

    return pap.DataFrameSchema(columns, strict=True)


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
        case "number":
            return pl.Float64
        case "integer":
            return pl.Int64
        case _:
            return pl.String
