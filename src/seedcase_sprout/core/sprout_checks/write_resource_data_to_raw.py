from pathlib import Path

import polars as pl

from seedcase_sprout.core.properties import (
    FieldProperties,
    ResourceProperties,
    TableSchemaProperties,
)
from seedcase_sprout.core.sprout_checks.check_constraints import check_constraints
from seedcase_sprout.core.sprout_checks.check_data_header import check_data_header
from seedcase_sprout.core.sprout_checks.check_data_types_and_formats import (
    check_data_types_and_formats,
)
from seedcase_sprout.core.sprout_checks.check_resource_properties import (
    check_resource_properties,
)
from seedcase_sprout.core.sprout_checks.csv_to_data_frame import csv_to_data_frame
from seedcase_sprout.core.sprout_checks.with_converted_data_types import (
    with_converted_data_types,
)
from seedcase_sprout.core.sprout_checks.with_missing_values_null import (
    with_missing_values_null,
)
from seedcase_sprout.core.sprout_checks.write_parquet_to_raw import write_parquet_to_raw


def write_resource_data_to_raw(
    data_path: Path, resource_properties: ResourceProperties
) -> Path:
    check_resource_properties(resource_properties)

    lazy_frame = csv_to_data_frame(data_path)
    check_data_header(lazy_frame, resource_properties)

    lazy_frame = with_missing_values_null(lazy_frame, resource_properties)
    df = lazy_frame.collect()
    check_data_types_and_formats(df, resource_properties)

    lazy_frame = with_converted_data_types(df.lazy(), resource_properties)

    check_constraints(lazy_frame, resource_properties)

    write_parquet_to_raw(lazy_frame, resource_properties)


resource_properties = ResourceProperties(
    schema=TableSchemaProperties(
        fields=[
            FieldProperties(name="my_bool", type="boolean"),
            FieldProperties(name="my_time", type="time"),
            FieldProperties(name="my_datetime", type="datetime"),
            FieldProperties(name="my_duration", type="duration"),
            FieldProperties(name="my_integer", type="integer"),
            FieldProperties(name="my_string", type="string"),
            FieldProperties(name="my_number", type="number"),
            FieldProperties(name="my_date", type="date"),
            FieldProperties(name="my_year", type="year"),
            FieldProperties(name="my_yearmonth", type="yearmonth"),
        ]
    )
)
lf = pl.LazyFrame(
    {
        "my_bool": [True, False, False],
        "my_time": ["11:23:23", "05:05:05", "02:10:12"],
        "my_datetime": [
            "2002-10-10T12:00:00+01:00",
            "0001-01-01T00:00:00Z",
            "2002-10-10T12:00:00.34-05:00",
        ],
        "my_duration": ["P1Y2M3DT10H30M", "P1Y2M3DT10H30M45.343S", "P0Y0M0DT0H0M1S"],
        "my_integer": [23456, -2, 0],
        "my_string": ["val", "vsd", "ǫooo"],
        "my_number": [34.5, "nan", "-inf"],
        "my_date": ["0001-01-01", "2002-10-10", "2002-10-10"],
        "my_year": ["-0100", "2015", "0000"],
        "my_yearmonth": ["2014-12", "0100-09", "0001-01"],
    },
    {
        "my_bool": pl.String,
        "my_time": pl.String,
        "my_datetime": pl.String,
        "my_duration": pl.String,
        "my_integer": pl.String,
        "my_string": pl.String,
        "my_number": pl.String,
        "my_date": pl.String,
        "my_year": pl.String,
        "my_yearmonth": pl.String,
    },
    strict=False,
)
lazy_frame = with_missing_values_null(lf, resource_properties)
lazy_frame = with_converted_data_types(lf, resource_properties)
write_parquet_to_raw(lazy_frame, resource_properties)
