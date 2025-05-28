import runpy
from pathlib import Path

from pytest import fixture

from seedcase_sprout.create_properties_template import create_properties_template
from seedcase_sprout.examples import example_package_properties
from seedcase_sprout.read_properties import read_properties
from seedcase_sprout.sprout_checks.required_fields import PACKAGE_SPROUT_REQUIRED_FIELDS
from seedcase_sprout.write_package_properties import write_package_properties
from tests.assert_raises_errors import assert_raises_check_errors


@fixture
def filled_template(tmp_cwd) -> Path:
    template_path = create_properties_template()
    template = template_path.read_text().replace('""', '"test"')
    template_path.write_text(template)
    return template_path


def test_empty_template_fails_checks(tmp_cwd):
    """Executing the empty template should fail the checks."""
    template_path = create_properties_template()

    assert_raises_check_errors(lambda: runpy.run_path(template_path))


def test_running_populated_template_creates_datapackage_json(filled_template):
    """Executing a populated template should create a datapackage.json file with the
    added fields."""
    runpy.run_path(filled_template)

    assert_datapackage_json_written(filled_template)


def test_running_populated_template_rewrites_datapackage_json(filled_template):
    """Executing a populated template should rewrite an existing datapackage.json
    file."""
    write_package_properties(example_package_properties())

    runpy.run_path(filled_template)

    assert_datapackage_json_written(filled_template)


def assert_datapackage_json_written(filled_template: Path):
    # Populated required fields should be present
    properties = read_properties()
    assert properties.name == filled_template.parent.name
    assert properties.title == "test"
    assert properties.description == "test"
    assert properties.licenses[0].name == "test"
    assert properties.id
    assert properties.version
    assert properties.created

    # Unpopulated optional fields should be absent
    assert all(key in PACKAGE_SPROUT_REQUIRED_FIELDS for key in properties.compact_dict)
