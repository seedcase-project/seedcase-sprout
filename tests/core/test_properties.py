from dataclasses import asdict

from pytest import mark

from sprout.core.properties import (
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
