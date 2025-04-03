import re
from pathlib import Path

from seedcase_sprout.core.sprout_checks.constants import BATCH_FILE_NAME_PATTERN


def _check_batch_file_name(path: Path) -> Path:
    """Check that the batch file name is in the expected pattern.

    Args:
        path: Path to the batch file.

    Returns:
        The path, if it is in the expected pattern.

    Raises:
        ValueError: If the path is not in the expected pattern.
    """
    filename = path.name

    if re.fullmatch(BATCH_FILE_NAME_PATTERN, filename) is None:
        raise ValueError(
            f"Batch file name '{filename}' is not in the expected pattern:"
            f"{BATCH_FILE_NAME_PATTERN}"
        )
    return path
