from sprout.core.create_dir import create_dir


def test_create_dir_existing_folder(tmp_path):
    """Checks for an existing folder and returns the name
    if the folder already exists.
    """
    # Create a temporary directory
    folder_path = tmp_path / "existing_folder"
    folder_path.mkdir()

    # Call the create_dir function
    result = create_dir(folder_path)

    # Check if the result is equal to the folder path
    assert result == folder_path


def test_create_dir_new_folder(tmp_path):
    """Create a new folder and returns the path correctly."""
    # Create a temporary directory
    folder_path = tmp_path / "new_folder"

    # Call the create_dir function
    result = create_dir(folder_path)

    # Check if the folder is created
    assert folder_path.exists()

    # Check if the result is equal to the folder path
    assert result == folder_path
