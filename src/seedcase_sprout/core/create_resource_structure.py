from pathlib import Path

from seedcase_sprout.core.create_dirs import create_dirs
from seedcase_sprout.core.create_id_path import create_id_path
from seedcase_sprout.core.create_next_id import create_next_id
from seedcase_sprout.core.create_resource_batch_path import create_resource_batch_path
from seedcase_sprout.core.get_ids import get_ids
from seedcase_sprout.core.internals import _check_is_dir


def create_resource_structure(path: Path) -> list[Path]:
    """Creates the directory structure of a new resource.

    This is the first function to use to set up the structure for a data
    resource. It creates the paths for a new data resource in a specific
    (existing) package by creating the folder setup described in the
    [Outputs](https://sprout.seedcase-project.org/docs/design/outputs) section
    on the Sprout website. It creates two paths: the `resources/<id>/` path and the
    `resources/<id>/batch/` path. The output is a list of these two path objects.

    Args:
       path: Path to the package folder.

    Returns:
       A list of the two created directories:

          - A path to the resource directory and
          - A path to the batch data directory.

    Raises:
       NotADirectoryError: If path is not an existing directory.

    Examples:
        ```{python}
        import seedcase_sprout.core as sp

        with sp.ExamplePackage(with_resources=False):
            sp.create_resource_structure()
        ```
    """
    _check_is_dir(path)
    path_resources = path / "resources"
    path_resources.mkdir(exist_ok=True)

    existing_ids = get_ids(path_resources)
    next_id = create_next_id(existing_ids)

    resource_path = create_id_path(path_resources, next_id)
    resource_batch_path = create_resource_batch_path(resource_path)

    return create_dirs([resource_path, resource_batch_path])
