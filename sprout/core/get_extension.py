from pathlib import Path

from sprout.core.verify_is_file import verify_is_file


def get_extension(path: Path) -> str:
    """Returns the extension of the file `path` points to without a leading `.`.

    Args:
        path: The path to the file.

    Returns:
        The extension of the file.

    Raises:
        FileNotFoundError: If `path` does not point to a file.
    """
    verify_is_file(path)
    return path.suffix[1:]
