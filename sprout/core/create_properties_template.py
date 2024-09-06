from pathlib import Path

from sprout.core.write_json import write_json


def create_properties_template(path: Path) -> Path:
    """Saves a template datapackage.json file to the specified location.

    This file contains all required metadata fields, leaving them blank.

    Args:
        path: The path where the file should be saved.

    Returns:
        The path where the file was saved.

    Raises:
        FileNotFoundError: If the path to the file cannot be resolved.
    """
    resource_properties = {
        "id": "",
        "name": "",
        "path": "",
        "type": "",
        "title": "",
        "description": "",
        "homepage": "",
        "sources": [],
        "format": "",
        "mediatype": "",
        "encoding": "",
    }
    package_properties = {
        "id": "",
        "name": "",
        "title": "",
        "description": "",
        "homepage": "",
        "version": "",
        "created": "",
        "contributors": [],
        "keywords": [],
        "image": "",
        "licenses": [],
        "resources": [resource_properties],
        "sources": [],
    }

    return write_json(package_properties, path)
