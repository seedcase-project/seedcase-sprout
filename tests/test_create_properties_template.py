from datetime import datetime
from unittest.mock import patch
from uuid import UUID
from zoneinfo import ZoneInfo

import time_machine

from seedcase_sprout.create_properties_template import create_properties_template
from seedcase_sprout.paths import PackagePath


@patch("seedcase_sprout.properties.uuid4", return_value=UUID(int=1))
@time_machine.travel(datetime(2024, 5, 14, 5, 0, 1, tzinfo=ZoneInfo("UTC")), tick=False)
def test_creates_template_with_default_values(mock_uuid, tmp_cwd):
    """Should create a template with default values."""
    template_path = create_properties_template()

    assert template_path == PackagePath().properties_template()
    template = template_path.read_text()
    assert f'name="{tmp_cwd.name}"' in template
    assert f'id="{str(mock_uuid())}"' in template
    assert 'version="0.1.0"' in template
    assert 'created="2024-05-14T05:00:01+00:00"' in template


def test_works_with_custom_path(tmp_path):
    """Should work with a custom path."""
    template_path = create_properties_template(tmp_path)

    assert template_path == PackagePath(tmp_path).properties_template()
    assert f'name="{tmp_path.name}"' in template_path.read_text()
