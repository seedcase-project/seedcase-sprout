from freezegun import freeze_time

from sprout.core.package import Package
from sprout.core.verify_package_properties import PACKAGE_REQUIRED_PROPERTIES
from sprout.core.verify_resource_properties import RESOURCE_REQUIRED_PROPERTIES


@freeze_time("2024-05-14 05:00:01")
def test_creates_package_with_default_values():
    package = Package()

    assert PACKAGE_REQUIRED_PROPERTIES.issubset(set(package.__dataclass_fields__))
    assert package.version == "0.1.0"
    assert package.created == "2024-05-14T05:00:01+00:00"

    assert package.resources
    resource = package.resources[0]
    assert RESOURCE_REQUIRED_PROPERTIES.issubset(set(resource.__dataclass_fields__))
    assert resource.type == "table"
    assert resource.format == "csv"
    assert resource.mediatype == "text/csv"
    assert resource.encoding == "utf-8"
