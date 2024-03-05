"""CSV file validator."""
from typing import Mapping

import polars as pl
from polars import read_csv

from sprout.csv_reader import _transform_to_suitable_csv_format


class CsvValidationError:
    """Information about a CSV validation error."""

    def __init__(
        self,
        column: str,
        data_type: pl.PolarsDataType,
        row_number: int = 0,
        value: str = "",
        is_column_missing: bool = False,
    ):
        """CsvValidationError constructor.

        Args:
            column: Name of the column with the error
            data_type: The expected data type of the column
            row_number: The row of the error
            value: The value that gave an error
            is_column_missing: True if the entire column is missing
        """
        self.column = column
        self.data_type = str(data_type.base_type())
        self.row_number = row_number
        self.value = value
        self.is_column_missing = is_column_missing

    def __str__(self):
        """String representation of the CsvValidationError."""
        if self.is_column_missing:
            return f"Column '{self.column}' with type '{self.data_type}' is missing"

        return (
            f"Value '{self.value}' is not '{self.data_type}'. Column: "
            f"'{self.column}', row: '{self.row_number}'"
        )


def validate_csv(
    file_path: str, type_mapping: Mapping[str, pl.PolarsDataType]
) -> list[CsvValidationError]:
    """Validate the CSV file.

    Args:
        file_path: The path of the CSV file to validate.
        type_mapping: A mapping between the column name and the expected data type.

    Returns:
        list[CsvValidationError]: A list of csv validation errors.
    """
    transformed_csv = _transform_to_suitable_csv_format(file_path, None)

    # Read the csv and convert cell values to null if unable to convert to type.
    df = read_csv(transformed_csv, dtypes=type_mapping, ignore_errors=True)

    validation_errors = validate_column_names(df.columns, type_mapping)

    # Read the csv again, but disable type inference (infer_schema_length=0), so we
    # can get the original values as strings.
    df_str = read_csv(transformed_csv, infer_schema_length=0)
    # We also add row numbers in a column called "index" starting from 1
    df_str = df_str.with_row_index(offset=1)

    for col in df:
        validation_errors.extend(get_errors_in_column(col, df_str))
    return validation_errors


def validate_column_names(
    csv_columns: list[str], type_mapping: Mapping[str, pl.PolarsDataType]
) -> list[CsvValidationError]:
    """Validate if the columns in type_mapping are present in the CSV file.

    Args:
        csv_columns: The columns or headers in the CSV file
        type_mapping: The expected columns and corresponding types

    Returns:
        list[CsvValidationError]: A list of CsvValidationError with missing columns
    """
    return [
        CsvValidationError(col, dtype, is_column_missing=True)
        for col, dtype in type_mapping.items()
        if col not in csv_columns
    ]


def get_errors_in_column(
    column: pl.Series, df_strings: pl.DataFrame
) -> list[CsvValidationError]:
    """Get a CsvValidationError list for all errors in a column.

    Args:
        column: The column to validate.
        df_strings: A dataframe with original values

    Returns:
        list[CsvValidationError]: A list of errors for a column.
    """
    # Null values indicate either a type validation error or an empty value
    null_values = column.is_null()

    # For every null value, find the original string values and rows numbers
    str_values = df_strings[column.name].filter(null_values)
    row_numbers = df_strings["index"].filter(null_values)

    # Create a CsvValidationError for each null value (if the str_value is not empty)
    return [
        CsvValidationError(column.name, column.dtype, row_numbers[idx], str_value)
        for idx, str_value in enumerate(str_values)
        if str_value is not None
    ]
