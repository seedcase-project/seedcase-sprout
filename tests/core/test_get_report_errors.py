from frictionless import Error, Report, ReportTask

from sprout.core.get_report_errors import get_report_errors


def test_gets_errors_correctly():
    """Extracts errors from both the report itself and its tasks."""
    expected_errors = [Error(note=f"error {n}") for n in range(5)]
    report = Report(
        valid=False,
        errors=expected_errors[:2],
        tasks=[
            create_report_task([expected_errors[2]]),
            create_report_task(expected_errors[3:]),
        ],
        stats={"tasks": 2, "errors": len(expected_errors)},
    )

    assert get_report_errors(report) == expected_errors


def create_report_task(errors: list[Error]) -> ReportTask:
    return ReportTask(
        errors=errors,
        name="test",
        valid=False,
        place="test",
        type="test",
        labels=[],
        stats={"errors": len(errors)},
    )
