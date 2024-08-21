from sprout.core.create_resource_path import create_resource_path


def test_return_the_resource_path(tmp_path):
    """Return the resource path."""
    assert create_resource_path(tmp_path, 1) == tmp_path / "1"
