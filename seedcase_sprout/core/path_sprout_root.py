from pathlib import Path

from seedcase_sprout.core.create_root_path import create_root_path
from seedcase_sprout.core.get_root_envvar import get_root_envvar


def path_sprout_root() -> Path:
    """Get Sprout's root path.

    Returns:
        A Path to Sprout's root directory.
    """
    return get_root_envvar() or create_root_path()
