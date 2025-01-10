from pytest import fixture, mark

from seedcase_sprout.core.sprout_checks.check_required_package_properties_not_blank import (  # noqa: E501
    check_required_package_properties_not_blank,
)
from seedcase_sprout.core.sprout_checks.get_blank_value_for_type import (
    get_blank_value_for_type,
)
from seedcase_sprout.core.sprout_checks.required_fields import (
    PACKAGE_SPROUT_REQUIRED_FIELDS,
)


@fixture
def properties():
    return {
        "name": "package-1",
        "id": "abc1",
        "title": "Package 1",
        "description": "A package.",
        "version": "1.0.0",
        "created": "2024-05-14T05:00:01+00:00",
        "licenses": [{"name": "a-license"}],
        "contributors": [{"title": "a contributor"}],
        "sources": [{"title": "a source"}],
    }


def test_passes_if_all_required_fields_populated(properties):
    """Should pass if all required fields are present and populated."""
    assert check_required_package_properties_not_blank(properties) == []


def test_passes_if_all_required_fields_missing():
    """Should pass if all required fields are missing."""
    assert check_required_package_properties_not_blank({}) == []


@mark.parametrize(
    "field,value,json_path",
    [
        *[
            (name, get_blank_value_for_type(type), f"$.{name}")
            for name, type in PACKAGE_SPROUT_REQUIRED_FIELDS.items()
        ],
        ("contributors", [{"title": ""}], "$.contributors[0].title"),
        ("sources", [{"title": ""}], "$.sources[0].title"),
        ("licenses", [{"name": ""}], "$.licenses[0].name"),
        ("licenses", [{"path": ""}], "$.licenses[0].path"),
    ],
)
def test_fails_if_required_field_blank(properties, field, value, json_path):
    """Should fail if a required field is present but blank."""
    properties[field] = value

    errors = check_required_package_properties_not_blank(properties)

    assert len(errors) == 1
    assert errors[0].json_path == json_path
    assert errors[0].validator == "blank"


def test_fails_if_all_required_fields_blank():
    """Should fail if all required fields are present but blank."""
    properties = {
        "name": "",
        "id": "",
        "title": "",
        "description": "",
        "version": "",
        "created": "",
        "licenses": [{"name": "", "path": ""}],
        "contributors": [{"title": ""}],
        "sources": [{"title": ""}],
    }

    errors = check_required_package_properties_not_blank(properties)

    assert len(errors) == 10
    assert all(error.validator == "blank" for error in errors)
