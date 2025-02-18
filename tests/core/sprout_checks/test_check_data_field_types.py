from pathlib import Path

from pandera import errors
from pytest import fixture, mark, raises

from seedcase_sprout.core.properties import (
    FieldProperties,
    ResourceProperties,
    TableDialectProperties,
    TableSchemaProperties,
)
from seedcase_sprout.core.sprout_checks.check_data import (
    check_data,
)
from seedcase_sprout.core.sprout_checks.get_pandera_checks import BOOLEAN_VALUES


@fixture
def data_path(tmp_path) -> Path:
    return tmp_path / "data.csv"


@fixture
def resource_properties() -> ResourceProperties:
    return ResourceProperties(
        name="data",
        title="data",
        path=str(Path("resources", "1", "data.csv")),
        description="My data...",
        dialect=TableDialectProperties(header=False),
        schema=TableSchemaProperties(),
    )


@mark.parametrize(
    "string,format",
    [
        ("my value $$", "default"),
        ("my value $$", None),
        ("jane_55@doe.co.uk", "email"),
        ("www.my-site.com", "uri"),
        ("aGVsbG8sIGFuIGVuY29kZWQgbWVzc2FnZQ==", "binary"),
        ("47254d85-541c-4594-bb8b-bf89431505eb", "uuid"),
    ],
)
def test_accepts_string_field(data_path, resource_properties, string, format):
    """Should not raise an error for valid string fields of the listed formats."""
    data_path.write_text(string)
    fields = [FieldProperties(name="my_string", type="string", format=format)]
    resource_properties.schema.fields = fields

    assert check_data(data_path, resource_properties) == data_path


@mark.parametrize("format", ["binary", "email", "uuid"])
def test_rejects_badly_formatted_string_field(data_path, resource_properties, format):
    """Should raise an error for invalid string fields of the listed formats."""
    data_path.write_text("***")
    fields = [FieldProperties(name="my_string", type="string", format=format)]
    resource_properties.schema.fields = fields

    with raises(errors.SchemaErrors):
        check_data(data_path, resource_properties)


@mark.parametrize("field_type", ["any", None])
@mark.parametrize(
    "value",
    [
        "123",
        "123.123",
        "some text",
        "2034-11-10",
        '"one,two"',
        '"[{""prop1"": ""value""}, {""prop2"": 123}]"',
    ],
)
def test_accepts_any_field(data_path, resource_properties, value, field_type):
    """Should accept any kind of value for default and any-type fields."""
    data_path.write_text(value)
    fields = [FieldProperties(name="my_any", type=field_type)]
    resource_properties.schema.fields = fields

    assert check_data(data_path, resource_properties) == data_path


@mark.parametrize(
    "number",
    [
        "123",
        "123.123",
        "-23",
        "+45.5",
        "0003",
        "2.0000",
        "NaN",
        "NAN",
        "nan",
        "inf",
        "INF",
        "-inf",
        "-INF",
        "2E3",
        "2E-33",
    ],
)
def test_accepts_number_field(data_path, resource_properties, number):
    """Should accept valid number values for number fields."""
    data_path.write_text(number)
    fields = [FieldProperties(name="my_number", type="number")]
    resource_properties.schema.fields = fields

    assert check_data(data_path, resource_properties) == data_path


def test_rejects_number_field_of_wrong_type(data_path, resource_properties):
    """Should throw an error for number fields of the wrong type."""
    data_path.write_text("not a number")
    fields = [FieldProperties(name="my_number", type="number")]
    resource_properties.schema.fields = fields

    with raises(errors.SchemaErrors):
        check_data(data_path, resource_properties)


@mark.parametrize("integer", ["123", "-123", "000"])
def test_accepts_integer_field(data_path, resource_properties, integer):
    """Should accept valid integer values for integer fields."""
    data_path.write_text(integer)
    fields = [FieldProperties(name="my_integer", type="integer")]
    resource_properties.schema.fields = fields

    assert check_data(data_path, resource_properties) == data_path


@mark.parametrize("boolean", BOOLEAN_VALUES)
def test_accepts_boolean_field(data_path, resource_properties, boolean):
    """Should accept valid boolean values for boolean fields."""
    data_path.write_text(f"{boolean}\n")
    fields = [FieldProperties(name="my_boolean", type="boolean")]
    resource_properties.schema.fields = fields

    assert check_data(data_path, resource_properties) == data_path


