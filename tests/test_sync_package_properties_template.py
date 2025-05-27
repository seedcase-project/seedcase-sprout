from datetime import datetime
from unittest.mock import patch
from uuid import UUID
from zoneinfo import ZoneInfo

import time_machine

from seedcase_sprout.examples import ExamplePackage
from seedcase_sprout.internals.write import _write_json
from seedcase_sprout.paths import PackagePath
from seedcase_sprout.properties import PackageProperties
from seedcase_sprout.read_properties import read_properties
from seedcase_sprout.sync_package_properties_template import (
    sync_package_properties_template,
)
from tests.assert_raises_errors import assert_raises_check_errors


@patch("seedcase_sprout.properties.uuid4", return_value=UUID(int=1))
@time_machine.travel(datetime(2024, 5, 14, 5, 0, 1, tzinfo=ZoneInfo("UTC")), tick=False)
def test_creates_empty_template_when_no_datapackage_json(mock_uuid, tmp_cwd):
    """When syncing without a datapackage.json, it should create an empty template with
    default values."""
    template_path = sync_package_properties_template()

    template = template_path.read_text()
    assert f'id="{str(mock_uuid())}"' in template
    assert 'version="0.1.0"' in template
    assert 'created="2024-05-14T05:00:01+00:00"' in template


def test_creates_populated_template_when_datapackage_json():
    """When syncing with an existing datapackage.json, it should create a template
    populated with values from datapackage.json."""
    with ExamplePackage():
        properties = read_properties()

        template_path = sync_package_properties_template()

        template = template_path.read_text()
        for name, value in [
            ("name", properties.name),
            ("title", properties.title),
            ("description", properties.description),
            ("id", properties.id),
            ("version", properties.version),
            ("created", properties.created),
            ("title", properties.contributors[0].title),
            ("email", properties.contributors[0].email),
            ("name", properties.licenses[0].name),
            ("path", properties.licenses[0].path),
            ("title", properties.licenses[0].title),
        ]:
            assert f'{name}="{value}"' in template
        assert 'roles=["creator"]' in template


def test_cannot_sync_to_incorrect_datapackage_json(tmp_cwd):
    """Should raise an error when trying to sync the template with an
    incorrect datapackage.json."""
    package_path = PackagePath(tmp_cwd)
    _write_json(PackageProperties().compact_dict, package_path.properties())

    assert_raises_check_errors(sync_package_properties_template)


def test_works_with_custom_path(tmp_path):
    """Should work with a custom path."""
    sync_package_properties_template(tmp_path)

    assert PackagePath(tmp_path).package_properties_template().exists()
