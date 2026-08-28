from pytest import raises

from seedcase_sprout.check_properties import DataResourceError
from seedcase_sprout.examples import (
    example_data,
    example_resource_properties,
)
from seedcase_sprout.write_resource_data import write_resource_data
from tests.assert_raises_errors import (
    assert_raises_errors,
)


def test_throws_error_if_resource_properties_incorrect():
    """Should throw an error if the resource properties are incorrect."""
    resource_properties = example_resource_properties()
    resource_properties.name = "spaces in name"

    with raises(DataResourceError):
        write_resource_data(example_data(), resource_properties)


def test_throws_error_if_properties_do_not_match_data():
    """Should throw an error if the resource properties and the data don't match."""
    resource_properties = example_resource_properties()
    assert resource_properties.schema and resource_properties.schema.fields
    resource_properties.schema.fields[0].type = "yearmonth"

    assert_raises_errors(
        lambda: write_resource_data(example_data(), resource_properties), ValueError
    )
