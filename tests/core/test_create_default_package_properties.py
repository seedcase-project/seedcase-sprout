from datetime import datetime

import time_machine

from sprout.core.create_default_package_properties import (
    create_default_package_properties,
)


@time_machine.travel(datetime(2024, 5, 14, 5, 0, 1), tick=False)
def test_creates_properties_dict_with_correct_defaults():
    """Given an id, should return a dictionary of package properties containing default
    values."""
    properties = create_default_package_properties(22)

    assert type(properties) is dict
    assert properties["id"] == 22
    assert properties["name"] == "package-22"
    assert properties["title"] == "Package 22"
    assert properties["description"] == "This is a description of Package 22."
    assert properties["version"] == "0.1.0"
    assert properties["created"] == "2024-05-14T05:00:01+00:00"
