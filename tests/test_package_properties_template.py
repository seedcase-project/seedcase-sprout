import os
import runpy
import shutil
from dataclasses import replace
from pathlib import Path

from pytest import fixture, raises

from seedcase_sprout.examples import ExamplePackage, example_package_properties
from seedcase_sprout.read_properties import read_properties
from seedcase_sprout.sprout_checks.required_fields import PACKAGE_SPROUT_REQUIRED_FIELDS
from seedcase_sprout.sync_package_properties_template import (
    sync_package_properties_template,
)
from seedcase_sprout.use_package_properties_template import (
    use_package_properties_template,
)
from tests.assert_raises_errors import assert_raises_check_errors


@fixture
def empty_template(tmp_cwd) -> Path:
    return sync_package_properties_template()


@fixture
def filled_template(tmp_cwd) -> Path:
    template_path = sync_package_properties_template()
    replace_in_template(template_path, old='""', new='"test"')
    return template_path


def test_empty_template_fails_checks(empty_template):
    """Executing the empty template should fail the checks."""
    assert_raises_check_errors(lambda: runpy.run_path(empty_template))


def test_runs_populated_template_from_package_root(filled_template):
    """Executing a populated template from the package root should create a
    datapackage.json file with the added fields."""
    runpy.run_path(filled_template)

    # Populated required fields should be present
    properties = read_properties()
    assert properties.name == "test"
    assert properties.title == "test"
    assert properties.description == "test"
    assert properties.licenses[0].name == "test"
    assert properties.id
    assert properties.version
    assert properties.created

    # Unpopulated optional fields should be absent
    assert all(key in PACKAGE_SPROUT_REQUIRED_FIELDS for key in properties.compact_dict)


def test_runs_populated_template_from_scripts_folder(filled_template):
    """Executing a populated template from the scripts folder should create a
    datapackage.json file with the added fields."""
    runpy_from_script_folder(filled_template)

    assert read_properties()


def test_running_unchanged_template_should_not_change_datapackage_json():
    """Executing an unchanged template generated from datapackage.json should write the
    same values back to datapackage.json."""
    with ExamplePackage():
        properties = read_properties()
        template_path = sync_package_properties_template()

        runpy.run_path(template_path)

        assert read_properties() == properties


def test_running_modified_template_updates_datapackage_json():
    """When a modified template is run, datapackage.json should be updated. Unchanged
    fields should remain the same."""
    with ExamplePackage():
        # Create template
        properties = read_properties()
        template_path = sync_package_properties_template()
        # Update `description`
        expected_properties = replace(properties, description="new description")
        replace_in_template(
            template_path,
            old=properties.description,
            new=expected_properties.description,
        )

        runpy.run_path(template_path)

        assert read_properties() == expected_properties


def test_cannot_set_resources_using_package_properties_template(empty_template):
    """Should raise an error if the `resources` field is set in the template."""
    replace_in_template(
        empty_template, old='name="",', new='name="",\n    resources=[],', count=1
    )

    with raises(ValueError, match="resources"):
        runpy.run_path(empty_template)


def test_cannot_use_non_file_template(empty_template):
    """Should raise an error if the template is not a file."""
    empty_template.unlink()
    empty_template.mkdir()

    with raises(ValueError, match=str(empty_template)):
        use_package_properties_template(example_package_properties(), empty_template)


def test_cannot_use_non_python_template(empty_template):
    """Should raise an error if the template is not a Python file."""
    empty_template = empty_template.with_suffix(".txt")

    with raises(ValueError, match=str(empty_template)):
        use_package_properties_template(example_package_properties(), empty_template)


def test_cannot_run_template_not_in_scripts_folder(filled_template):
    """Should raise an error if the template is not in the scripts folder."""
    outside_scripts = filled_template.parent.parent / filled_template.name
    shutil.move(str(filled_template), str(outside_scripts))

    with raises(ValueError, match=str(outside_scripts)):
        runpy.run_path(outside_scripts)


def replace_in_template(template_path: Path, old: str, new: str, count: int = -1):
    """Update the template by replacing substrings."""
    template = template_path.read_text().replace(old, new, count)
    template_path.write_text(template)


def runpy_from_script_folder(script_path: Path):
    """Runs a Python script with the script's folder as the cwd."""
    original = os.getcwd()
    os.chdir(script_path.parent)
    try:
        runpy.run_path(script_path)
    finally:
        os.chdir(original)
