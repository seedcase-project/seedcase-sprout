from dataclasses import asdict

from sprout.core.properties import PackageProperties
from sprout.core.utils import get_iso_timestamp


def create_default_package_properties(id: int) -> dict:
    """Creates a `PackageProperties` object with default values.

    Args:
        id: The id of the package.

    Returns:
        A dictionary representation of the package properties.
    """
    package_properties = PackageProperties(
        id=id,
        name=f"package-{id}",
        title=f"Package {id}",
        description=f"This is a description of Package {id}.",
        version="0.1.0",
        created=get_iso_timestamp(),
    )
    return asdict(package_properties)
