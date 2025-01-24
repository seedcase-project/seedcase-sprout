from pathlib import Path

from seedcase_sprout.core.check_is_dir import check_is_dir
from seedcase_sprout.core.create_dirs import create_dir
from seedcase_sprout.core.create_id_path import create_id_path
from seedcase_sprout.core.create_next_id import create_next_id
from seedcase_sprout.core.create_properties_path import create_properties_path
from seedcase_sprout.core.create_readme_path import create_readme_path
from seedcase_sprout.core.create_readme_text import create_readme_text
from seedcase_sprout.core.get_ids import get_ids
from seedcase_sprout.core.properties import PackageProperties
from seedcase_sprout.core.write_file import write_file
from seedcase_sprout.core.write_json import write_json


def create_package_structure(path: Path) -> list[Path]:
    """Sets up the folder structure for a new package.

    This is the first function to use to create a new data package. It assigns a package
    ID and then creates a package folder and all the necessary files for a package
    (excluding the resources), outputting the file paths for the created files.

    Args:
        path: The path to the folder containing the packages. Use `path_packages()`
            to provide the correct path location.

    Returns:
        A list of paths to the two created files, datapackage.json and
            README.md, and the created folder `resources/`.

    Raises:
        NotADirectoryError: If the directory in the path doesn't exist.
        FileNotFoundError: If a file could not be created.
        TypeError: If `datapackage.json` could not be created.

    Examples:
        ```{python}
        #| output: true
        import tempfile
        from pathlib import Path

        import seedcase_sprout.core as sp

        # Create a temporary directory for the example
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_path = Path(temp_dir)

            # Create a package structure
            sp.create_package_structure(path=temp_path)
        ```
    """
    check_is_dir(path)
    ids = get_ids(path)
    id = create_next_id(ids)
    package_path = create_id_path(path, id)
    create_dir(package_path)

    properties = PackageProperties.default().compact_dict
    properties_path = create_properties_path(package_path)
    readme = create_readme_text(properties)
    readme_path = create_readme_path(package_path)

    return [
        write_json(properties, properties_path),
        write_file(readme, readme_path),
        create_dir(package_path / "resources"),
    ]
