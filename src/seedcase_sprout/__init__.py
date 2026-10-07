"""External-facing functions of Seedcase Sprout."""
# This exposes only the functions we want exposed when
# the package is imported via `from seedcase_sprout import *`.

from pprint import pprint
from textwrap import dedent

from .cli import extract_metadata, init_metadata
from .examples import (
    example_data,
    example_data_all_types,
    example_package_properties,
    example_resource_properties,
    example_resource_properties_all_types,
)
from .properties import (
    ConstraintsProperties,
    ContributorProperties,
    FieldProperties,
    FieldsMatchType,
    FieldType,
    LicenseProperties,
    ReferenceProperties,
    ResourceProperties,
    SourceProperties,
    SproutProperties,
    TableSchemaForeignKeyProperties,
    TableSchemaProperties,
)
from .write_properties import write_properties

__all__ = [
    "ConstraintsProperties",
    "ContributorProperties",
    "FieldProperties",
    "FieldType",
    "FieldsMatchType",
    "LicenseProperties",
    "ReferenceProperties",
    "ResourceProperties",
    "SourceProperties",
    "SproutProperties",
    "TableSchemaForeignKeyProperties",
    "TableSchemaProperties",
    "dedent",
    "example_data",
    "example_data_all_types",
    "example_package_properties",
    "example_resource_properties",
    "example_resource_properties_all_types",
    "extract_field_properties",
    "extract_metadata",
    "init_metadata",
    "pprint",
    "write_properties",
]
