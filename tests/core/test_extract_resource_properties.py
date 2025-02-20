import polars as pl
from pytest import mark

from seedcase_sprout.core.extract_resource_properties import extract_resource_properties


empty_data = pl.DataFrame([])
schema_empty_data = {"fields": []}

tidy_data = pl.DataFrame(
    {
        "id": [1, 2, 3],
        "name": ["Alice", "Bob", "Charlie"],
        "dob": ["2000-09-22", "1996-11-12", "1998-03-15"],
        "height": [1.7, 1.6, 1.8],
        "survey_datetime": [
            "2020-01-02 08:00:00",
            "2021-02-03 09:00:00",
            "2022-03-04 10:00:00",
        ],
        "completed": [True, False, True],
    }
)
schema_tidy_data = {
    "fields": [
        {"name": "id", "type": "integer"},
        {"name": "name", "type": "string"},
        {"name": "dob", "type": "date"},
        {"name": "height", "type": "number"},
        {"name": "survey_datetime", "type": "datetime"},
        {"name": "completed", "type": "boolean"},
    ]
}

non_tidy_data = pl.DataFrame(
    {
        "id": [1, 2, "NA"],
        "name": ["Alice", 10, "Charlie"],
        "dob": ["2000-09-22", "1996-11-12", "1998-03-15 00:00:00"],
        "height": [1.7, 1.6, 1],
        "survey_datetime": [
            "2020-01-02 08:00:00",
            "2021-02-03",
            "2022-03-04 10:00:00",
        ],
        "completed": [True, False, True],
    },
    strict=False,
)
schema_non_tidy_data = {
    "fields": [
        {"name": "id", "type": "string"},
        {"name": "name", "type": "string"},
        {"name": "dob", "type": "string"},
        {"name": "height", "type": "number"},
        {"name": "survey_datetime", "type": "string"},
        {"name": "completed", "type": "boolean"},
    ]
}


@mark.parametrize(
    "data, expected_schema",
    [
        (empty_data, schema_empty_data),
        (tidy_data, schema_tidy_data),
        (non_tidy_data, schema_non_tidy_data),
    ],
)
def test_returns_expected_resource_properties_from_csv_file(
    tmp_path, data, expected_schema
):
    """Returns expected resource properties from a non-empty csv file."""
    # Given
    file_path = tmp_path / "data.csv"
    data.write_csv(file_path)

    expected_properties_compact_dict = {
        "name": "data",
        "path": str(file_path),
        "type": "table",
        "format": "csv",
        "mediatype": "text/csv",
        "encoding": "utf-8",
        "schema": expected_schema,
    }
    # When
    properties = extract_resource_properties(file_path)

    # Then
    assert properties.compact_dict == expected_properties_compact_dict


@mark.parametrize(
    "data, expected_schema",
    [
        (empty_data, schema_empty_data),
        (tidy_data, schema_tidy_data),
        (non_tidy_data, schema_non_tidy_data),
    ],
)
def test_returns_expected_resource_properties_from_tsv_file(
    tmp_path, data, expected_schema
):
    """Returns expected resource properties from a non-empty tsv file."""
    # Given
    file_path = tmp_path / "data.tsv"
    data.write_csv(file_path, separator="\t")

    expected_properties_compact_dict = {
        "name": "data",
        "path": str(file_path),
        "type": "table",
        "format": "tsv",
        "mediatype": "text/tsv",
        "encoding": "utf-8",
        "dialect": {"delimiter": "\t"},
        "schema": expected_schema,
    }
    # When
    properties = extract_resource_properties(file_path)

    # Then
    assert properties.compact_dict == expected_properties_compact_dict


@mark.parametrize(
    "data, expected_schema, extension",
    [
        (empty_data, schema_empty_data, "parq"),
        (tidy_data, schema_tidy_data, "parq"),
        (non_tidy_data, schema_non_tidy_data, "parq"),
        (empty_data, schema_empty_data, "parquet"),
        (tidy_data, schema_tidy_data, "parquet"),
        (non_tidy_data, schema_non_tidy_data, "parquet"),
    ],
)
def test_returns_expected_resource_properties_from_parquet_file(
    tmp_path, data, expected_schema, extension
):
    """Returns expected resource properties from a non-empty parquet file."""
    # Given
    file_path = tmp_path / f"data.{extension}"
    data.write_parquet(file_path)

    expected_properties_compact_dict = {
        "name": "data",
        "path": str(file_path),
        "type": "table",
        "format": f"{extension}",
        "mediatype": "application/parquet",
        # Note that the Frictionless library doesn't return encoding for parquet files
        "schema": expected_schema,
    }
    # When
    properties = extract_resource_properties(file_path)

    # Then
    assert properties.compact_dict == expected_properties_compact_dict