@mark.parametrize(
    "value,field_type",
    [
        ("2002-10-10T12:00:00.34-05:00", "datetime"),
        ("2002-10-10", "date"),
        ("15:00:59", "time"),
        ("2014", "year"),
        ("2014-12", "yearmonth"),
        ("P1Y2M3DT10H30M45.343S", "duration"),
        ('"+90.0, -127.554334"', "geopoint"),
    ],
)
def test_accepts_date_or_time_related_field(
    data_path, resource_properties, value, field_type
):
    """Should accept valid values for fields of the listed types."""
    data_path.write_text(value)
    fields = [FieldProperties(name="my_field", type=field_type)]
    resource_properties.schema.fields = fields

    assert check_data(data_path, resource_properties) == data_path


@mark.parametrize(
    "value,field_type",
    [
        ("2002-10-10 12:00:00.34-05:00", "datetime"),
        ("2002-13-10", "date"),
        ("15-00-59", "time"),
        ("14", "year"),
        ("2014.12", "yearmonth"),
        ("1Y2M3DT10H30M45.343S", "duration"),
        ('"+90.1, -127"', "geopoint"),
    ],
)
def test_rejects_badly_formatted_date_or_time_related_field(
    data_path, resource_properties, value, field_type
):
    """Should throw an error for invalid values for fields of the listed types."""
    data_path.write_text(value)
    fields = [FieldProperties(name="my_field", type=field_type)]
    resource_properties.schema.fields = fields

    with raises(errors.SchemaErrors):
        check_data(data_path, resource_properties)


@mark.parametrize("value", ["one", '"one,two,three"'])
def test_accepts_list_field(data_path, resource_properties, value):
    """Should accept valid values for list fields."""
    data_path.write_text(value)
    fields = [FieldProperties(name="my_list", type="list")]
    resource_properties.schema.fields = fields

    assert check_data(data_path, resource_properties) == data_path


@mark.parametrize(
    "json_object",
    [
        "{}",
        '"{}"',
        (
            '"{""outer"": ""value"", ""inner"": '
            '{""prop1"": 123, ""prop2"": [1, 2, null], ""prop3"": true}}"'
        ),
    ],
)
def test_accepts_object_field(data_path, resource_properties, json_object):
    """Should accept valid values for object fields."""
    data_path.write_text(json_object)
    fields = [FieldProperties(name="my_object", type="object")]
    resource_properties.schema.fields = fields

    assert check_data(data_path, resource_properties) == data_path


@mark.parametrize(
    "value",
    [
        "[]",
        '"[{""prop1"": ""value""}]"',
        '"{""prop1"": ""value"",}"',
        '"{""prop1"": ""value"}"',
    ],
)
def test_rejects_badly_formatted_object_field(data_path, resource_properties, value):
    """Should throw an error for invalid object fields."""
    data_path.write_text(value)
    fields = [FieldProperties(name="my_object", type="object")]
    resource_properties.schema.fields = fields

    with raises(errors.SchemaErrors):
        check_data(data_path, resource_properties)


@mark.parametrize(
    "json_array",
    [
        "[]",
        '"[{""prop1"": ""value""}, {""prop2"": 123}]"',
    ],
)
def test_accepts_array_field(data_path, resource_properties, json_array):
    """Should accept valid values for array fields."""
    data_path.write_text(json_array)
    fields = [FieldProperties(name="my_array", type="array")]
    resource_properties.schema.fields = fields

    assert check_data(data_path, resource_properties) == data_path


@mark.parametrize(
    "value",
    [
        '"[,]"',
        '"[{""prop1"": ""value"",}]"',
        "{}",
        '"{""prop1"": ""value""}"',
    ],
)
def test_rejects_badly_formatted_array_field(data_path, resource_properties, value):
    """Should throw an error for invalid array fields."""
    data_path.write_text(value)
    fields = [FieldProperties(name="my_array", type="array")]
    resource_properties.schema.fields = fields

    with raises(errors.SchemaErrors):
        check_data(data_path, resource_properties)


@mark.parametrize(
    "field_type",
    [
        "integer",
        "boolean",
        "object",
        "array",
        "datetime",
        "date",
        "time",
        "year",
        "yearmonth",
        "duration",
        "geopoint",
    ],
)
def test_rejects_value_of_wrong_type(data_path, resource_properties, field_type):
    """Should throw an error for values of the wrong type for the listed fields."""
    data_path.write_text("123.123")
    fields = [FieldProperties(name="my_field", type=field_type)]
    resource_properties.schema.fields = fields

    with raises(errors.SchemaErrors):
        check_data(data_path, resource_properties)
