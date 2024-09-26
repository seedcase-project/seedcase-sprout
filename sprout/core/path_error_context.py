from pathlib import Path
from typing import Literal

from sprout.core.get_ids import get_ids
from sprout.core.verify_is_dir import verify_is_dir


def verify_is_dir_or_raise_error_with_id_context(
    path: Path, ids_path: Path, context: Literal["package", "resource"]
) -> Path:
    """Verifies if path is a directory or raises error with existing ids.

    Args:
        path: Path to verify.
        ids_path: Path to find existing IDs.
        context: The context of the path. Either "package" or "resource".

    Returns:
        Path, if path is a directory.

    Raises:
        NotADirectoryError: If the path is not a directory. The error message
            includes existing IDs.
    """
    try:
        return verify_is_dir(path)
    except NotADirectoryError as e:
        raise NotADirectoryError(
            f"Existing {context} IDs are {get_ids(ids_path)}"
        ) from e
