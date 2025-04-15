from typing import Any, TypeVar

from seedcase_sprout.core.examples import (
    example_resource_properties,
)
from seedcase_sprout.core.properties import PackageProperties, ResourceProperties

T = TypeVar("T")


def get_nested_attr(
    base_object: Any, attributes: str, default: T | None = None
) -> T | None:
    """Returns the attribute specified by `attributes`.

    Tries to resolve the chain of attributes against `base_object`. Returns None
    or the specified default value if the attribute chain cannot be resolved.

    Args:
        base_object: The object to start resolving the attributes from.
        attributes: The chain of attributes as a dot-separated string.
        default: The default value to return if the attributes cannot be resolved.
            Defaults to None.

    Returns:
        The value at the end of the attribute chain.

    Raises:
        ValueError: If the attribute chain contains an element that is not a valid
            identifier.

    Examples:
        ```{python}
        class Inner:
            pass
        class Middle:
            inner: Inner = Inner()
        class Outer:
            middle: Middle = Middle()

        get_nested_attr(Outer(), "middle.inner")
        ```
    """
    attributes = attributes.split(".")

    try:
        for attribute in attributes:
            base_object = getattr(base_object, attribute)
    except AttributeError:
        return default

    return default if base_object is None else base_object


_get_nested_property = get_nested_attr


def _get_package_property(properties: PackageProperties, field: str) -> Any | None:
    return getattr(properties, field)


def _get_resource_property(properties: ResourceProperties, field: str) -> Any | None:
    return getattr(properties, field)


from itertools import repeat


def _get_resource_field_names(properties: ResourceProperties) -> list[str] | None:
    properties = _get_resource_fields(properties)
    return list(map(getattr, properties, repeat("name")))


def _get_resource_fields(
    properties: ResourceProperties,
) -> list[Any | None]:
    return _get_nested_property(properties, "schema.fields")


print(_get_resource_field_names(example_resource_properties()))

# fields: list[FieldProperties] = get_nested_attr(
#     resource_properties, "schema.fields", default=[]
# )

# schema_missing_values = get_nested_attr(
#     resource_properties, "schema.missing_values", default=[""]
# )
