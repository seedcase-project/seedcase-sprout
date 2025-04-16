from collections import OrderedDict
from typing import Callable

import polars as pl

from seedcase_sprout.core.properties import FieldType

"""
Mapping between Frictionless types and Polars types.

Each Frictionless type maps to a function that checks if a given Polars type is an
allowed representation of that Frictionless type. There are often multiple allowed
Polars types for a single Frictionless type.

To allow reverse lookups, i.e. mapping a Polars type to a single Frictionless type,
entries are listed in order of precedence. The Polars type should be compared against
Frictionless types in the order they are listed. The first entry with a passing check
should determine the Frictionless type. Use `polars_to_frictionless()` to do the reverse
lookup.
"""
_FRICTIONLESS_TO_POLARS: OrderedDict[FieldType, Callable[[pl.DataType], bool]] = (
    OrderedDict(
        {
            # Primary types: reverse lookup always gives back Frictionless type
            "number": lambda dtype: dtype.is_float() or dtype.is_decimal(),
            "integer": lambda dtype: (
                dtype.is_integer() or isinstance(dtype, pl.Duration)
            ),
            "string": lambda dtype: isinstance(
                dtype, (pl.String, pl.Categorical, pl.Enum, pl.Binary)
            ),
            "date": lambda dtype: isinstance(dtype, pl.Date),
            "datetime": lambda dtype: isinstance(dtype, pl.Datetime),
            "time": lambda dtype: dtype == pl.Time,  # Polars stores Time as a class
            "boolean": lambda dtype: isinstance(dtype, pl.Boolean),
            # Secondary types: reverse lookup gives back Frictionless type only if
            # primary type doesn't take precedence
            "array": lambda dtype: isinstance(dtype, (pl.String, pl.Array, pl.List)),
            "object": lambda dtype: isinstance(
                dtype, (pl.String, pl.Struct, pl.Object)
            ),
            # Tertiary types: reverse lookup never gives back Frictionless type
            "geopoint": lambda dtype: (
                isinstance(dtype, pl.Array)
                and dtype.size == 2
                and dtype.inner.is_numeric()
            ),
            "geojson": lambda dtype: isinstance(
                dtype, (pl.String, pl.Struct, pl.Object)
            ),
            "year": lambda dtype: dtype.is_integer(),
            "yearmonth": lambda dtype: isinstance(dtype, pl.Date),
            "duration": lambda dtype: isinstance(dtype, pl.String),
            # Fallback type
            "any": lambda _: True,
        }
    )
)

# Mapping from Frictionless types to descriptions of allowed Polars types
_FRICTIONLESS_TO_POLARS_DESCRIPTION: dict[FieldType, str] = {
    "number": "a float or decimal type",
    "integer": f"an integer type or '{pl.Duration}'",
    "string": (
        f"one of '{pl.String}', '{pl.Categorical}', '{pl.Enum}', or '{pl.Binary}'"
    ),
    "date": f"'{pl.Date}'",
    "datetime": f"'{pl.Datetime}'",
    "time": f"'{pl.Time}'",
    "boolean": f"'{pl.Boolean}'",
    "array": f"one of '{pl.String}', '{pl.Array}', or '{pl.List}'",
    "object": f"one of '{pl.String}', '{pl.Struct}', or '{pl.Object}'",
    "geopoint": "an array of a numeric type with size 2",
    "geojson": f"one of '{pl.String}', '{pl.Struct}', or '{pl.Object}'",
    "year": "an integer type",
    "yearmonth": f"'{pl.Date}'",
    "duration": f"'{pl.String}'",
    "any": "any type",
}


def _polars_to_frictionless(dtype: pl.DataType) -> FieldType:
    """Map a Polars type to the corresponding Frictionless type.

    Frictionless types are matched against the Polars type in the order set out in
    `_FRICTIONLESS_TO_POLARS_TYPE_CHECK`. The first successful match is returned.

    Args:
        dtype: The Polars type.

    Returns:
        The corresponding Frictionless type.
    """
    return next(
        (
            frictionless_type
            for frictionless_type, is_type in _FRICTIONLESS_TO_POLARS.items()
            if is_type(dtype)
        ),
        "any",
    )
