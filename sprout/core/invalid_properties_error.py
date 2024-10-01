from frictionless import Report


class InvalidPropertiesError(Exception):
    """Raised for invalid properties objects."""

    def __init__(self, report: Report, properties: dict, *args, **kwargs):
        """Initialises InvalidPropertiesError.

        Args:
            report: Validation report provided by Frictionless.
            properties: Invalid properties.
            *args: Non-keyword arguments.
            **kwargs: Keyword arguments.
        """
        # TODO: Consider if it's a problem for us that report.errors is not guaranteed
        # to include all errors.
        errors = [
            f"{error.title}: {error.description} {error.message}"
            for error in report.errors
        ]
        message = (
            f"Invalid properties provided:\n{properties}"
            f"\nThe following errors were found:\n{'\n'.join(errors)}"
        )
        super().__init__(message, *args, **kwargs)
