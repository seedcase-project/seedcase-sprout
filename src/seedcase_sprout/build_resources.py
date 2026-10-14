from pathlib import Path
from typing import Optional, cast

import polars as pl
import seedcase_soil as so

from seedcase_sprout.config import Config, ResourceConfig, resolve_config_path
from seedcase_sprout.join_staging import join_staging
from seedcase_sprout.obs_units import (
    check_obs_unit_id_cols_in_all_resources,
    exclude_deleted_obs_units,
    read_obs_unit_file,
)
from seedcase_sprout.properties import SproutProperties
from seedcase_sprout.read_properties import read_properties
from seedcase_sprout.read_staging import read_staging
from seedcase_sprout.write_resource_data import write_resource_data


def build_resources(config: Config, project_dir: Path) -> list[Path]:
    """Convert a set of "staging" Parquet files into the final resources.

    Args:
        config: The configuration file for Sprout.
        project_dir: The directory containing the project files.

    Returns:
        The paths where the final resources were written.
    """
    metadata_path = resolve_config_path(
        path=config.metadata_file,
        project_dir=project_dir,
    )
    package_properties = read_properties(metadata_path)

    deleted_obs_unit_ids = None
    if unit_file := config.build_resources.delete_obs_units_file:
        unit_file = resolve_config_path(
            path=unit_file,
            project_dir=project_dir,
        )
        deleted_obs_unit_ids = read_obs_unit_file(unit_file)
        check_obs_unit_id_cols_in_all_resources(
            deleted_obs_unit_ids.columns, package_properties
        )

    output_paths = so.fmap(
        config.build_resources.resources,
        lambda resource: _build_resource(
            resource_config=resource,
            project_dir=project_dir,
            package_properties=package_properties,
            deleted_obs_unit_ids=deleted_obs_unit_ids,
        ),
    )
    return cast(list[Path], so.keep(output_paths, bool))


def _build_resource(
    resource_config: ResourceConfig,
    project_dir: Path,
    package_properties: SproutProperties,
    deleted_obs_unit_ids: Optional[pl.DataFrame],
) -> Optional[Path]:
    try:
        resource_properties = package_properties.get_resource_by_name(
            resource_config.name
        )
        input_dir = resolve_config_path(
            path=resource_config.input_dir,
            project_dir=project_dir,
        )
        staged_dfs = read_staging(
            resource_properties=resource_properties,
            paths=list(input_dir.glob("*.parquet")),
        )
        built_resource = join_staging(
            data_list=staged_dfs,
            resource_properties=resource_properties,
        )
        if deleted_obs_unit_ids is not None:
            built_resource = exclude_deleted_obs_units(
                built_resource, deleted_obs_unit_ids
            )

        output_path = resolve_config_path(
            path=resource_config.output_dir / f"{resource_config.name}.parquet",
            project_dir=project_dir,
        )
        write_resource_data(
            data=built_resource,
            resource_properties=resource_properties,
            data_path=output_path,
        )
        return output_path
    except Exception as e:  # noqa: BLE001 - building a resource can raise many different error types
        so.pretty_print(f"Resource {resource_config.name!r} could not be built: {e}.")
