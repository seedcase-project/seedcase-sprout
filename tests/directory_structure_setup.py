from pathlib import Path

from seedcase_soil import write_properties

from seedcase_sprout import (
    example_package_properties,
)


def create_test_data_package(tmp_path: Path) -> Path:
    """Creates a package file structure (with empty files) for path function tests.

    Args:
        tmp_path: Path to a temporary folder.

    Returns:
        Path of package.
    """
    tmp_path.mkdir(parents=True, exist_ok=True)
    write_properties(
        properties=example_package_properties().compact_dict,
        path=tmp_path / "datapackage.json",
    )

    return tmp_path
