from pathlib import Path

from sprout.core.get_ids import get_ids
from sprout.core.verify_is_dir import verify_is_dir
from sprout.core.verify_is_file import verify_is_file


def verify_is_dir_or_raise_error_with_id_context(path: Path, ids_path: Path):
    """Verifies if path is a directory or raises error with existing ids.

    Args:
        path: Path to verify.
        ids_path: Path to find existing IDs.

    Returns:
        Path, if path is a directory.

    Raises:
        NotADirectoryError: If the path is not a directory. The error message
            includes existing IDs.
    """
    try:
        return verify_is_dir(path)
    except NotADirectoryError as e:
        raise NotADirectoryError(f"Existing IDs are {get_ids(ids_path)}") from e


def verify_is_file_or_raise_error_with_id_context(path: Path, ids_path: Path):
    """Verifies if path is a file or raises error with existing ids.

    Args:
        path: Path to verify.
        ids_path: Path to find existing IDs.

    Returns:
        Path, if path is a file.

    Raises:
        FileNotFoundError: If the path is not a file. The error message
            includes existing IDs.
    """
    try:
        verify_is_file(path)
        return path
    except FileNotFoundError as e:
        existing_ids = get_ids(ids_path)
        raise FileNotFoundError(f"Existing IDs are {existing_ids}") from e
