def edit_resource_properties_field(properties: dict, field: str, value: any) -> dict:
    """Updates properties by setting the specified field to the specified value.

    Args:
        properties: the properties to update
        field: the name of the field to set or update
        value: the value to assign to the field

    Returns:
        the updated properties object
    """
    properties[field] = value
    return properties
