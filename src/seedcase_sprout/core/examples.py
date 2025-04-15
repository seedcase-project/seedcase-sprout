import os
import tempfile
from contextlib import AbstractContextManager
from pathlib import Path
from uuid import uuid4

import polars as pl

from seedcase_sprout.core.as_readme_text import as_readme_text
from seedcase_sprout.core.create_resource_properties import create_resource_properties
from seedcase_sprout.core.create_resource_structure import create_resource_structure
from seedcase_sprout.core.get_iso_timestamp import get_iso_timestamp
from seedcase_sprout.core.map_data_types import FRICTIONLESS_TO_POLARS
from seedcase_sprout.core.paths import PackagePath
from seedcase_sprout.core.properties import (
    ContributorProperties,
    FieldProperties,
    LicenseProperties,
    PackageProperties,
    ResourceProperties,
    TableSchemaProperties,
)
from seedcase_sprout.core.write_file import write_file
from seedcase_sprout.core.write_package_properties import write_package_properties


def example_package_properties() -> PackageProperties:
    """Generate an example package properties object.

    Returns:
        Outputs a correctly formatted example `PackageProperties` object.

    Examples:
        ```{python}
        import seedcase_sprout.core as sp
        sp.example_package_properties()
        ```
    """
    properties = PackageProperties(
        name="example-package",
        version="0.1.0",
        created=get_iso_timestamp(),
        id=str(uuid4()),
        title="Example fake data package",
        description="Data from a fake data package on something.",
        contributors=[
            ContributorProperties(
                title="Jamie Jones",
                email="jamie_jones@example.com",
                roles=["creator"],
            )
        ],
        licenses=[
            LicenseProperties(
                name="ODC-BY-1.0",
                path="https://opendatacommons.org/licenses/by",
                title="Open Data Commons Attribution License 1.0",
            )
        ],
    )

    return properties


def example_resource_properties() -> ResourceProperties:
    """Generate an example resource properties object.

    Returns:
        Outputs a correctly formatted example `ResourceProperties` object.

    Examples:
        ```{python}
        import seedcase_sprout.core as sp
        sp.example_resource_properties()
        ```
    """
    return ResourceProperties(
        name="example-resource",
        title="Example fake data resource",
        description="Data from a fake resource on something.",
        path="resources/1/data.parquet",
        schema=TableSchemaProperties(
            fields=[
                FieldProperties(
                    name="id",
                    title="ID",
                    description="Unique identifier for the record.",
                    type="integer",
                ),
                FieldProperties(
                    name="name",
                    title="Name",
                    description="Name of the record.",
                    type="string",
                ),
                FieldProperties(
                    name="value",
                    title="Value",
                    description="Value of the record.",
                    type="number",
                ),
            ],
            primary_key=["id"],
        ),
    )


def example_data() -> pl.DataFrame:
    """Generate an example Polars data frame.

    Returns:
        A Polars data frame matching the resource properties generated by
            `example_resource_properties()`.

    Examples:
        ```{python}
        import seedcase_sprout.core as sp
        sp.example_data()
        ```
    """
    return pl.DataFrame(
        {
            "id": [34, 99, 100],
            "name": ["Helly R", "Mark S", "Ms Casey"],
            "value": [123.123, 9988, -76.0009],
        }
    )


def example_resource_properties_all_types() -> ResourceProperties:
    """Generate an example resource properties object with all Frictionless data types.

    Returns:
        Outputs a correctly formatted example `ResourceProperties` object.

    Examples:
        ```{python}
        import seedcase_sprout.core as sp
        sp.example_resource_properties_all_types()
        ```
    """
    return ResourceProperties(
        name="data",
        title="data",
        path=str(Path("resources", "1", "data.parquet")),
        description="My data...",
        schema=TableSchemaProperties(
            fields=[
                FieldProperties(name="my_boolean", type="boolean"),
                FieldProperties(name="my_integer", type="integer"),
                FieldProperties(name="my_number", type="number"),
                FieldProperties(name="my_year", type="year"),
                FieldProperties(name="my_yearmonth", type="yearmonth"),
                FieldProperties(name="my_datetime_tz", type="datetime"),
                FieldProperties(name="my_datetime_no_tz", type="datetime"),
                FieldProperties(name="my_date", type="date"),
                FieldProperties(name="my_time", type="time"),
                FieldProperties(name="my_geopoint", type="geopoint"),
                FieldProperties(name="my_array", type="array"),
                FieldProperties(name="my_object", type="object"),
                FieldProperties(name="my_string", type="string"),
                FieldProperties(name="my_any", type="any"),
                FieldProperties(name="my_none", type=None),
                FieldProperties(name="my_duration", type="duration"),
                FieldProperties(name="my_geojson", type="geojson"),
            ],
        ),
    )


