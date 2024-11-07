from datetime import datetime
from re import sub


def get_iso_timestamp() -> str:
    """Generates a timestamp compliant with the Data Package spec.

    Returns:
        The timestamp as a string. E.g. `2024-05-14T05:00:01+00:00`.
    """
    return datetime.now().astimezone().isoformat(timespec="seconds")


def get_compact_iso_timestamp() -> str:
    """Generates a compact timestamp.

    Returns:
        The timestamp as a string. E.g. `20240514-05000100`.
    """
    return sub(r"\W", "", get_iso_timestamp()).replace("T", "-")
