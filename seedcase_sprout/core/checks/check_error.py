import re


class CheckError(Exception):
    """Raised or returned when a properties object fails a single check."""

    def __init__(
        self,
        message: str,
        json_path: str,
        validator: str,
    ):
        """Initialises CheckError.

        Args:
            message: The error message.
            json_path: The path to the JSON field within the enclosing JSON object where
                the error occurred.
            validator: The name of the validator that failed.
        """
        self.message = message
        self.json_path = json_path
        self.validator = validator
        super().__init__(
            f"Error at `{json_path}` caused by validator `{validator}`: {message}"
        )

    @property
    def field(self) -> str | None:
        """Returns the name of the field where the error occurred.

        Returns None if the field cannot be specified.

        Returns:
            The name of the field.
        """
        if self.validator == "required":
            match = re.search("'(.*)' is a required property", self.message)
            if match:
                return match.group(1)

        return self.json_path.split(".")[-1] if "." in self.json_path else None
