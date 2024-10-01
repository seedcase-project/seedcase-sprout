from frictionless import Report
from frictionless.errors import PackageError

REQUIRED_PACKAGE_PROPERTIES = {
    "name",
    "id",
    "title",
    "description",
    "version",
    "created",
}


def verify_required_package_properties(report: Report, properties: dict) -> Report:
    """Verifies that all required fields are present on `properties` and not empty.

    The results are added to the `report` object.

    Args:
        report: A Frictionless validation report to add the results to.
        properties: The package properties to verify.

    Returns:
        The updated validation report.
    """
    for field in REQUIRED_PACKAGE_PROPERTIES:
        if properties.get(field) in ["", None]:
            error = PackageError(
                note=f"'{field}' is a required property and cannot be empty."
            )
            report.errors.append(error)
    report.valid = not report.errors
    report.stats["errors"] = len(report.errors)
    return report
