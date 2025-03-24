# ruff: noqa
def _check_column_names(
    data: DataFrame, resource_properties: ResourceProperties
) -> str:
    """Check that column names in `data` match those in `resource_properties`.

    Args:
        data: The data to check.
        resource_properties: The resource properties to check against.

    Returns:
        The data if the column names match.

    Raises:
        CheckError: If the column names do not match then the error message will
            include which names are mismatching between the `data` and `resource_properties`.
    """
    check_resource_properties(resource_properties)

    names_in_data = data.schema.names()
    names_in_resource = _get_property_field_names(resource_properties)

    difference_in_data = set(names_in_data) - set(names_in_resource)
    difference_in_properties = set(names_in_resource) - set(names_in_data)

    # Should look something like maybe with both mismatch:
    # "Mismatch between names in data vs properties: "
    #
    # "- Data: {difference_in_names}."
    # "- Resource properties: {names_in_resource}."
    #
    # Or if mismatch in e.g. data only:
    # "Mismatch between names in data vs properties: "
    #
    # "- Data: {difference_in_names}."
    # TODO: This function name is a placeholder for getting the message to look like above.
    error_message = _format_column_name_error_message(
        difference_in_data, difference_in_properties
    )

    if error_message:
        raise CheckError(error_message)

    return data
