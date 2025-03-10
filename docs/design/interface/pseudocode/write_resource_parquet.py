# ruff: noqa
def write_resource_parquet(
    data: DataFrame, resource_properties: ResourceProperties
) -> Path:
    """Check and write the resource data into a Parquet file.

    This function takes the `data` built from `build_resource_data()`, checks it
    against the `resource_properties`, and then writes the data to the resources
    `data.parquet` file .  The Parquet file is saved based on the path found in
    `ResourceProperties.path` and is always overwritten.  Before writing, this
    function does a check against the `resource_properties` to ensure that the
    data is correctly structured and tidy.

    Examples:

        ``` python
        import seedcase_sprout.core as sp

        data = sp.build_resource_data(
            raw_files_path=sp.path_resources_raw_files(1),
            resource_properties=sp.example_resource_properties,
        )

        sp.write_resource_parquet(data, sp.example_resource_properties)
        ```

    Args:
        data: A DataFrame object with the resources data from the files in its
            `raw/` folder.
        resource_properties: The `ResourceProperties` object that contains the
            properties of the resource you want to create the Parquet file for.

    Returns:
        Outputs the path of the created Parquet file.
    """
    check_resource_properties(resource_properties)

    # This function could be several functions or the one full function.
    check_data(data, resource_properties)

    # Not sure the correct import for this.
    return polars.write_parquet(data, resource_properties["path"], overwrite=True)
