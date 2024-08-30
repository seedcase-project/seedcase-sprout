from pathlib import Path

from sprout.core.create_relative_resource_data_path import (
    create_relative_resource_data_path,
)
from sprout.core.edit_resource_properties_field import edit_resource_properties_field
from sprout.core.verify_is_dir import verify_is_dir
from sprout.core.verify_resource_properties import verify_resource_properties


def create_resource_properties(path: Path, properties: dict) -> dict:
    """Creates a valid properties object for the specified resource.

    Args:
        path: the path to the resource folder
        properties: the properties of the resource

    Raises:
        NotADirectoryError: if path does not point to a directory
        InvalidResourcePropertiesError: if properties are not valid Frictionless
        resource properties

    Returns:
        the properties object, verified and updated
    """
    verify_is_dir(path)
    verify_resource_properties(properties)
    data_path = create_relative_resource_data_path(path)
    return edit_resource_properties_field(properties, "path", str(data_path))
