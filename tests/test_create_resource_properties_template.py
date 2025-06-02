from pytest import mark, raises

from seedcase_sprout.create_resource_properties_template import (
    create_resource_properties_template,
)
from seedcase_sprout.paths import PackagePath
from seedcase_sprout.properties import (
    FieldProperties,
    ResourceProperties,
    TableSchemaProperties,
)
from tests.load_properties import load_properties


@mark.parametrize("args", [[], [None] * 3])
def test_creates_empty_template(tmp_cwd, args):
    """Should create an empty template."""
    template_path = create_resource_properties_template(*args)

    assert template_path == PackagePath().resource_properties_template()
    properties = load_properties(template_path, "resource_properties_")
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
def test_creates_template_with_name_and_fields(tmp_cwd, resource_name):
    """Should create a template with resource name and fields."""
    fields = [
        FieldProperties(name="field1", type="string"),
        FieldProperties(name="field2", type="datetime"),
    ]

    template_path = create_resource_properties_template(
        resource_name=resource_name,
        fields=fields,
    )

    properties = load_properties(template_path, "resource_properties_my_resource")
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
    template_path = create_resource_properties_template(path=tmp_path)

    assert template_path == PackagePath(tmp_path).resource_properties_template()


def test_incorrect_resource_name_raises_error(tmp_cwd):
    """Should raise a error if an incorrect resource name is provided."""
    with raises(ValueError, match="resource name"):
        create_resource_properties_template(resource_name="spaces in name")
