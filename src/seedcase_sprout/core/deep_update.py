from copy import deepcopy
from typing import Any, TypeVar

from deepmerge import Merger

from seedcase_sprout.core.properties import Properties

PropertiesSubclass = TypeVar("PropertiesSubclass", bound=Properties)


def _merge_properties(
    merger: Merger, path: list, old: PropertiesSubclass, updates: PropertiesSubclass
) -> PropertiesSubclass:
    """Merges two properties objects using the strategy specified in the merger.

    This is a helper function to be called by `deepmerge.Merger`.

    Args:
        merger: The merger calling this function.
        path: The path in the object to the attribute being merged.
        old: The properties object to update.
        updates: The properties object representing the updates to make.

    Returns:
        A new properties object with the updates.
    """
    return old.from_dict(merger.merge(old.compact_dict, updates.compact_dict))


DEEP_MERGER = Merger(
    # Merge strategies for types
    [
        (list, ["override"]),
        (dict, ["merge"]),
        (Properties, _merge_properties),
    ],
    # Fallback strategy for other types
    ["override"],
    # Strategy when types conflict
    ["override"],
)

PropertiesOrDict = TypeVar("PropertiesOrDict", Properties, dict[str, Any])


def deep_update(old: PropertiesOrDict, updates: PropertiesOrDict) -> PropertiesOrDict:
    """Updates an object with values from another object.

    Works analogously to the `update` method of the dictionary class, but
    can also handle nested structures and properties objects. Nested objects
    at each level of nesting are updated individually.

    Returns a new object without modifying the existing object.

    Args:
        old: The existing object to update.
        updates: The object representing the updates to make.

    Returns:
        A new object with updated values.
    """
    if isinstance(old, dict):
        old = deepcopy(old)
    return DEEP_MERGER.merge(old, updates)
