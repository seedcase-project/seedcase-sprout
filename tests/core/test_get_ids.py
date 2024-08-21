from sprout.core.get_ids import get_ids


def test_get_single_id(tmp_path):
    """Test that the get_ids function returns a single ID."""
    (tmp_path / "1").mkdir()
    assert get_ids(tmp_path) == [1]


def test_get_only_dirs(tmp_path):
    """Return only directories - not files."""
    (tmp_path / "1").mkdir()
    (tmp_path / "datapackage.json").touch()
    (tmp_path / "1.txt").touch()
    (tmp_path / "2").touch()

    assert get_ids(tmp_path) == [1]


def test_empty_list_when_no_ids(tmp_path):
    """Return an empty list when there are no IDs."""
    assert get_ids(tmp_path) == []


def test_return_multiple_ids(tmp_path):
    """Test that the get_ids function returns multiple IDs."""
    (tmp_path / "1").mkdir()
    (tmp_path / "2").mkdir()

    assert sorted(get_ids(tmp_path)) == [1, 2]


def test_only_numbers_output(tmp_path):
    """Test that the get_ids function returns only numbers."""
    (tmp_path / "1").mkdir()
    (tmp_path / "a").mkdir()

    assert get_ids(tmp_path) == [1]


def test_different_numbers_output(tmp_path):
    """Test that the get_ids function returns numbers of any size."""
    (tmp_path / "1").mkdir()
    (tmp_path / "20").mkdir()
    (tmp_path / "999").mkdir()

    assert sorted(get_ids(tmp_path)) == [1, 20, 999]


def test_get_only_dirs_with_numbers(tmp_path):
    """Test that the get_ids function returns only directories with numbers."""
    (tmp_path / "1").mkdir()
    (tmp_path / "1a").mkdir()
    (tmp_path / "b3").mkdir()

    assert get_ids(tmp_path) == [1]
