from pathlib import Path

from seedcase_sprout.core.create_sprout_global_path import create_sprout_global_path
from seedcase_sprout.core.get_sprout_global_envvar import get_sprout_global_envvar


def path_sprout_global() -> Path:
    """Gets Sprout's global path location.

    Returns:
        The path to Sprout's global directory.

    Examples:
        ```{python}
        #| output: true
        import os

        import seedcase_sprout.core as sp

        # Set global path for the example
        os.environ["SPROUT_GLOBAL"] = ".storage/"

        sp.path_sprout_global()
        ```
    """
    return get_sprout_global_envvar() or create_sprout_global_path()
