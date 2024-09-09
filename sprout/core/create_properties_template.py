from datetime import datetime
from pathlib import Path

from sprout.core.write_json import write_json

RESOURCE_TEMPLATE = {
    "id": "",
    "name": "",
    "path": "",
    "type": "table",
    "title": "",
    "description": "",
    "homepage": "",
    "sources": [],
    "format": "csv",
    "mediatype": "text/csv",
    "encoding": "utf-8",
}


def package_template() -> dict:
    """Creates a package template object with default values for some properties.

    Returns:
        A package template object.
    """
    return {
        "id": "",
        "name": "",
        "title": "",
        "description": "",
        "homepage": "",
        "version": "0.1.0",
        "created": datetime.now().astimezone().isoformat(timespec="seconds"),
        "contributors": [],
        "keywords": [],
        "image": "",
        "licenses": [],
        "resources": [RESOURCE_TEMPLATE],
        "sources": [],
    }


def create_properties_template(path: Path) -> Path:
    """Saves a template datapackage.json file to the specified location.

    This file contains all required metadata fields with some default values provided.

    Args:
        path: The path where the file should be saved.

    Returns:
        The path where the file was saved.

    Raises:
        FileNotFoundError: If the path to the file cannot be resolved.
    """
    return write_json(package_template(), path)
