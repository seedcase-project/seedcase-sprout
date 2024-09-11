from dataclasses import fields

from freezegun import freeze_time
from pytest import mark

from sprout.core.package import Package, Resource


@freeze_time("2024-05-14 05:00:01")
def test_creates_package_with_default_values():
    """When calling the constructor with no arguments, should create a package with
    default values."""
    package = Package()

    assert package.version == "0.1.0"
    assert package.created == "2024-05-14T05:00:01+00:00"
    assert package.resources

    resource = package.resources[0]
    assert resource.type == "table"
    assert resource.format == "csv"
    assert resource.mediatype == "text/csv"
    assert resource.encoding == "utf-8"


@mark.parametrize("cls", [Package, Resource])
def test_required_properties_in_class(cls: type):
    """The required properties of a class should be a subset of the class' fields."""
    class_fields = [field.name for field in fields(cls)]
    assert cls.REQUIRED_PROPERTIES.issubset(class_fields)
