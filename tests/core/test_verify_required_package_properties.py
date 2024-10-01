from dataclasses import asdict

from frictionless import Report
from frictionless.errors import PackageError
from pytest import fixture, mark

from sprout.core.properties import PackageProperties
from sprout.core.verify_required_package_properties import (
    REQUIRED_PACKAGE_PROPERTIES,
    verify_required_package_properties,
)


@fixture
def properties():
    return asdict(
        PackageProperties(
            name="my-package",
            id="123-abc-123",
            title="My Package",
            description="This is my package.",
            version="2.0.0",
            created="2024-05-14T05:00:01+00:00",
        )
    )


@mark.parametrize("field", REQUIRED_PACKAGE_PROPERTIES)
@mark.parametrize("empty_value", ["", None])
def test_updates_report_correctly_one_error(properties, field, empty_value):
    """Should update the report correctly when there is one error."""
    properties[field] = empty_value

    report = verify_required_package_properties(
        Report(valid=True, stats={}), properties
    )

    assert not report.valid
    assert report.stats["errors"] == 1
    assert len(report.errors) == 1
    assert report.errors[0].note == (
        f"'{field}' is a required property and cannot be empty."
    )


def test_updates_report_correctly_multiple_errors():
    """Should update the report correctly when there are multiple errors."""
    existing_error = PackageError(note="Another type of error.")

    report = verify_required_package_properties(
        Report(valid=False, stats={"errors": 1}, errors=[existing_error]), {}
    )

    assert not report.valid
    assert report.stats["errors"] == 7
    assert len(report.errors) == 7
    notes = [error.note for error in report.errors]
    for field in REQUIRED_PACKAGE_PROPERTIES:
        assert f"'{field}' is a required property and cannot be empty." in notes


def test_leaves_report_unchanged_no_error(properties):
    """Should not update the report when there are no errors."""
    report = verify_required_package_properties(
        Report(valid=True, stats={}), properties
    )

    assert report.valid
    assert report.stats["errors"] == 0
    assert not report.errors
