from typing import Any, TypeVar

from seedcase_sprout.core.properties import PackageProperties, ResourceProperties

PackagePropertiesOrDict = TypeVar(
    "PackagePropertiesOrDict", PackageProperties, dict[str, Any]
)
ResourcePropertiesOrDict = TypeVar(
    "ResourcePropertiesOrDict", ResourceProperties, dict[str, Any]
)
