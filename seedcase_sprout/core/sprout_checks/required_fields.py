from seedcase_sprout.core import checks
from seedcase_sprout.core.checks.required_fields import (
    RequiredFieldType,
)
from seedcase_sprout.core.sprout_checks.omit_keys import omit_keys

# Sprout-specific required fields and their types

PACKAGE_SPROUT_REQUIRED_FIELDS = (
    omit_keys(checks.PACKAGE_REQUIRED_FIELDS, ["resources"])
    | checks.PACKAGE_RECOMMENDED_FIELDS
    | {
        "title": RequiredFieldType.str,
        "description": RequiredFieldType.str,
        "version": RequiredFieldType.str,
        "created": RequiredFieldType.str,
    }
)

RESOURCE_SPROUT_REQUIRED_FIELDS = omit_keys(
    checks.RESOURCE_REQUIRED_FIELDS, ["data"]
) | {
    "title": RequiredFieldType.str,
    "description": RequiredFieldType.str,
}
