from datetime import datetime
from unittest.mock import patch
from uuid import UUID
from zoneinfo import ZoneInfo

import time_machine

from seedcase_sprout.create_properties_script import create_properties_script
from seedcase_sprout.paths import PackagePath
from seedcase_sprout.properties import LicenseProperties, PackageProperties
from tests.load_properties import load_properties


@patch("seedcase_sprout.properties.uuid4", return_value=UUID(int=1))
@time_machine.travel(datetime(2024, 5, 14, 5, 0, 1, tzinfo=ZoneInfo("UTC")), tick=False)
def test_creates_script_with_default_values(mock_uuid, tmp_cwd):
    """Should create a script with default values."""
    script_path = create_properties_script()

    assert script_path == PackagePath().properties_script()
    properties = load_properties(script_path, "properties")
    assert properties == PackageProperties(
        name=tmp_cwd.name,
        title="",
        description="",
        licenses=[LicenseProperties(name="")],
        id=str(mock_uuid()),
        version="0.1.0",
        created="2024-05-14T05:00:01+00:00",
    )


def test_works_with_custom_path(tmp_path):
    """Should work with a custom path."""
    script_path = create_properties_script(tmp_path)

    assert script_path == PackagePath(tmp_path).properties_script()
    assert load_properties(script_path, "properties").name == tmp_path.name
