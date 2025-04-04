from seedcase_sprout.core import check_datapackage
from seedcase_sprout.core.check_datapackage.required_fields import (
    RequiredFieldType,
)

# Sprout-specific required fields and their types

PACKAGE_SPROUT_REQUIRED_FIELDS = (
    check_datapackage.PACKAGE_REQUIRED_FIELDS
    | check_datapackage.PACKAGE_RECOMMENDED_FIELDS
    | {
        "title": RequiredFieldType.str,
        "description": RequiredFieldType.str,
        "version": RequiredFieldType.str,
        "created": RequiredFieldType.str,
    }
)
PACKAGE_SPROUT_REQUIRED_FIELDS.pop("resources", None)

RESOURCE_SPROUT_REQUIRED_FIELDS = check_datapackage.RESOURCE_REQUIRED_FIELDS | {
    "title": RequiredFieldType.str,
    "description": RequiredFieldType.str,
}
RESOURCE_SPROUT_REQUIRED_FIELDS.pop("data", None)
