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


def test_as_pruned_dict_generates_empty_dictionary_when_no_args_given():
    """Should return an empty dictionary, when no arguments are given to Properties
    class."""
    # Since this is a test of the base class, it's enough to test only one subclass
    assert ResourceProperties().as_pruned_dict == {}


@mark.parametrize(
    "properties, expected_dict",
    [
        (ContributorProperties(family_name="Kirk"), {"family_name": "Kirk"}),
        (LicenseProperties(name="MIT"), {"name": "MIT"}),
        (SourceProperties(title="SDCA"), {"title": "SDCA"}),
        (TableDialectProperties(header=True), {"header": True}),
        (ReferenceProperties(resource="resource-1"), {"resource": "resource-1"}),
        (TableSchemaForeignKeyProperties(fields=["field-1"]), {"fields": ["field-1"]}),
        (MissingValueProperties(value="NA"), {"value": "NA"}),
        (ConstraintsProperties(required=False), {"required": False}),
        (FieldProperties(name="field-1"), {"name": "field-1"}),
        (TableSchemaProperties(fields=["field-1"]), {"fields": ["field-1"]}),
        (ResourceProperties(name="resource-1"), {"name": "resource-1"}),
        (
            PackageProperties(name="package-1", version="3.2.1"),
            {"name": "package-1", "version": "3.2.1"},
        ),
    ],
)
def test_as_pruned_dict_preserves_only_non_none_values(properties, expected_dict):
    """Should return a dictionary with only non-None values when args given."""
    assert properties.as_pruned_dict == expected_dict


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
def test_default_return_properties_objects_with_same_keys_as_just_instantiated_object(
    cls,
):
    """Should return a Properties object with the same keys as a just-instantiated
    object, but different values."""
    default_properties = cls.default()

    assert asdict(default_properties).keys() == asdict(cls()).keys()
    assert asdict(default_properties).values() != asdict(cls()).values()

