import os
from typing import IO

from config.settings import PERSISTENT_STORAGE_PATH
from sprout.helpers.paths import path_raw_storage


def write_to_raw(file: IO, output_file: str) -> str:
    """Upload and save a file into raw storage.

    Args:
        file: The file as an IO object
        output_file: The name of the file to store.

    Returns:
        str: The path to the saved file.
    """
    raw_folder = path_raw_storage()
    output_path = f"{raw_folder}/{output_file}"
    return write(file, output_path)


def write(file: IO, output_path: str) -> str:
    # Begin reading of file at the start of it
    file.seek(0)
    with open(output_path, "wb") as target:
        target.write(file.read())
    return output_path
