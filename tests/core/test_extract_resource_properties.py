import polars as pl
from pytest import mark

from seedcase_sprout.core.extract_resource_properties import extract_resource_properties

data = pl.DataFrame(
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

expected_schema = {
    "fields": [
        {"name": "id", "type": "integer"},
        {"name": "name", "type": "string"},
        {"name": "dob", "type": "date"},
        {"name": "height", "type": "number"},
        {"name": "survey_datetime", "type": "datetime"},
        {"name": "completed", "type": "boolean"},
    ]
}


@mark.parametrize(
    "file, expected_schema",
    [(data, expected_schema), (pl.DataFrame([]), {"fields": []})],
)
def test_returns_expected_resource_properties_from_csv_file(
    tmp_path, file, expected_schema
):
    """Returns expected resource properties from a non-empty csv file."""
    # Given
    file_path = tmp_path / "data.csv"
    file.write_csv(file_path)

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
