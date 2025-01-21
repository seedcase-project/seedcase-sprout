"""Core, external-facing functions of Sprout."""
# This exposes only the functions we want exposed when
# the package is imported via `from sprout.core import *`.

# Packages -----
# from .list_packages import *
# from .view_package_properties import *
from .create_package_structure import create_package_structure

# from .delete_package import *
# Resources -----
# from .list_resources import *
# from .view_resource import *
from .create_resource_properties import create_resource_properties
from .create_resource_structure import create_resource_structure
from .edit_package_properties import edit_package_properties

# from .write_resource_to_database import *
# from .delete_resource_raw_file import *
# from .delete_resource_data import *
# from .delete_resource_properties import *
# Path -----
# TODO: Consider having all these in one module.
from .path_package_functions import (
    path_package,
    path_package_database,
    path_package_properties,
    path_packages,
)
from .path_resource_functions import (
    path_resource,
    path_resource_data,
    path_resource_raw,
    path_resource_raw_files,
    path_resources,
)
from .path_sprout_global import path_sprout_global
from .properties import (
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
from .write_package_properties import write_package_properties

# from .extract_resource_properties import *
# from .edit_resource_properties import *
# from .write_resource_data_to_raw import *
# from .write_resource_parquet import *
from .write_resource_properties import write_resource_properties

# Helpers -----
# from .pretty_json import *

__all__ = [
    # Properties -----
    "ConstraintsProperties",
    "ContributorProperties",
    "FieldProperties",
    "LicenseProperties",
    "MissingValueProperties",
    "PackageProperties",
    "ReferenceProperties",
    "ResourceProperties",
    "SourceProperties",
    "TableDialectProperties",
    "TableSchemaForeignKeyProperties",
    "TableSchemaProperties",
    # Packages -----
    # "list_packages",
    # "view_package_properties",
    "create_package_structure",
    "edit_package_properties",
    "write_package_properties",
    # "delete_package",
    # Resources -----
    # "list_resources",
    # "view_resource",
    "create_resource_structure",
    # "create_resource_properties",
    # "extract_resource_properties",
    # "edit_resource_properties",
    # "write_resource_data_to_raw",
    # "write_resource_parquet",
    "write_resource_properties",
    # "write_resource_to_database",
    # "delete_resource_raw_file",
    # "delete_resource_data",
    # "delete_resource_properties",
    # Path -----
    "path_package",
    "path_package_database",
    "path_package_properties",
    "path_packages",
    "path_resource",
    "path_resource_data",
    "path_resource_raw",
    "path_resource_raw_files",
    "path_resources",
    "path_sprout_global",
    # Helpers -----
    # "pretty_json",
]
