from pytest import fixture, mark, raises

from seedcase_sprout.core.checks.check_error_matcher import CheckErrorMatcher
from seedcase_sprout.core.properties import PackageProperties
from seedcase_sprout.core.sprout_checks.check_package_properties import (
    check_package_properties,
)
from seedcase_sprout.core.sprout_checks.failed_check_error import FailedCheckError
from seedcase_sprout.core.sprout_checks.get_blank_value_for_type import (
    get_blank_value_for_type,
)
from seedcase_sprout.core.sprout_checks.required_fields import (
    PACKAGE_SPROUT_REQUIRED_FIELDS,
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
    ).compact_dict


def test_passes_full_package_properties(properties):
    """Should pass if all required fields are present and correct."""
    assert check_package_properties(properties) == properties


@mark.parametrize("resources", [[], [{}], [{"name": "name", "path": "data.csv"}]])
def test_passes_without_checking_resources(resources, properties):
    """Should pass matching package properties without checking individual resource
    properties."""
    properties["resources"] = resources

    assert check_package_properties(properties) == properties


def test_fails_with_resources_of_wrong_type(properties):
    """Should fail if there is a `resources` field with a value of the wrong type."""
    properties["resources"] = 123

    with raises(FailedCheckError) as error:
        check_package_properties(properties)

    errors = error.value.errors
    assert len(errors) == 1
    assert errors[0].validator == "type"
    assert errors[0].json_path == "$.resources"


@mark.parametrize("field", PACKAGE_SPROUT_REQUIRED_FIELDS.keys())
def test_fails_if_required_field_missing(properties, field):
    """Should fail if a required field is missing."""
    del properties[field]

    with raises(FailedCheckError) as error:
        check_package_properties(properties)

    errors = error.value.errors
    assert len(errors) == 1
    assert errors[0].json_path == f"$.{field}"
    assert errors[0].validator == "required"


def test_fails_if_nested_required_fields_missing():
    """Should fail if nested required fields are missing."""
    properties = PackageProperties(
        name="package-1",
        id="abc1",
        title="Package 1",
        description="A package.",
        version="1.0.0",
        created="2024-05-14T05:00:01+00:00",
        licenses=[{}],
        contributors=[{}],
        sources=[{}],
    ).compact_dict

    with raises(FailedCheckError) as error:
        check_package_properties(properties)

    required_errors = [
        error for error in error.value.errors if error.validator == "required"
    ]
    assert [error.json_path for error in required_errors] == [
        "$.contributors[0].title",
        "$.licenses[0].name",
        "$.licenses[0].path",
        "$.sources[0].title",
    ]


def test_fails_with_mismatched_pattern(properties):
    """Should fail if `name` violates the pattern."""
    properties["name"] = "a name with spaces"

    with raises(FailedCheckError) as error:
        check_package_properties(properties)

    errors = error.value.errors
    assert len(errors) == 1
    assert errors[0].json_path == "$.name"
    assert errors[0].validator == "pattern"


def test_fails_with_mismatched_format(properties):
    """Should fail if `homepage` violates the format."""
    properties["homepage"] = "not a URL"

    with raises(FailedCheckError) as error:
        check_package_properties(properties)

    errors = error.value.errors
    assert len(errors) == 1
    assert errors[0].json_path == "$.homepage"
    assert errors[0].validator == "format"


@mark.parametrize("name,type", PACKAGE_SPROUT_REQUIRED_FIELDS.items())
def test_fails_if_fields_blank(properties, name, type):
    """Should fail if there is one required field that is present but blank."""
    properties[name] = get_blank_value_for_type(type)

    with raises(FailedCheckError) as error:
        check_package_properties(properties)

    blank_errors = [error for error in error.value.errors if error.validator == "blank"]

    assert len(blank_errors) == 1
    assert blank_errors[0].json_path == f"$.{name}"


def test_fails_if_nested_fields_blank():
    """Should fail if required nested fields are present but blank."""
    properties = PackageProperties(
        name="package-1",
        id="abc1",
        title="Package 1",
        description="A package.",
        version="1.0.0",
        created="2024-05-14T05:00:01+00:00",
        licenses=[{"name": "", "path": ""}],
        contributors=[{"title": ""}],
        sources=[{"title": ""}],
    ).compact_dict

    with raises(FailedCheckError) as error:
        check_package_properties(properties)

    blank_errors = [error for error in error.value.errors if error.validator == "blank"]
    assert [error.json_path for error in blank_errors] == [
        "$.contributors[0].title",
        "$.licenses[0].name",
        "$.licenses[0].path",
        "$.sources[0].title",
    ]


def test_ignored_errors_should_not_make_check_fail():
    """Check should not fail if triggered by an error that is ignored."""
    assert (
        check_package_properties({}, ignore=[CheckErrorMatcher(validator="required")])
        == {}
    )


def test_excludes_ignored_errors_from_output(properties):
    """Errors that are ignored should not be in error output."""
    properties["name"] = "invalid name with spaces"
    properties["homepage"] = "not a URL"

    with raises(FailedCheckError) as error:
        check_package_properties(
            properties, ignore=[CheckErrorMatcher(json_path="homepage")]
        )

    errors = error.value.errors
    assert len(errors) == 1
    assert errors[0].json_path == "$.name"
    assert errors[0].validator == "pattern"
