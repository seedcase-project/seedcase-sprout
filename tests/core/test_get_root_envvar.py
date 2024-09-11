import os

from sprout.core.get_root_envvar import get_root_envvar


def test_returns_root_envvar_if_set(tmp_path):
    """Returns the root environment variable SPROUT_ROOT if it is set."""
    # Given
    root = tmp_path / "sprout"
    root.mkdir
    os.environ["SPROUT_ROOT"] = str(root)

    # When
    root_path = get_root_envvar()

    # Then
    assert root_path == root


def test_returns_none_if_root_envvar_is_not_set():
    """Returns None if SPROUT_ROOT isn't set."""
    root_path = get_root_envvar()

    # Assert
    assert root_path is None
