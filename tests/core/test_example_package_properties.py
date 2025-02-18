from seedcase_sprout.core.example_package_properties import example_package_properties
from seedcase_sprout.core.properties import PackageProperties


def test_creates_correct_properties_object():
    assert type(example_package_properties()) is PackageProperties
