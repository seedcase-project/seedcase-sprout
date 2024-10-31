from pathlib import Path

from frictionless import Error


class MismatchedRawDataError(Exception):
    """Raised when a raw data file does not conform to the resource properties."""

    def __init__(self, errors: list[Error], data_path: Path, *args, **kwargs):
        """Initialises MismatchedRawDataError.

        Args:
            errors: List of Frictionless errors.
            data_path: Path to the raw data file.
            *args: Non-keyword arguments.
            **kwargs: Keyword arguments.
        """
        errors = [
            f"{error.title}: {error.description} {error.message}" for error in errors
        ]
        message = (
            f"The raw data file at `{data_path}` does not conform to the corresponding "
            "resource properties."
            f"\nThe following errors were found:\n{'\n'.join(errors)}"
        )
        super().__init__(message, *args, **kwargs)
