from pytest import fixture

from sprout.core.write_file import write_file


@fixture
def file_content():
    return "This is test content."


def test_returns_path(tmp_path, file_content):
    """Tests that the path is returned."""
    file_path = tmp_path / "test.txt"

    assert write_file(file_path, file_content) == file_path


def test_creates_a_file_with_the_given_content(tmp_path, file_content):
    """Tests that a file with the given content is created."""
    file_path = tmp_path / "test.md"

    assert write_file(file_path, file_content) == file_path
    assert file_path.is_file()
    assert file_path.read_text() == file_content
