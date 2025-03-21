# ruff: noqa
def join_resource_batches(
    data_list: list[DataFrame], resource_properties: ResourceProperties
) -> DataFrame:
    """Joins all batch resource DataFrames into a single (Polars) DataFrame.

    This function takes the list of DataFrames, joins them together, does a
    check to confirm the data are ok after joining against the `resource_properties`,
    and then drops any duplicate observational units.

    If there are any duplicate observational units in the data, only the most recent
    observational unit will be kept. This way, if there are any errors or mistakes
    in older batch files that have been corrected in later files, the mistake can still
    be kept, but won't impact the data that will actually be used.

    Examples:

        ``` python
        import seedcase_sprout.core as sp

        sp.join_resource_batches(
            batch_files_path=sp.path_resources_batch_files(1),
            resource_properties=sp.example_resource_properties,
        )
        ```

    Args:
        data_list: A list of Polars DataFrames for all the batch files. Use `read_resource_batches()` get a list of DataFrames that have been checked against the properties individually.
        resource_properties: The `ResourceProperties` object that contains the properties
            of the resource to check the data against.

    Returns:
        Outputs a single DataFrame object of all the batch data with duplicate observational units removed.
    """
    check_resource_properties(resource_properties)

    data = polars.concat(data_list)
    data = drop_duplicate_obs_units(data)
    check_data(data, resource_properties)

    return data


def drop_duplicate_obs_units(data: DataFrame) -> DataFrame:
    # Drop duplicates based on the observation unit, keeping only the most
    # recent one. This allows older batch files to contain potentially wrong
    # data that was corrected in the most recent file.
    return data.drop_duplicates()
