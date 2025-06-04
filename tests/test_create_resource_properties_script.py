from pytest import mark, raises

from seedcase_sprout.create_resource_properties_script import (
    create_resource_properties_script,
)
from seedcase_sprout.paths import PackagePath
from seedcase_sprout.properties import (
    FieldProperties,
    ResourceProperties,
    TableSchemaProperties,
)
from tests.load_properties import load_properties


@mark.parametrize("args", [[], [None] * 3])
def test_creates_empty_script(tmp_cwd, args):
    """Should create an empty script."""
    script_path = create_resource_properties_script(*args)

    assert script_path == PackagePath().resource_properties_script()
    properties = load_properties(script_path, "resource_properties_")
    assert properties == ResourceProperties(
        name="",
        title="",
        description="",
        type="table",
        format="parquet",
        mediatype="application/parquet",
        schema=TableSchemaProperties(fields=[FieldProperties(name="", type="")]),
    )


@mark.parametrize("resource_name", ["my_resource", "my.resource", "my-resource"])
def test_creates_script_with_name_and_fields(tmp_cwd, resource_name):
    """Should create a script with resource name and fields."""
    fields = [
        FieldProperties(name="field1", type="string"),
        FieldProperties(name="field2", type="datetime"),
    ]

    script_path = create_resource_properties_script(
        resource_name=resource_name,
        fields=fields,
    )

    properties = load_properties(script_path, "resource_properties_my_resource")
    assert properties == ResourceProperties(
        name=resource_name,
        title="",
        description="",
        type="table",
        format="parquet",
        mediatype="application/parquet",
        schema=TableSchemaProperties(fields=fields),
    )


def test_works_with_custom_path(tmp_path):
    """Should work with a custom path."""
    script_path = create_resource_properties_script(path=tmp_path)

    assert script_path == PackagePath(tmp_path).resource_properties_script()


def test_incorrect_resource_name_raises_error(tmp_cwd):
    """Should raise a error if an incorrect resource name is provided."""
    with raises(ValueError, match="resource name"):
        create_resource_properties_script(resource_name="spaces in name")
