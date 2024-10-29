from pathlib import Path

from pytest import fixture, mark, raises

from sprout.core.check_raw_data import check_raw_data
from sprout.core.mismatched_raw_data_error import MismatchedRawDataError
from sprout.core.properties import ResourceProperties, TableSchemaProperties
from sprout.core.write_file import write_file


@fixture
def sprout_root(tmp_path, monkeypatch) -> Path:
    ROOT = tmp_path / "root"
    monkeypatch.setenv("SPROUT_ROOT", str(ROOT))
    return ROOT


@fixture
def path_to_data(sprout_root) -> Path:
    sprout_root.mkdir()
    file_path = sprout_root / "data.csv"
    data = "id,name,dob\n1,Alice,2000-09-22\n2,Bob,1996-11-12\n"
    return write_file(data, file_path)


@fixture
def resource_properties() -> dict:
    return ResourceProperties(
        name="resource-1",
        title="My First Resource",
        description="This is my first resource.",
        schema=TableSchemaProperties(),
    ).asdict


def test_accepts_matching_data(path_to_data, resource_properties):
    """Should accept data matching the table schema."""
    resource_properties["schema"]["fields"] += [
        {"name": "id", "type": "integer"},
        {"name": "name", "type": "string"},
        {"name": "dob", "type": "date"},
    ]

    assert check_raw_data(resource_properties, path_to_data) == path_to_data


def test_rejects_empty_data(path_to_data, resource_properties):
    """Should reject an empty data file."""
    write_file("", path_to_data)

    with raises(MismatchedRawDataError, match="the source is empty"):
        check_raw_data(resource_properties, path_to_data)


def test_rejects_uneven_data(path_to_data, resource_properties):
    """Should reject a data file with rows of different lengths."""
    path_to_data.write_text(
        path_to_data.read_text() + "3,Carl,1996-11-12,and,four,more,cells\n"
    )
    resource_properties["schema"]["fields"] += [
        {"name": "id", "type": "integer"},
        {"name": "name", "type": "string"},
        {"name": "dob", "type": "date"},
    ]

    with raises(MismatchedRawDataError) as error:
        check_raw_data(resource_properties, path_to_data)

    message = str(error.value)
    assert message.count("Extra Cell") == 4


@mark.parametrize(
    "fields, error_codes",
    [
        ([], ["Extra Label", "Blank Row"]),
        ([{"name": "id", "type": "integer"}], ["Extra Label", "Extra Cell"]),
        (
            [
                {"name": "id", "type": "integer"},
                {"name": "name", "type": "integer"},
                {"name": "dob", "type": "date"},
            ],
            ["Type Error"],
        ),
    ],
)
def test_rejects_mismatched_data(
    path_to_data, resource_properties, fields, error_codes
):
    """Should reject a data file that does not match the table schema."""
    resource_properties["schema"]["fields"] += fields

    with raises(MismatchedRawDataError) as error:
        check_raw_data(resource_properties, path_to_data)

    message = str(error.value)
    for code in error_codes:
        assert code in message


def test_accepts_matching_data_with_constraints(path_to_data, resource_properties):
    """Should accept a data file that conforms to schema constraints."""
    resource_properties["schema"]["fields"] += [
        {"name": "id", "type": "integer"},
        {"name": "name", "type": "string", "constraints": {"maxLength": 10}},
        {"name": "dob", "type": "date"},
    ]

    assert check_raw_data(resource_properties, path_to_data) == path_to_data


def test_rejects_data_violating_constraints(path_to_data, resource_properties):
    """Should reject a data file that violates schema constraints."""
    resource_properties["schema"]["fields"] += [
        {"name": "id", "type": "integer"},
        {"name": "name", "type": "string", "constraints": {"maxLength": 4}},
        {"name": "dob", "type": "date"},
    ]

    with raises(MismatchedRawDataError, match="Constraint Error"):
        check_raw_data(resource_properties, path_to_data)
