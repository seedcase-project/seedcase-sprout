from pytest import raises

from sprout.core.verify_is_directory import verify_is_directory


def test_verify_is_directory_returns_existing_directory(tmp_path):
    """Test that the verify_is_directory function returns the directory if it exists."""
    assert verify_is_directory(tmp_path) == tmp_path


def test_verify_is_directory_raises_error_with_non_existent_directory(tmp_path):
    """Test that the verify_is_directory function raises a NotADirectoryError
    if the directory does not exist."""
    with raises(
        NotADirectoryError,
        match=r"/non_existent_directory directory doesn't exist.",
    ):
        verify_is_directory(tmp_path / "non_existent_directory")


def test_verify_is_directory_returns_error_with_file(tmp_path):
    """Test that the verify_is_directory function raises a NotADirectoryError
    if the directory does not exist."""

    file_path = tmp_path / "test.py"
    file_path.write_text("# This is a temporary Python file")

    assert file_path.is_file()

    with raises(
        NotADirectoryError,
        match=r"/test.py directory doesn't exist.",
    ):
        verify_is_directory(file_path)
