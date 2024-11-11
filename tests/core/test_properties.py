from dataclasses import asdict
from datetime import datetime
from unittest.mock import patch
from uuid import UUID

import time_machine
from pytest import mark

from seedcase_sprout.core.properties import (
    ConstraintsProperties,
    ContributorProperties,
    FieldProperties,
    LicenseProperties,
    MissingValueProperties,
    PackageProperties,
    ReferenceProperties,
    ResourceProperties,
    SourceProperties,
    TableDialectProperties,
    TableSchemaForeignKeyProperties,
    TableSchemaProperties,
)


@mark.parametrize(
    "cls",
    [
        ContributorProperties,
        LicenseProperties,
        SourceProperties,
        TableDialectProperties,
        ReferenceProperties,
        TableSchemaForeignKeyProperties,
        MissingValueProperties,
        ConstraintsProperties,
        FieldProperties,
        TableSchemaProperties,
        ResourceProperties,
        PackageProperties,
    ],
)
def test_initiated_class_only_contains_none_values(cls):
    """When a Properties class is instantiated, all values should be None."""
    assert all(value is None for value in asdict(cls()).values())


def test_compact_dict_generates_empty_dictionary_when_no_args_given():
    """Should return an empty dictionary, when no arguments are given to Properties
    class."""
    # Since this is a test of the base class, it's enough to test only one subclass
    assert ResourceProperties().compact_dict == {}


def test_compact_dict_preserves_only_non_none_values():
    """Should return a dictionary with only non-None values when args given."""
    # Since this is a test of the base class, it's enough to test only one subclass

    # Given
    properties = PackageProperties(name="package-1", version="3.2.1")

    # When, then
    assert properties.compact_dict == {"name": "package-1", "version": "3.2.1"}


@patch("seedcase_sprout.core.properties.uuid4", return_value=UUID(int=1))
@time_machine.travel(datetime(2024, 5, 14, 5, 0, 1), tick=False)
def test_creates_package_properties_with_correct_defaults(mock_uuid):
    """Should return a dictionary of package properties containing correct defaults for
    PackageProperties specific values: id, version, and created"""
    properties = PackageProperties.default()

    assert properties.id == str(mock_uuid())
    assert properties.version == "0.1.0"
    assert properties.created == "2024-05-14T05:00:01+00:00"
