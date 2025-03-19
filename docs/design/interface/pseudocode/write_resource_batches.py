# ruff: noqa
def write_resource_batches(
    data: pl.DataFrame, resource_properties: ResourceProperties
) -> Path:
    """Writes the tidied, original data (as a DataFrame) into the resource's batch data folder.

    Writes the original raw data that's been read in as a Polars DataFrame
    into the resource location available in the `path` property of the
    `resource_properties`. This will save a timestamped, unique file
    name to store it as a backup. See the
    [design](https://sprout.seedcase-project.org/docs/design/) docs for an
    explanation of this batch file. Data is always checked against the properties
    before saving into the batch folder. Copies and compresses the file, and
    outputs the path object of the created file.

        Args:
            data: A Polars DataFrame object with the data to write to the batch folder.
                Use `read_resource_batches()` and `join_resource_batches()` to get the
                data ready to write.
            resource_properties: The properties object for the specific resource.
                Use `read_properties()` to read the properties for the resource
                and `get_properties()` to get the correct resource properties.

        Returns:
            The path to the written Parquet resource file.

        Examples:
            ```{python}
            #| eval: false
            ```
    """
    check_data(data, resource_properties)
    # Since `path` is to the `data.parquet` file.
    batch_dir = Path(resource_properties.path.parent / "batch")

    batch_resource_path = Path(batch_dir / create_batch_file_name())
    return write_parquet(data, batch_resource_path)


def create_batch_file_name() -> str:
    """Creates a timestamped, unique file name for the batch data file.

    This function creates a timestamped, unique file name for the batch data file
    that is being copied into the resource's batch data folder. This file name
    is used to store the data file as a backup. The file name will be
    in the format `{timestamp}-{uuid}.parquet`, where `timestamp` is the
    current time following ISO8601 format, and `uuid` is a universally unique ID.

        Returns:
            A path to a (potentially) new batch resource file.
    """
    # Untested code.
    timestamp = datetime.datetime.now().isoformat()
    uuid = str(uuid.uuid4())
    return f"{timestamp}-{uuid}.parquet"
