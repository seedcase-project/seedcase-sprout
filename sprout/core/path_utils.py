from pathlib import Path

from sprout.core.get_ids import get_ids
from sprout.core.verify_is_dir import verify_is_dir
from sprout.core.verify_is_file import verify_is_file


def verify_is_dir_or_raise_error_with_id_context(path: Path, ids_path: Path):
    """Verifies if path is a directory or raises error with existing ids.

    Args:
        path: Path to verify.
        ids_path: Path to find existing ID's.

    Returns:
        Path, if path is a directory.

    Raises:
        NotADirectoryError: If the path is not a directory. The error message
            includes existing ID's.
    """
    try:
        verify_is_dir(path)
        return path
    except NotADirectoryError as e:
        existing_ids = get_ids(ids_path)
        raise NotADirectoryError(f"Existing ID's are {existing_ids}") from e


def verify_is_file_or_raise_error_with_id_context(path: Path, ids_path: Path):
    """Verifies if path is a file or raises error with existing ids.

    Args:
        path: Path to verify.
        ids_path: Path to find existing ID's.

    Returns:
        Path, if path is a file.

    Raises:
        FileNotFoundError: If the path is not a file. The error message
            includes existing ID's.
    """
    try:
        verify_is_file(path)
        return path
    except FileNotFoundError as e:
        existing_ids = get_ids(ids_path)
        raise FileNotFoundError(f"Existing ID's are {existing_ids}") from e
