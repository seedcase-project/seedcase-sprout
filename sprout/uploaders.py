import pathlib
from typing import IO

from sprout.helpers.paths import path_raw_storage


def write_to_raw(file: IO, output_file: str) -> str:
    """Upload and save a file into raw storage.

    Args:
        file: The file as an IO object
        output_file: The name of the file to store.

    Returns:
        str: The path to the saved file.
    """
    output_path = path_raw_storage(0).joinpath(output_file)
    return write(file, output_path)


def write(file: IO, output_path: str) -> str:
    """Write a file to a specified path.

    Args:
        file: file to write
        output_path: path to write the file to

    Returns:
        str: The path to the written/saved file.
    """
    # Begin reading of file at the start of it
    file.seek(0)
    with open(output_path, "wb") as target:
        target.write(file.read())
    return output_path
