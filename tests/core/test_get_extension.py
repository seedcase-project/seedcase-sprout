from pytest import mark, raises

from sprout.core.get_extension import get_extension


@mark.parametrize("filename, extension", [("test.csv", "csv"), ("test.tar.gz", "gz")])
def test_gets_extension_correctly(tmp_path, filename, extension):
    """Should return the file extension correctly."""
    path = tmp_path / filename
    path.touch()

    assert get_extension(path) == extension


def test_rejects_path_if_not_file(tmp_path):
    """Should throw FileNotFoundError if the path does not point to a file."""
    with raises(FileNotFoundError):
        get_extension(tmp_path)


def test_rejects_path_if_file_does_not_exist(tmp_path):
    """Should throw FileNotFoundError if the path does not exist."""
    with raises(FileNotFoundError):
        get_extension(tmp_path / "nonexistent.txt")
