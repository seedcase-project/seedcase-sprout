from seedcase_sprout.core import checks
from seedcase_sprout.core.checks.required_fields import (
    RequiredFieldType,
)

# Sprout-specific required fields and their types

PACKAGE_SPROUT_REQUIRED_FIELDS = checks.PACKAGE_RECOMMENDED_FIELDS | {
    "title": RequiredFieldType.str,
    "description": RequiredFieldType.str,
    "version": RequiredFieldType.str,
    "created": RequiredFieldType.str,
}

RESOURCE_SPROUT_REQUIRED_FIELDS = checks.RESOURCE_REQUIRED_FIELDS | {
    "title": RequiredFieldType.str,
    "description": RequiredFieldType.str,
}
