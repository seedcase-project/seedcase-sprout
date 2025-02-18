from pathlib import Path

import pandera as pa
from pytest import fixture, mark, raises

from seedcase_sprout.core.properties import (
    ConstraintsProperties,
    FieldProperties,
    ResourceProperties,
    TableDialectProperties,
    TableSchemaProperties,
)
from seedcase_sprout.core.sprout_checks.check_data import (
    check_data,
)


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


@mark.parametrize("required", [False, None])
def test_no_error_for_schema_missing_values_when_field_not_required(
    data_path, resource_properties, required
):
    """If a field's value is listed in `schema.missing_values`, it is treated as null.
    When the field is not required, null values don't trigger an error."""
    resource_properties.schema.fields = [
        FieldProperties(
            name="my_date",
            type="date",
            constraints=ConstraintsProperties(required=required),
        )
    ]
    resource_properties.schema.missing_values = ["None", "NA", "*", "some text"]
    data_path.write_text(
        "1234-11-11\n" + "\n".join(resource_properties.schema.missing_values)
    )

    assert check_data(data_path, resource_properties) == data_path


def test_error_for_schema_missing_values_when_field_required(
    data_path, resource_properties
):
    """If a field's value is listed in `schema.missing_values`, it is treated as null.
    When the field is required, null values trigger an error."""
    resource_properties.schema.fields = [
        FieldProperties(
            name="my_any",
            type="any",
            constraints=ConstraintsProperties(required=True),
        )
    ]
    resource_properties.schema.missing_values = ["None"]
    data_path.write_text("1234-11-11\nNone")

    with raises(pa.errors.SchemaErrors):
        check_data(data_path, resource_properties)


@mark.parametrize("required", [False, None])
def test_no_error_for_field_missing_values_when_field_not_required(
    data_path, resource_properties, required
):
    """If a field's value is listed in `field.missing_values`, it is treated as null.
    When the field is not required, null values don't trigger an error."""
    resource_properties.schema.fields = [
        FieldProperties(
            name="my_date",
            type="date",
            constraints=ConstraintsProperties(required=required),
            missing_values=["None", "NA", "*", "some text"],
        )
    ]
    data_path.write_text(
        "1234-11-11\n" + "\n".join(resource_properties.schema.fields[0].missing_values)
    )

    assert check_data(data_path, resource_properties) == data_path


def test_error_for_field_missing_values_when_field_required(
    data_path, resource_properties
):
    """If a field's value is listed in `field.missing_values`, it is treated as null.
    When the field is required, null values trigger an error."""
    resource_properties.schema.fields = [
        FieldProperties(
            name="my_any",
            type="any",
            constraints=ConstraintsProperties(required=True),
            missing_values=["None"],
        )
    ]
    data_path.write_text("1234-11-11\nNone")

    with raises(pa.errors.SchemaErrors):
        check_data(data_path, resource_properties)


@mark.parametrize(
    "schema_missing_values,data",
    [
        (["schema-missing-value"], "schema-missing-value,value"),
        ([], ",value"),
        (None, ",value"),
    ],
)
def test_field_missing_values_override_schema_missing_values_error_case(
    data_path, resource_properties, schema_missing_values, data
):
    """If both `schema.missing_values` and `field.missing_values` are set, the latter
    takes precedence. Fields with a value in `schema.missing_values` are not changed to
    null. When these values are of the wrong data type, an error is raised."""
    resource_properties.schema.fields = [
        FieldProperties(
            name="my_integer",
            type="integer",
            missing_values=["field-missing-value"],
        ),
        FieldProperties(
            name="my_string",
            type="string",
        ),
    ]
    resource_properties.schema.missing_values = schema_missing_values
    data_path.write_text(f"123,value\n{data}")

    with raises(pa.errors.SchemaErrors):
        check_data(data_path, resource_properties)


