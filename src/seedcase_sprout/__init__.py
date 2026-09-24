"""External-facing functions of Seedcase Sprout."""
# This exposes only the functions we want exposed when
# the package is imported via `from seedcase_sprout import *`.

from pprint import pprint
from textwrap import dedent

from .check_data import check_data
from .check_properties import DataResourceError
from .cli import extract_metadata, init_metadata
from .examples import (
    example_data,
    example_data_all_types,
    example_package_properties,
    example_resource_properties,
    example_resource_properties_all_types,
)
from .extract_field_properties import extract_field_properties
from .join_staging import join_staging
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
from .read_properties import read_properties
from .read_staging import read_staging
from .write_file import write_file
from .write_properties import write_properties
from .write_resource_data import write_resource_data

__all__ = [
    "ConstraintsProperties",
    "ContributorProperties",
    "DataResourceError",
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
    "check_data",
    "dedent",
    "example_data",
    "example_data_all_types",
    "example_package_properties",
    "example_resource_properties",
    "example_resource_properties_all_types",
    "extract_field_properties",
    "extract_metadata",
    "init_metadata",
    "join_staging",
    "pprint",
    "read_properties",
    "read_staging",
    "write_file",
    "write_properties",
    "write_resource_data",
]
