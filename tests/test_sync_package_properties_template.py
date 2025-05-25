import runpy
from dataclasses import replace
from datetime import datetime
from unittest.mock import patch
from uuid import UUID
from zoneinfo import ZoneInfo

import time_machine
from pytest import raises

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
    """When syncing without a datapackage.json, it should create an empty template."""
    package_path = PackagePath(tmp_cwd)

    sync_package_properties_template()

    # Should create empty template with default values
    template = package_path.package_properties_template().read_text()
    assert f'id="{str(mock_uuid())}"' in template
    assert 'version="0.1.0"' in template
    assert 'created="2024-05-14T05:00:01+00:00"' in template

    # Executing the template should fail the checks
    assert_raises_check_errors(
        lambda: runpy.run_path(package_path.package_properties_template())
    )


def test_creates_populated_template_when_datapackage_json():
    """When syncing with an existing datapackage.json, it should create a template
    populated with values from datapackage.json."""
    with ExamplePackage() as package_path:
        properties = read_properties()
        sync_package_properties_template()
        template_path = package_path.package_properties_template()

        # Should create a template with values from datapackage.json
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

        # Executing the template should write the same values back to datapackage.json
        runpy.run_path(template_path)
        assert read_properties() == properties


def test_running_modified_template_updates_datapackage_json():
    """When a modified template is run, datapackage.json should be updated. Unchanged
    fields should remain the same."""
    with ExamplePackage() as package_path:
        # Create template
        properties = read_properties()
        sync_package_properties_template()
        # Update `description`
        expected_properties = replace(properties, description="new description")
        template_path = package_path.package_properties_template()
        template = template_path.read_text().replace(
            properties.description, expected_properties.description
        )
        template_path.write_text(template)

        runpy.run_path(template_path)

        assert read_properties() == expected_properties


def test_cannot_set_resources_using_package_properties_template(tmp_cwd):
    """Should raise an error if the `resources` field is set in the template."""
    # Create template
    package_path = PackagePath(tmp_cwd)
    sync_package_properties_template()
    template_path = package_path.package_properties_template()
    # Add a `resources` field
    template = template_path.read_text().replace(
        'name="",', 'name="",\n    resources=[],', 1
    )
    template_path.write_text(template)

    with raises(ValueError, match="resources"):
        runpy.run_path(template_path)


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