@mark.parametrize("schema_missing_values", ["schema-missing-value", [], None])
def test_field_missing_values_override_schema_missing_values_pass_case(
    data_path, resource_properties, schema_missing_values
):
    """If both `schema.missing_values` and `field.missing_values` are set, the latter
    takes precedence. Fields with a value in `field.missing_values` are changed to
    null and count as valid when the field is not required."""
    resource_properties.schema.fields = [
        FieldProperties(
            name="my_date",
            type="date",
            missing_values=["field-missing-value"],
        )
    ]
    resource_properties.schema.missing_values = schema_missing_values
    data_path.write_text("1234-11-11\nfield-missing-value")

    assert check_data(data_path, resource_properties) == data_path


@mark.parametrize("schema_missing_values", ["schema-missing-value", [], None])
@mark.parametrize("required", [True, False, None])
def test_all_values_count_as_present_when_field_missing_values_empty(
    data_path, resource_properties, schema_missing_values, required
):
    """When `field.missing_values` is set to the empty list, no value counts as missing
    and no null conversion is done. Empty string fields don't raise an error, regardless
    of whether the field is required. `field.missing_values` takes precedence over
    `schema.missing_values`."""
    resource_properties.schema.fields = [
        FieldProperties(
            name="col1",
            type="string",
            missing_values=[],
            constraints=ConstraintsProperties(required=required),
        ),
        FieldProperties(
            name="col2",
            type="string",
        ),
    ]
    resource_properties.schema.missing_values = schema_missing_values
    data_path.write_text("value1,value2\n,value2")

    assert check_data(data_path, resource_properties) == data_path


@mark.parametrize("required", [True, False, None])
def test_all_values_count_as_present_when_schema_missing_values_empty(
    data_path, resource_properties, required
):
    """When `schema.missing_values` is set to the empty list and `field.missing_values`
    is not set, no value counts as missing and no null conversion is done. Empty string
    fields don't raise an error, regardless of whether the field is required."""
    resource_properties.schema.fields = [
        FieldProperties(
            name="col1",
            type="string",
            constraints=ConstraintsProperties(required=required),
        ),
        FieldProperties(
            name="col2",
            type="string",
        ),
    ]
    resource_properties.schema.missing_values = []
    data_path.write_text("value1,value2\n,value2")

    assert check_data(data_path, resource_properties) == data_path


@mark.parametrize("required", [False, None])
def test_no_error_for_missing_values_when_field_not_required_and_no_missing_values_set(
    data_path, resource_properties, required
):
    """When missing values are not set, the empty string is treated as null by default.
    No error is raised for fields that are not required."""
    resource_properties.schema.fields = [
        FieldProperties(
            name="my_date",
            type="date",
            constraints=ConstraintsProperties(required=required),
        ),
        FieldProperties(name="my_string", type="string"),
    ]
    data_path.write_text("1234-11-11,value\n,value")

    assert check_data(data_path, resource_properties) == data_path


def test_error_for_missing_values_when_field_required_and_no_missing_values_set(
    data_path, resource_properties
):
    """When missing values are not set, the empty string is treated as null by default.
    An error is raised for required fields."""
    resource_properties.schema.fields = [
        FieldProperties(
            name="my_any",
            type="any",
            constraints=ConstraintsProperties(required=True),
        ),
        FieldProperties(name="my_string", type="string"),
    ]
    data_path.write_text("1234-11-11,value\n,value")

    with raises(pa.errors.SchemaErrors):
        check_data(data_path, resource_properties)


def test_makes_value_null_only_if_full_match(data_path, resource_properties):
    """A value is changed to null only if it fully matches one of the missing values."""
    resource_properties.schema.fields = [
        FieldProperties(
            name="my_date",
            type="date",
            constraints=ConstraintsProperties(required=False),
        )
    ]
    resource_properties.schema.missing_values = ["11-11"]
    data_path.write_text("1234-11-11\n11-11")

    assert check_data(data_path, resource_properties) == data_path


def test_field_missing_values_can_be_set_separately_for_each_field(
    data_path, resource_properties
):
    """`field.missing_values` can be set separately for each field."""
    resource_properties.schema.fields = [
        FieldProperties(
            name="col1",
            type="date",
            missing_values=["field-1-missing"],
        ),
        FieldProperties(
            name="col2",
            type="date",
            missing_values=["field-2-missing"],
        ),
    ]
    data_path.write_text("field-1-missing,1234-11-11\n1010-05-05,field-2-missing")

    assert check_data(data_path, resource_properties) == data_path
