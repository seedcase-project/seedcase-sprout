from pathlib import Path


def write_file(string: str, path: Path) -> Path:
    """Writes a file to the given path with the given content.

    Args:
        string: Content to be written to the file.
        path: Path of the file to be created, including file name and extension.

    Returns:
        A path to the file that was created.
    """
    path.write_text(string)

    return path