def example_data_all_types() -> pl.DataFrame:
    """Generate an example Polars data frame with all Frictionless data types.

    Returns:
        A Polars data frame matching the resource properties generated by
            `example_resource_properties_all_types()`.

    Examples:
        ```{python}
        import seedcase_sprout.core as sp
        sp.example_data_all_types()
        ```
    """
    return pl.DataFrame(
        {
            "my_boolean": [True, True, False],
            "my_integer": [12223, -123, 0],
            "my_number": [123.123, float("inf"), float("2E-33")],
            "my_year": [2012, -1000, 0],
            "my_yearmonth": pl.Series(
                ["2014-12-01", "0001-01-01", "0000-01-01"]
            ).str.to_date(),
            "my_datetime_tz": pl.Series(
                [
                    "2002-10-10T12:00:00+01:00",
                    "2002-05-12T12:40:00.34+01:00",
                    "2019-01-20T09:30:00+01:00",
                ]
            ).str.to_datetime(),
            "my_datetime_no_tz": pl.Series(
                [
                    "2002-10-10T12:44:10",
                    "2002-10-10T12:00:00.34",
                    "0000-01-01T00:00:00",
                ]
            ).str.to_datetime(),
            "my_date": pl.Series(
                ["2002-10-10", "0001-01-01", "0000-01-01"]
            ).str.to_date(),
            "my_time": pl.Series(
                ["15:00:59", "00:00:00.3", "12:00:00.345345"]
            ).str.to_time(),
            "my_geopoint": pl.Series([[-90, -180], [5, 45], [5.9999, 45.0000]]).cast(
                FRICTIONLESS_TO_POLARS["geopoint"]
            ),
            "my_array": [
                "[]",
                '[{"prop1": true}]',
                '[{"prop1": "value"}, {"prop2": 123}]',
            ],
            "my_object": [
                "{}",
                '{"outer": "value", "inner": {"prop1": 123, "prop2": [1, 2, null]}}',
                '{"outer": "value", "inner": {"prop1": 123, "prop2": true}}',
            ],
            "my_string": ["some text", "æøåäöü£$%^&*()\\''", "μῆνιν ἄειδε θεὰ"],
            "my_any": pl.Series([[1]] * 3, dtype=pl.List),
            "my_none": pl.Series([[1]] * 3, dtype=pl.List),
            "my_duration": ["P1Y2M3DT10H30M45.343S", "P1Y2M3DT10H30M45", "P33Y6M4D"],
            "my_geojson": ["{}"] * 3,
        }
    )


def example_resource_properties_all_polars_types() -> ResourceProperties:
    """Generate an example resource properties object with all Polars data types.

    Returns:
        Outputs a correctly formatted example `ResourceProperties` object.
        sp.example_resource_properties_all_polars_types()
        ```
    """
    return ResourceProperties(
        name="data",
        title="data",
        path=str(Path("resources", "1", "data.parquet")),
        description="My data...",
        schema=TableSchemaProperties(
            fields=[
                FieldProperties(name="my_decimal", type="number"),
                FieldProperties(name="my_float32", type="number"),
                FieldProperties(name="my_float64", type="number"),
                FieldProperties(name="my_int8", type="integer"),
                FieldProperties(name="my_int16", type="integer"),
                FieldProperties(name="my_int32", type="integer"),
                FieldProperties(name="my_int64", type="integer"),
                FieldProperties(name="my_int128", type="integer"),
                FieldProperties(name="my_uint8", type="integer"),
                FieldProperties(name="my_uint16", type="integer"),
                FieldProperties(name="my_uint32", type="integer"),
                FieldProperties(name="my_uint64", type="integer"),
                FieldProperties(name="my_date", type="date"),
                FieldProperties(name="my_datetime", type="datetime"),
                FieldProperties(name="my_duration", type="string"),
                FieldProperties(name="my_time", type="time"),
                FieldProperties(name="my_array", type="array"),
                FieldProperties(name="my_list", type="list"),
                FieldProperties(name="my_struct", type="object"),
                FieldProperties(name="my_string", type="string"),
                FieldProperties(name="my_categorical", type="string"),
                FieldProperties(name="my_enum", type="string"),
                FieldProperties(name="my_binary", type="string"),
                FieldProperties(name="my_boolean", type="boolean"),
                FieldProperties(name="my_null", type="any"),
                FieldProperties(name="my_object", type="object"),
            ],
        ),
    )


