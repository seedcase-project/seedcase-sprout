from pytest import mark

from seedcase_sprout.check_datapackage.check_package_properties import (
    check_package_properties,
)

# Without recommendations


def test_passes_matching_properties():
    """Should pass properties matching the schema."""
    properties = {
        "name": "a name with spaces",
        "title": "A Title",
        "created": "2024-05-14T05:00:01+00:00",
        "version": "a version",
        "contributors": [{"email": "jane@doe.com"}],
        "sources": [{"email": "jane@doe.com"}],
    }

    assert check_package_properties(properties, check_recommendations=False) == []


@mark.parametrize("resources", [[], [{}], [{"name": "name", "path": "data.csv"}]])
def test_passes_matching_properties_without_checking_resources(resources):
    """Should pass matching package properties without checking individual resource
    properties."""
    properties = {"resources": resources}

    assert check_package_properties(properties, check_recommendations=False) == []


def test_fails_properties_with_resources_of_wrong_type():
    """Should fail properties if they have a `resources` field with a value of the wrong
    type."""
    properties = {"resources": 123}
    errors = check_package_properties(properties, check_recommendations=False)

    assert len(errors) == 1
    assert errors[0].validator == "type"
    assert errors[0].json_path == "$.resources"


def test_fails_properties_with_missing_required_fields():
    """Should fail properties with missing required fields."""
    properties = {
        "name": "a name",
        "licenses": [{"title": "my license"}],
    }

    errors = check_package_properties(properties, check_recommendations=False)

    assert len(errors) == 2
    assert all(error.validator == "required" for error in errors)
    assert {error.json_path for error in errors} == {
        "$.licenses[0].name",
        "$.licenses[0].path",
    }


def test_fails_properties_with_bad_type():
    """Should fail properties with a field of the wrong type."""
    properties = {"name": 123}
    errors = check_package_properties(properties, check_recommendations=False)

    assert len(errors) == 1
    assert errors[0].validator == "type"
    assert errors[0].json_path == "$.name"


def test_fails_properties_with_bad_format():
    """Should fail properties with a field of the wrong format."""
    properties = {"name": "a name", "homepage": "not a URL"}

    errors = check_package_properties(properties, check_recommendations=False)

    assert len(errors) == 1
    assert errors[0].validator == "format"
    assert errors[0].json_path == "$.homepage"


def test_fails_properties_with_pattern_mismatch():
    """Should fail properties with a field that does not match the pattern."""
    properties = {"name": "a name", "contributors": [{"path": "/a/bad/path"}]}

    errors = check_package_properties(properties, check_recommendations=False)

    assert len(errors) == 1
    assert errors[0].validator == "pattern"
    assert errors[0].json_path == "$.contributors[0].path"


# With recommendations


def test_passes_matching_properties_with_recommendations():
    """Should pass properties matching recommendations."""
    properties = {
        "name": "a-name-with-no-spaces",
        "title": "A Title",
        "id": "123",
        "created": "2024-05-14T05:00:01+00:00",
        "version": "3.2.1",
        "contributors": [{"title": "a contributor"}],
        "sources": [{"title": "a source"}],
        "licenses": [{"name": "a-license"}],
    }

    assert check_package_properties(properties, check_recommendations=True) == []


def test_fails_properties_with_missing_required_fields_with_recommendations():
    """Should fail properties with missing required fields."""
    errors = check_package_properties({}, check_recommendations=True)

    assert len(errors) == 3
    assert all(error.validator == "required" for error in errors)


def test_fails_properties_violating_recommendations():
    """Should fail properties that do not meet the recommendations."""
    properties = {
        "name": "a name with spaces",
        "id": "123",
        "version": "not semver",
        "contributors": [{"email": "jane@doe.com"}],
        "sources": [{"email": "jane@doe.com"}],
        "licenses": [{"name": "a-license"}],
    }

    errors = check_package_properties(properties, check_recommendations=True)

    assert len(errors) == 4
    assert {error.json_path for error in errors} == {
        "$.name",
        "$.version",
        "$.contributors[0].title",
        "$.sources[0].title",
    }
