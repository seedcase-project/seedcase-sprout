from pathlib import Path


def _list_rel_files(package_path: Path) -> list[Path]:
    """List all files relative to the package directory, excluding `.git` files.

    This is basically only used for the website to show what's been added.

    Args:
        package_path: The path to the package directory.

    Returns:
        A list of relative file paths within the package directory.
    """
    # Check if the path is a directory and exists
    if not package_path.is_dir():
        raise ValueError(f"{package_path} is not a directory.")

    # Get all files in the package directory, excluding .git files
    files = list(set(package_path.glob("**/*")) - set(package_path.glob(".git/**/*")))
    return [f.relative_to(package_path) for f in files]
