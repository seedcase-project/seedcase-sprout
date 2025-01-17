from pathlib import Path

from pytest import fixture, mark, raises

from seedcase_sprout.core.checks.check_error import CheckError
from seedcase_sprout.core.properties import PackageProperties, ResourceProperties
from seedcase_sprout.core.sprout_checks.check_properties import check_properties
from seedcase_sprout.core.sprout_checks.get_blank_value_for_type import (
    get_blank_value_for_type,
)
from seedcase_sprout.core.sprout_checks.required_fields import (
    PACKAGE_SPROUT_REQUIRED_FIELDS,
    RESOURCE_SPROUT_REQUIRED_FIELDS,
)


@fixture
def properties():
    return PackageProperties(
        name="package-1",
        id="abc1",
        title="Package 1",
        description="A package.",
        version="1.0.0",
        created="2024-05-14T05:00:01+00:00",
        licenses=[{"name": "a-license"}],
        contributors=[{"title": "a contributor"}],
        sources=[{"title": "a source"}],
        resources=[
            ResourceProperties(
                name="resource-1",
                path=str(Path("resources", "1", "data.parquet")),
                title="Resource 1",
                description="A resource.",
            ),
            ResourceProperties(
                name="resource-2",
                path=str(Path("resources", "2", "data.parquet")),
                title="Resource 2",
                description="A second resource.",
            ),
        ],
    ).compact_dict


@mark.parametrize("check_required", [True, False])
def test_check_passes_full_properties(properties, check_required):
    """Should pass if all required fields are present and correct."""
    assert check_properties(properties, check_required=check_required) == properties


def test_passes_partial_properties_without_required_check():
    """Should pass properties with missing required fields when these are not
    enforced."""
    assert check_properties({}, check_required=False) == {}


@mark.parametrize("field", [*PACKAGE_SPROUT_REQUIRED_FIELDS.keys(), "resources"])
def test_raises_error_if_package_required_field_is_missing(properties, field):
    """Should raise an error if a required field is missing among the package
    properties."""
    del properties[field]

    with raises(ExceptionGroup) as error_info:
        check_properties(properties, check_required=True)

    errors = error_info.value.exceptions
    assert len(errors) == 1
    assert errors[0].json_path == f"$.{field}"
    assert errors[0].validator == "required"


@mark.parametrize("field", RESOURCE_SPROUT_REQUIRED_FIELDS.keys())
def test_raises_error_if_resource_required_field_is_missing(properties, field):
    """Should raise an error if a required field is missing among the resource
    properties."""
    del properties["resources"][0][field]

    with raises(ExceptionGroup) as error_info:
        check_properties(properties, check_required=True)

    errors = error_info.value.exceptions
    assert len(errors) == 1
    assert errors[0].json_path == f"$.resources[0].{field}"
    assert errors[0].validator == "required"


@mark.parametrize("check_required", [True, False])
@mark.parametrize("name,type", PACKAGE_SPROUT_REQUIRED_FIELDS.items())
def test_raises_error_if_package_field_is_blank(properties, name, type, check_required):
    """Should raise an error if there is one required package field that is present but
    blank."""
    properties[name] = get_blank_value_for_type(type)

    with raises(ExceptionGroup) as error_info:
        check_properties(properties, check_required=check_required)

    blank_errors = [
        error for error in error_info.value.exceptions if error.validator == "blank"
    ]

    assert len(blank_errors) == 1
    assert blank_errors[0].json_path == f"$.{name}"


@mark.parametrize("check_required", [True, False])
@mark.parametrize("name,type", RESOURCE_SPROUT_REQUIRED_FIELDS.items())
def test_raises_error_if_resource_field_is_blank(
    properties, name, type, check_required
):
    """Should raise an error if there is one required resource field that is present
    but blank."""
    properties["resources"][0][name] = get_blank_value_for_type(type)

    with raises(ExceptionGroup) as error_info:
        check_properties(properties, check_required=check_required)

    blank_errors = [
        error for error in error_info.value.exceptions if error.validator == "blank"
    ]

    assert len(blank_errors) == 1
    assert blank_errors[0].json_path == f"$.resources[0].{name}"


@mark.parametrize("check_required", [True, False])
def test_raises_error_if_there_are_both_package_and_resource_errors(
    properties, check_required
):
    """Should raise `CheckError`s if there are both package and resource errors."""
    properties["name"] = "space in name"
    properties["title"] = 123
    properties["resources"][0]["name"] = "space in name"
    properties["resources"][1]["path"] = "/bad path"
    properties["resources"][1]["data"] = "some data"

    with raises(ExceptionGroup) as error_info:
        check_properties(properties, check_required=check_required)

    errors = error_info.value.exceptions
    assert [error.json_path for error in errors] == [
        "$.name",
        "$.resources[0].name",
        "$.resources[1].data",
        "$.resources[1].path",
        "$.resources[1].path",
        "$.title",
    ]
    assert [error.validator for error in errors] == [
        "pattern",
        "pattern",
        "inline-data",
        "pattern",
        "pattern",
        "type",
    ]


@mark.parametrize("check_required", [True, False])
def test_raises_error_for_only_sprout_specific_errors(properties, check_required):
    """Errors should be triggered by only those Data Package standard violations that
    are relevant for Sprout."""
    properties["resources"][0]["path"] = 123

    with raises(ExceptionGroup) as error_info:
        check_properties(properties, check_required=check_required)

    errors = error_info.value.exceptions
    assert errors == (
        CheckError("123 is not of type 'string'", "$.resources[0].path", "type"),
    )
