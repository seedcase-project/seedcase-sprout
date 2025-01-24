from pathlib import Path

from seedcase_sprout.core.check_is_dir import check_is_dir
from seedcase_sprout.core.create_relative_resource_data_path import (
    create_relative_resource_data_path,
)
from seedcase_sprout.core.properties import ResourceProperties
from seedcase_sprout.core.sprout_checks.check_resource_properties import (
    check_resource_properties,
)


def create_resource_properties(
    path: Path, properties: ResourceProperties
) -> ResourceProperties:
    """Creates a valid properties object for the specified resource.

    This function sets up and structures a new resource property by taking
    the fields given in the `properties` argument to fill them and prepare
    them to be added to the `datapackage.json` file.

    Args:
        path: The path to the resource `id` folder; use `path_resource()`
            to provide the correct path or use the output of
            `create_resource_structure()`.
        properties: The properties of the resource; must be given as a
            `ResourceProperties` object following the Data Package specification.
            See the `ResourceProperties` help documentation for details
            on what can or needs to be filled in.

    Returns:
        The properties object, verified and updated.

    Raises:
        NotADirectoryError: If path does not point to a directory.
        ExceptionGroup: If there is an error in the properties. A group of
            `CheckError`s, one error per failed check.
    """
    check_is_dir(path)
    properties.path = str(create_relative_resource_data_path(path))
    check_resource_properties(properties.compact_dict)
    return properties
