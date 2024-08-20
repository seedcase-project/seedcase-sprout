from sprout.core.create_resource_raw_dir import create_resource_raw_dir


def test_create_resource_raw_dir_returns_new_resource_raw_directory(tmp_path):
    """Test that the create_resource_raw_dir function returns the directory if it exists.
    Args:
        tmp_path: Temporary directory created by pytest
    """
    assert create_resource_raw_dir(tmp_path) == tmp_path / "raw"
