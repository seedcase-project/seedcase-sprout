def edit_property_field(properties: dict, field: str, value: any) -> dict:
    """Updates properties by setting the specified field to the specified value.

    The field must exist on the properties object.

    Args:
        properties: the properties to update
        field: the name of the field to update
        value: the value to assign to the field

    Returns:
        the updated properties object

    Raises:
        KeyError: if the specified field does not exist in properties
    """
    if field not in properties:
        raise KeyError(f"Field '{field}' does not exist in properties {properties}.")

    properties[field] = value
    return properties
