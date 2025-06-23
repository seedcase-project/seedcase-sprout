from pathlib import Path


def write_file(string: str, path: Path) -> Path:
    """Write the `string` to a file from `path`.

    The parent folder of the file in `path` must exist.
    If the file already exists, it will be overwritten.

    Args:
        string: The content to be written to the file.
        path: A path of the file to be created, including the file name and extension.

    Returns:
        A path to the file that was created.

    Raises:
        FileNotFoundError: If the parent folder of the file doesn't exist.
    """
    path.write_text(string)

    return path
