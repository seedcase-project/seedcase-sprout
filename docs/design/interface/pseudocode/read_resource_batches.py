# ruff: noqa
def read_resource_batches(
    paths: list[Path], resource_properties: ResourceProperties
) -> list[DataFrame]:
    """Reads all the batch resource file(s) into a list of (Polars) DataFrames.

    This function takes the file(s) given by `paths`, reads them in as Polars
    DataFrames as a list and does some checks on each of the DataFrames in the list
    based on the `resource_properties`. The `resource_properties` object is used
    to check the data and ensure it is correct. This function doesn't write to
    Parquet, so that you can do any additional processing to the data before
    saving it as a Parquet file.  While Sprout generally assumes that the files
    stored in the `resources/<id>/batch/` folder are already correctly
    structured and tidy, this function still runs checks to ensure the data are
    correct by comparing to the properties.

    Examples:

        ``` python
        import seedcase_sprout.core as sp

        sp.read_resource_batches(
            paths=sp.path_resources_batch_files(1),
            resource_properties=sp.example_resource_properties(),
        )
        ```

    Args:
        paths: A list of paths for all the files in the resource's `batch/` folder.
            Use `path_resource_batch_files()` to help provide the correct paths to the
            batch files.
        resource_properties: The `ResourceProperties` object that contains the properties
            of the resource you want to check the data against.

    Returns:
        Outputs a list of DataFrame objects from all the batch files.
    """
    # Not sure if this is the correct way to verify multiple files.
    map(check_is_file, paths)
    check_resource_properties(resource_properties)

    data_list = list(map(pl.read_parquet, paths))

    list(map(check_data, data_list, resource_properties))

    return data_list
