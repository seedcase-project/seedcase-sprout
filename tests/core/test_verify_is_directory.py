from pytest import raises

from sprout.core.verify_is_directory import verify_is_directory


def test_verify_is_directory_returns_existing_directory(tmp_path):
    """Test that the verify_is_directory function returns the directory if it exists.
    """
    assert verify_is_directory(tmp_path) == tmp_path


def test_verify_is_directory_raises_not_a_directory_error(tmp_path):
    """Test that the verify_is_directory function raises a NotADirectoryError
    if the directory does not exist."""
    with raises(
        NotADirectoryError,
        match=r"/non_existent_directory is not an existing directory",
    ):
        verify_is_directory(tmp_path / "non_existent_directory")
