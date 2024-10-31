from pathlib import Path

from frictionless import Resource

from sprout.core.get_extension import get_extension
from sprout.core.get_report_errors import get_report_errors
from sprout.core.mismatched_raw_data_error import MismatchedRawDataError
from sprout.core.path_sprout_root import path_sprout_root


def check_raw_data(resource_properties: dict, data_path: Path) -> Path:
    """Checks a raw data file against a set of resource properties.

    Args:
        resource_properties: The resource properties to check against.
        data_path: The path to the raw data file.

    Returns:
        The path to the raw data file, if the data match the properties.

    Raises:
        MismatchedRawDataError: If the data do not match the properties.
    """
    resource = Resource.from_descriptor(resource_properties)
    resource.format = get_extension(data_path)
    resource.scheme = "file"
    resource.basepath = str(path_sprout_root())
    resource.path = str(data_path.relative_to(path_sprout_root()))

    report = resource.validate()
    errors = get_report_errors(report)
    if errors:
        raise MismatchedRawDataError(errors, data_path)

    return data_path
