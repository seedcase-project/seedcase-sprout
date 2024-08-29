from pathlib import Path


def write_file(path: Path, string: str) -> Path:
    """Writes a file to the given path with the given content.

    Args:
        path: Path of the file to be created, including file name and extension.
        string: Content to be written to the file.

    Returns:
        A path to the file that was created.
    """
    path.write_text(string)

    return path
