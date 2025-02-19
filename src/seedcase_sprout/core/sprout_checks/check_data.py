from pathlib import Path

import polars as pl

from seedcase_sprout.core.get_nested_attr import get_nested_attr
from seedcase_sprout.core.properties import FieldProperties, ResourceProperties
from seedcase_sprout.core.sprout_checks.check_data_header import (
    check_data_header,
)
from seedcase_sprout.core.sprout_checks.check_resource_properties import (
    check_resource_properties,
)
from seedcase_sprout.core.sprout_checks.resource_properties_to_pandera_schema import (
    resource_properties_to_pandera_schema,
)


def check_data(data_path: Path, resource_properties: ResourceProperties) -> Path:
    """Checks that the CSV data file at `data_path` matches the resource properties.

    Runs the following checks:
    - Can the data file be read as a CSV file?
    - Does the data file have a header row that matches column names in the properties?
    - Do the columns in the data file match those in the properties?
    - Do the data types in the data file match those in the properties?
    TODO: - Does the data in the data file meet the constraints in the properties?

    Args:
        data_path: The path to the raw data file.
        resource_properties: The properties object for the specific resource.

    Returns:
        The `data_path` if all checks are successful.

    Raises:
        ExceptionGroup[CheckError]: If the resource properties are incorrect.
        polars.exceptions.ComputeError: If the data file cannot be parsed as CSV.
        polars.exceptions.ShapeError: If the columns in the data file cannot
            be matched with the columns in the resource properties.
        pandera.errors.SchemaErrors: If data types in the data file do not match the
            data types in the resource properties or if the data violates any
            constraints in the resource properties.
    """
    check_resource_properties(resource_properties)

    # Prepare for reading the data file
    lazy_frame = pl.scan_csv(
        data_path,
        has_header=True,
        infer_schema=False,
        missing_utf8_is_empty_string=True,
    )

    # Check data header against resource properties
    fields: list[FieldProperties] = get_nested_attr(
        resource_properties, "schema.fields", default=[]
    )
    expected_columns = [field.name for field in fields]
    check_data_header(lazy_frame, expected_columns)

    # Set missing values to null
    schema_missing_values = get_nested_attr(
        resource_properties, "schema.missing_values", default=[""]
    )
    lazy_frame = lazy_frame.with_columns(
        pl.col(field.name).replace(
            schema_missing_values
            if field.missing_values is None
            else field.missing_values,
            None,
        )
        for field in fields
    )

    # Check the number of columns in each data row
    try:
        data_frame = lazy_frame.collect()
    except pl.exceptions.ComputeError as error:
        if "found more fields than defined" in str(error):
            raise pl.exceptions.ShapeError(
                "At least one data row contains more items than the expected number of"
                f"columns. Expected columns: {expected_columns}."
            ) from error
        raise

    # Check data against resource properties
    schema = resource_properties_to_pandera_schema(resource_properties)
    schema.validate(data_frame, lazy=True)

    return data_path
