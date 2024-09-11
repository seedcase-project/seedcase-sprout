from pathlib import Path

from platformdirs import user_data_path


def create_root_path() -> Path:
    """Creates the path to Sprout root.

    Returns:
        A Path with the Sprout root directory tied to the user.
    """
    root_path = user_data_path("sprout")

    return root_path
