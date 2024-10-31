from frictionless import Error, Report


def get_report_errors(report: Report) -> list[Error]:
    """Returns all errors in a Frictionless report.

    Args:
        report: The report to get the errors from.

    Returns:
        The errors in the report.
    """
    return [
        error
        for error in report.errors
        + [error for task in report.tasks for error in task.errors]
    ]
