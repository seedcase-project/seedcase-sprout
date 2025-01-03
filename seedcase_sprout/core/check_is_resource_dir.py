from pathlib import Path

from seedcase_sprout.core.check_is_dir import check_is_dir
from seedcase_sprout.core.get_ids import get_ids


def check_is_resource_dir(path: Path) -> Path:
    """Verifies that the path is a directory in the resources folder.

    Args:
        path: The Path to verify.

    Returns:
        Path if path is a directory.

    Raises:
        NotADirectoryError: If the path is not a directory. The error message
            includes existing IDs.
    """
    try:
        return check_is_dir(path)
    except NotADirectoryError as error:
        raise NotADirectoryError(
            f"This path can't be found, did you use the correct resource ID?"
            f"- Existing IDs: {get_ids(path.parent)}"
        ) from error
