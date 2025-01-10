from seedcase_sprout.core.checks.check_error import CheckError


class FailedCheckError(Exception):
    """Raised when a properties object fails at least one check."""

    def __init__(self, message: str, errors: list[CheckError]):
        """Initialises FailedCheckError.

        Args:
            message: The error message.
            errors: The list of all individual errors that triggered this error.
        """
        self.message = message
        self.errors = errors
        super().__init__(self.__str__())

    def __str__(self) -> str:
        """Returns a user-friendly string representation of the error.

        Returns:
            The string representation.
        """
        return f"{self.message}\nThe following checks failed:\n" + "\n".join(
            [str(error) for error in self.errors]
        )

    def __repr__(self) -> str:
        """Returns a developer-friendly, unambiguous representation of the error.

        Returns:
            The developer-friendly representation.
        """
        return f"FailedCheckError(message={self.message!r}, errors={self.errors!r})"
