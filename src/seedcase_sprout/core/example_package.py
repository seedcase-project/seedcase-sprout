import os
import tempfile
from contextlib import AbstractContextManager
from pathlib import Path

from seedcase_sprout.core.as_readme_text import as_readme_text
from seedcase_sprout.core.create_resource_properties import create_resource_properties
from seedcase_sprout.core.create_resource_structure import create_resource_structure
from seedcase_sprout.core.examples import (
    example_package_properties,
    example_resource_properties,
)
from seedcase_sprout.core.paths import PackagePath
from seedcase_sprout.core.write_file import write_file
from seedcase_sprout.core.write_package_properties import write_package_properties


class ExamplePackage(AbstractContextManager):
    """Create a temporary data package with optional resources for demoing or testing.

    Examples:
        ```{python}
        import seedcase_sprout.core as sp
        with sp.ExamplePackage() as package_path:
            properties = read_properties(package_path.properties())
            ...
        ```
        ```{python}
        import seedcase_sprout.core as sp
        with sp.ExamplePackage(with_resources=False) as package_path:
            properties = read_properties(package_path.properties())
            ...
        ```
    """

    def __init__(self, with_resources: bool = True):
        """Initialise the `ExamplePackage` context manager.

        Args:
            with_resources: Whether resources should be added when creating the package.
                Defaults to True.
        """
        self.with_resources = with_resources
        self.calling_dir = Path.cwd()
        self.temp_dir = tempfile.TemporaryDirectory()

    def __enter__(self) -> PackagePath:
        """Create the temporary package structure and switch to its directory.

        Returns:
            A `PackagePath` object pointing to the root of the temporary package.
        """
        package_path = PackagePath(Path(self.temp_dir.name))

        # Create package properties
        package_properties = example_package_properties()

        # Create resource properties
        if self.with_resources:
            resource_properties = example_resource_properties()
            package_properties.resources = [resource_properties]

            # Create resource folders
            # TODO: update after resource creation is refactored
            package_path.resources().mkdir(exist_ok=True)
            resource_path, _ = create_resource_structure(path=package_path.path)
            resource_properties = create_resource_properties(
                path=resource_path, properties=resource_properties
            )
            resource_properties.name = resource_path.stem

        # Save properties
        write_package_properties(
            properties=package_properties, path=package_path.properties()
        )

        # Write README
        write_file(as_readme_text(package_properties), package_path.readme())

        os.chdir(package_path.path)

        return package_path

    def __exit__(self, *_) -> None:
        """Restore the original working directory and clean up the temporary package."""
        os.chdir(self.calling_dir)
        self.temp_dir.cleanup()
