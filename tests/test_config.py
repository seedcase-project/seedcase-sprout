from pathlib import Path

from pytest import fixture, raises

from seedcase_sprout.config import (
    BuildResourcesConfig,
    Config,
    ResourceConfig,
    load_config,
)


def sprout_config(metadata_file: str = "metadata/metadata.json") -> Config:
    return Config(
        metadata_file=Path(metadata_file),
        build_resources=BuildResourcesConfig(
            delete_obs_units_file=Path("units.csv"),
            resources=[
                ResourceConfig(
                    name="demographics",
                    input_dir=Path("staging") / "demographics",
                    output_dir=Path("resources"),
                    extras={"key": "value"},
                )
            ],
        ),
    )


config_toml = """
metadata-file = "{metadata}"

[build-resources]
delete-obs-units-file = "units.csv"

[[build-resources.resources]]
name = "demographics"
input-dir = "staging/demographics"
output-dir = "resources"

[build-resources.resources.extras]
key = "value"
"""


def _create_toml(path: Path) -> str:
    metadata_text = "".join(path.parts[-2:])
    path.parent.mkdir(exist_ok=True, parents=True)
    path.write_text(config_toml.format(metadata=metadata_text))
    return metadata_text


@fixture
def _custom_config_toml(tmp_path) -> str:
    path = tmp_path / "custom.toml"
    return _create_toml(path)


@fixture
def _config_sprout_toml(tmp_path) -> str:
    path = tmp_path / ".config" / "sprout.toml"
    return _create_toml(path)


@fixture
def _sprout_toml(tmp_path) -> str:
    path = tmp_path / "sprout.toml"
    return _create_toml(path)


@fixture
def _dot_sprout_toml(tmp_path) -> str:
    path = tmp_path / ".sprout.toml"
    return _create_toml(path)


@fixture
def _pyproject_toml(tmp_path) -> str:
    path = tmp_path / "pyproject.toml"
    toml = config_toml.format(metadata="pyproject").replace(
        "build-resources", "tool.sprout.build-resources"
    )
    toml = f"[tool.sprout]\n{toml}"
    path.write_text(toml)
    return "pyproject"


def test_config_created_from_dict_with_custom_values():
    config_dict = {
        "metadata_file": "metadata/metadata.json",
        "build_resources": {
            "delete_obs_units_file": "units.csv",
            "resources": [
                {
                    "name": "demographics",
                    "input_dir": "staging/demographics",
                    "output_dir": "resources",
                    "extras": {"key": "value"},
                }
            ],
        },
    }

    assert Config.model_validate(config_dict) == sprout_config()


def test_config_created_from_dict_with_default_values():
    assert Config.model_validate({}) == Config(
        metadata_file=Path("datapackage.json"),
        build_resources=BuildResourcesConfig(
            delete_obs_units_file=None,
            resources=[],
        ),
    )


def test_loads_config_from_custom_path_as_first_preference(
    tmp_path,
    _custom_config_toml,
    _config_sprout_toml,
    _sprout_toml,
    _dot_sprout_toml,
    _pyproject_toml,
):
    config = load_config(project_dir=tmp_path, config_path=tmp_path / "custom.toml")

    assert config == sprout_config(_custom_config_toml)


def test_loads_config_from_config_sprout_toml_as_first_fallback(
    tmp_path, _config_sprout_toml, _sprout_toml, _dot_sprout_toml, _pyproject_toml
):
    config = load_config(project_dir=tmp_path)

    assert config == sprout_config(_config_sprout_toml)


def test_loads_config_from_sprout_toml_as_second_fallback(
    tmp_path, _sprout_toml, _dot_sprout_toml, _pyproject_toml
):
    config = load_config(project_dir=tmp_path)

    assert config == sprout_config(_sprout_toml)


def test_loads_config_from_dot_sprout_toml_as_third_fallback(
    tmp_path, _dot_sprout_toml, _pyproject_toml
):

    config = load_config(project_dir=tmp_path)

    assert config == sprout_config(_dot_sprout_toml)


def test_loads_config_from_pyproject_toml_as_fourth_fallback(tmp_path, _pyproject_toml):

    config = load_config(project_dir=tmp_path)

    assert config == sprout_config(_pyproject_toml)


def test_loads_config_from_empty_file(tmp_path):
    (tmp_path / "sprout.toml").touch()

    config = load_config(project_dir=tmp_path)

    assert config == Config()


def test_errors_when_custom_path_given_but_file_missing(
    tmp_path, _config_sprout_toml, _sprout_toml, _dot_sprout_toml, _pyproject_toml
):
    with raises(FileNotFoundError):
        load_config(project_dir=tmp_path, config_path=tmp_path / "custom.toml")


def test_errors_when_pyproject_exists_but_config_missing(tmp_path):
    (tmp_path / "pyproject.toml").touch()

    with raises(FileNotFoundError):
        load_config(project_dir=tmp_path)


def test_errors_when_no_custom_path_given_with_all_files_missing(tmp_path):
    with raises(FileNotFoundError):
        load_config(project_dir=tmp_path)
