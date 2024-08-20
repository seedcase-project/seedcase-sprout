from pytest import raises

from sprout.core.get_ids import get_ids


def test_get_ids_returns_list_of_resources(tmp_path):
    """Test that the get_ids function returns a list of resources.

    Args:
        tmp_path: Temporary directory created by pytest
    """
    (tmp_path / "1").mkdir()  # single digit
    (tmp_path / "20").mkdir()  # double digit
    (tmp_path / "datapackage.json").mkdir()  # file
    (tmp_path / "resources").mkdir()  # directory without digits

    assert sorted(get_ids(tmp_path)) == [1, 20]


def test_get_ids_returns_empty_list(tmp_path):
    """Test that the get_ids function returns the directory if it exists.

    Args:
        tmp_path: Temporary directory created by pytest
    """
    assert get_ids(tmp_path) == []


# What happens if it's not a directory?
def test_get_ids_raises_not_a_directory_error(tmp_path):
    """Test that the get_ids function raises a NotADirectoryError if the path is not a directory.

    Args:
        tmp_path: Temporary directory created by pytest
    """
    with raises(
        NotADirectoryError,
        match=r"/non_existent_directory is not an existing directory",
    ):
        get_ids(tmp_path / "non_existent_directory")
