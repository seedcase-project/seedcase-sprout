from pathlib import Path

from pytest import fixture, mark, raises

from seedcase_sprout.core.checks.check_error import CheckError
from seedcase_sprout.core.properties import ResourceProperties
from seedcase_sprout.core.sprout_checks.check_resource_properties import (
    check_resource_properties,
)
from seedcase_sprout.core.sprout_checks.failed_check_error import FailedCheckError
from seedcase_sprout.core.sprout_checks.get_blank_value_for_type import (
    get_blank_value_for_type,
)
from seedcase_sprout.core.sprout_checks.required_fields import (
    RESOURCE_SPROUT_REQUIRED_FIELDS,
)


@fixture
def properties():
    return ResourceProperties(
        name="resource-1",
        path=str(Path("resources", "1", "data.parquet")),
        title="Resource 1",
        description="A resource.",
    ).compact_dict


@mark.parametrize("check_required", [True, False])
def test_passes_full_resource_properties(properties, check_required):
    """Should pass if all required fields are present and correct."""
    assert (
        check_resource_properties(properties, check_required=check_required)
        == properties
    )


@mark.parametrize(
    "field",
    RESOURCE_SPROUT_REQUIRED_FIELDS.keys(),
)
def test_fails_if_required_field_missing(properties, field):
    """Should fail if a required field is missing."""
    del properties[field]

    with raises(FailedCheckError) as error:
        check_resource_properties(properties, check_required=True)

    errors = error.value.errors
    assert len(errors) == 1
    assert errors[0].json_path == f"$.{field}"
    assert errors[0].validator == "required"


@mark.parametrize("check_required", [True, False])
@mark.parametrize("path", ["", [], str(Path("resources", "1")), "/bad/path/data.csv"])
def test_fails_if_data_path_incorrect_(properties, path, check_required):
    """Should fail if `path` contains no resource ID, is not a string, or is
    otherwise malformed."""
    properties["path"] = path

    with raises(FailedCheckError) as error:
        check_resource_properties(properties, check_required=check_required)

    errors = error.value.errors
    assert len(errors) >= 1
    assert all(error.json_path.endswith("path") for error in errors)


@mark.parametrize("check_required", [True, False])
def test_fails_with_inline_data(properties, check_required):
    """Should fail if inline data is set."""
    properties["data"] = "some data"

    with raises(FailedCheckError) as error:
        check_resource_properties(properties, check_required=check_required)

    errors = error.value.errors
    assert len(errors) == 1
    assert errors[0].json_path == "$.data"
    assert errors[0].validator == "inline-data"


@mark.parametrize("check_required", [True, False])
@mark.parametrize("name,type", RESOURCE_SPROUT_REQUIRED_FIELDS.items())
def test_fails_if_fields_blank(properties, name, type, check_required):
    """Should fail if there is one required field that is present but blank."""
    properties[name] = get_blank_value_for_type(type)

    with raises(FailedCheckError) as error:
        check_resource_properties(properties, check_required=check_required)

    blank_errors = [error for error in error.value.errors if error.validator == "blank"]

    assert len(blank_errors) == 1
    assert blank_errors[0].json_path == f"$.{name}"


@mark.parametrize("check_required", [True, False])
def test_fails_with_mismatched_pattern(properties, check_required):
    """Should fail if `name` violates the pattern."""
    properties["name"] = "a name with spaces"

    with raises(FailedCheckError) as error:
        check_resource_properties(properties, check_required=check_required)

    errors = error.value.errors
    assert len(errors) == 1
    assert errors[0].json_path == "$.name"
    assert errors[0].validator == "pattern"


@mark.parametrize("check_required", [True, False])
def test_fails_with_mismatched_format(properties, check_required):
    """Should fail if `homepage` violates the format."""
    properties["homepage"] = "not a URL"

    with raises(FailedCheckError) as error:
        check_resource_properties(properties, check_required=check_required)

    errors = error.value.errors
    assert len(errors) == 1
    assert errors[0].json_path == "$.homepage"
    assert errors[0].validator == "format"


@mark.parametrize("check_required", [True, False])
def test_fails_with_mismatched_type(properties, check_required):
    """Should fail if `name` violates the type constraint."""
    properties["name"] = 123

    with raises(FailedCheckError) as error:
        check_resource_properties(properties, check_required=check_required)

    errors = error.value.errors
    assert len(errors) == 1
    assert errors[0].json_path == "$.name"
    assert errors[0].validator == "type"


@mark.parametrize("check_required", [True, False])
def test_fails_with_only_sprout_specific_errors(properties, check_required):
    """Errors should be triggered by only those Data Package standard violations that
    are relevant for Sprout."""
    properties["path"] = 123

    with raises(FailedCheckError) as error:
        check_resource_properties(properties, check_required=check_required)

    errors = error.value.errors
    assert errors == [CheckError("123 is not of type 'string'", "$.path", "type")]


def test_passes_partial_resource_properties_without_required_check():
    """Should pass properties with missing required fields when these are not
    enforced."""
    assert check_resource_properties({}, check_required=False) == {}
