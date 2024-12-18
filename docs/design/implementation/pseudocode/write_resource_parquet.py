# ruff: noqa
def write_resource_parquet(
    raw_files_path: list[Path], parquet_path: Path, properties_path: Path
) -> Path:
    """Merge all raw resource file(s) and write into a Parquet file.

    This function takes the file(s) provided by `raw_files_path` and merges them into
    a `data.parquet` file provided by `parquet_path`. While Sprout generally assumes
    that the files stored in the `resources/raw/` folder have already been
    verified and validated, this function does some quick verification checks
    of the data after reading it into Python from the raw file(s) by comparing
    with the current properties given by the `properties_path`. All data in the
    `resources/raw/` folder will be merged into one single data object and then
    written back to the Parquet file. The Parquet file will be overwritten.

    Examples:

        ``` python
        import seedcase_sprout.core as sp

        sp.write_resource_parquet(
            raw_files_path=sp.path_resources_raw_files(1, 1),
            parquet_path=sp.path_resource_data(1, 1),
            properties_path=sp.path_package_properties(1, 1),
        )
        ```

    Args:
        raw_files_path: A list of paths for all the raw files, mostly commonly stored in the
            `.csv.gz` format. Use `path_resource_raw_files()` to help provide the
            correct paths to the raw files.
        parquet_path: The path to the Use `path_resource_data()` to help provide
            the correct path location for the resource's `data.parquet` file.
        properties_path: The path to the properties for this resource. Use
            `path_package_properties()` to help give the correct location.

    Returns:
        Outputs the path object of the created Parquet file.
    """
    # Not sure if this is the correct way to verify multiple files.
    [verify_is_file(path) for path in raw_files_path]

    data = read_raw_files(raw_file)

    # Confirms that the data matches the resource properties found in `datapackage.json`.
    # Not sure if this is the best solution here to load in the properties file.
    verify_is_file(properties_path)
    properties = read_json(properties_path)

    # This function could be several, e.g. verify_data_column_types(), verify_data_column_names()?
    verify_data(data, properties)

    # Could include validation here?
    # validate_data(data, properties)

    return write_parquet(data, parquet_path)


def write_parquet(data: DataFrame, path: Path) -> Path:
    return path


def read_raw_files(paths: list[Path]) -> DataFrame:
    # Can read gzip files.
    data_list = [polars.read_csv(path) for path in paths]
    # Merge them all together.
    data = polars.concat(data_list)
    return data


def verify_data(data: DataFrame, properties: dict) -> Path:
    # Compare against the properties for:
    # - Header names
    # - Data types
    # - Number of rows?
    # - Others?

    # Error if fails, data if pass
    return data
