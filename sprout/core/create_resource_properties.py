from pathlib import Path

from sprout.core.create_relative_resource_data_path import (
    create_relative_resource_data_path,
)
from sprout.core.edit_resource_properties_field import edit_resource_properties_field
from sprout.core.verify_is_dir import verify_is_dir
from sprout.core.verify_resource_properties import verify_resource_properties


def create_resource_properties(path: Path, properties: dict) -> dict:
    """Creates a valid properties object for the specified resource.

    This function sets up and structures a new resource property by taking
    the fields given in the `properties` argument to fill them and prepare
    them to be added to the `datapackage.json` file.

    Args:
        path: the path to the resource `id` folder; use `path_resource()`
            to provide the correct path or use the output of
            `create_resource_structure()`
        properties: the properties of the resource; must be given as a
            JSON object following the Data Package specification; use
            `view_resource_properties_template()` to get a JSON object
            that follows the Frictionless Data Package standard

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
