import tomllib
from dataclasses import field
from pathlib import Path
from typing import Any, Optional

import seedcase_soil as so
from pydantic import (
    BaseModel,
    ConfigDict,
)


class ConfigFile(BaseModel, frozen=True):
    """Pydantic model for TOML config files."""

    model_config = ConfigDict(
        alias_generator=lambda string: string.replace("_", "-"),
        populate_by_name=True,
    )


class ResourceConfig(ConfigFile, frozen=True):
    """Configuration for a resource to be built."""

    name: str
    input_dir: Path
    output_dir: Path
    extras: Optional[dict[str, Any]] = None


class BuildResourcesConfig(ConfigFile, frozen=True):
    """Configuration for the `build-resources` CLI command."""

    delete_obs_units_file: Optional[Path] = None
    resources: list[ResourceConfig] = field(default_factory=list)


class Config(ConfigFile, frozen=True):
    """Configuration for Sprout."""

    metadata_file: Path = Path("datapackage.json")
    build_resources: BuildResourcesConfig = field(default_factory=BuildResourcesConfig)


def resolve_config_path(path: Path, project_dir: Path) -> Path:
    """Resolves relative config paths against the project root."""
    return path if path.is_absolute() else project_dir / path


def load_config(project_dir: Path, config_path: Optional[Path] = None) -> Config:
    """Loads the Sprout configuration.

    Uses `config_path` if given. If no `config_path` is given, it first tries
    `.config/sprout.toml`, then `sprout.toml`, and `.sprout.toml` in that
    order, and finally `pyproject.toml` under `[tool.sprout]`.
    """
    if config_path is not None:
        return _load_config_from_path(config_path)
    config = _load_config_from_default_paths(
        project_dir
    ) or _load_config_from_pyproject(project_dir)
    if config is None:
        raise FileNotFoundError(
            "No configuration file found for Sprout. Please create a "
            "`.config/sprout.toml`, `sprout.toml`, or `.sprout.toml` file, or add a "
            "`[tool.sprout]` section to your `pyproject.toml`."
        )
    return config


def _load_config_from_path(path: Path) -> Config:
    """Load the Sprout configuration from a custom path."""
    with path.open("rb") as f:
        config = tomllib.load(f)
    return Config.model_validate(config)


def _load_config_from_default_paths(project_dir: Path) -> Optional[Config]:
    paths = [
        project_dir / ".config" / "sprout.toml",
        project_dir / "sprout.toml",
        project_dir / ".sprout.toml",
    ]
    files = so.keep(
        paths,
        lambda path: path.is_file(),
    )
    return _load_config_from_path(files[0]) if files else None


def _load_config_from_pyproject(project_dir: Path) -> Optional[Config]:
    pyproject_path = project_dir / "pyproject.toml"
    if not pyproject_path.is_file():
        return None

    with pyproject_path.open("rb") as f:
        pyproject = tomllib.load(f)
    sprout_config = pyproject.get("tool", {}).get("sprout")
    return Config.model_validate(sprout_config) if sprout_config else None