def example_data_all_polars_types() -> pl.DataFrame:
    """Generate an example Polars data frame with all Polars data types.

    Returns:
        A Polars data frame matching the resource properties generated by
            `example_resource_properties_all_polars_types()`.

    Examples:
        ```{python}
        import seedcase_sprout.core as sp
        sp.example_data_all_polars_types()
        ```
    """
    return pl.DataFrame(
        {
            "my_decimal": pl.Series([1.1, 2.2], dtype=pl.Decimal(10, 2)),
            "my_float32": pl.Series([1.1, 2.2], dtype=pl.Float32),
            "my_float64": pl.Series([1.1, 2.2], dtype=pl.Float64),
            "my_int8": pl.Series([1, 2], dtype=pl.Int8),
            "my_int16": pl.Series([1, 2], dtype=pl.Int16),
            "my_int32": pl.Series([1, 2], dtype=pl.Int32),
            "my_int64": pl.Series([1, 2], dtype=pl.Int64),
            "my_int128": pl.Series([1, 2], dtype=pl.Int128),
            "my_uint8": pl.Series([1, 2], dtype=pl.UInt8),
            "my_uint16": pl.Series([1, 2], dtype=pl.UInt16),
            "my_uint32": pl.Series([1, 2], dtype=pl.UInt32),
            "my_uint64": pl.Series([1, 2], dtype=pl.UInt64),
            "my_date": pl.Series(["2023-01-01", "2023-01-02"]).str.to_date(),
            "my_datetime": pl.Series(
                ["2023-01-01 00:00:00", "2023-01-02 00:00:00"]
            ).str.to_datetime(),
            "my_duration": pl.Series([1, 2]).cast(pl.Duration("ms")),
            "my_time": pl.Series(["00:00:00", "01:00:00"]).str.to_time(),
            "my_array": pl.Series([[1, 2], [3, 4]]).cast(pl.Array(pl.Int32, shape=2)),
            "my_list": pl.Series([[1, 2], [3, 4]]).cast(pl.List(pl.Int32)),
            "my_struct": pl.Series([{"a": 1}, {"b": 2}]),
            "my_string": pl.Series(["a", "b"]),
            "my_categorical": pl.Series(["a", "b"]).cast(pl.Categorical),
            "my_enum": pl.Series(["a", "b"]).cast(pl.Enum(categories=["a", "b"])),
            # pl.Utf8 is an alias for pl.String, so it's not included here
            "my_binary": pl.Series([b"a", b"b"]),
            "my_boolean": pl.Series([True, False]),
            "my_null": pl.Series([None, None]),
            "my_object": pl.Series(["a", {"a": 1}], dtype=pl.Object),
            # TODO: Couldn't find a way to create pl.Unknown
        }
    )


class ExamplePackage(AbstractContextManager):
    """Create a temporary data package with optional resources for demoing or testing.

    Examples:
        ```{python}
        import seedcase_sprout.core as sp
        with sp.ExamplePackage() as package_path:
            properties = sp.read_properties(package_path.properties())

        with sp.ExamplePackage(with_resources=False) as package_path:
            properties = sp.read_properties(package_path.properties())
        ```
    """

    def __init__(self, with_resources: bool = True):
        """Initialise the `ExamplePackage` context manager.

        Args:
            with_resources: Whether resources should be added when creating the package.
                Defaults to True.
        """
        self.with_resources = with_resources
        self.calling_dir = Path.cwd()
        self.temp_dir = tempfile.TemporaryDirectory()

    def __enter__(self) -> PackagePath:
        """Create the temporary package structure and switch to its directory.

        Returns:
            A `PackagePath` object pointing to the root of the temporary package.
        """
        package_path = PackagePath(Path(self.temp_dir.name))

        # Create package properties
        package_properties = example_package_properties()

        # Create resource properties
        if self.with_resources:
            resource_properties = example_resource_properties()
            package_properties.resources = [resource_properties]

            # Create resource folders
            # TODO: update after resource creation is refactored
            package_path.resources().mkdir(exist_ok=True)
            resource_path, _ = create_resource_structure(path=package_path.path)
            resource_properties = create_resource_properties(
                path=resource_path, properties=resource_properties
            )
            resource_properties.name = resource_path.stem

        # Save properties
        write_package_properties(
            properties=package_properties, path=package_path.properties()
        )

        # Write README
        write_file(as_readme_text(package_properties), package_path.readme())

        os.chdir(package_path.path)

        return package_path

    def __exit__(self, *_) -> None:
        """Restore the original working directory and clean up the temporary package."""
        os.chdir(self.calling_dir)
        self.temp_dir.cleanup()

