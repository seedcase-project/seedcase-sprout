from sprout.core.create_root_path import create_root_path


def test_returns_root_path():
    """Returns root path o."""
    root_path = create_root_path()

    assert root_path.name == "sprout"
