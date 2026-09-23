from pathlib import Path
from typing import Optional, cast

import polars as pl
import seedcase_soil as so

from seedcase_sprout.properties import ResourceProperties, SproutProperties


def read_obs_unit_file(
    path: Optional[Path], package_properties: SproutProperties
) -> Optional[pl.DataFrame]:
    """Reads the IDs of observational units from a CSV at the given path."""
    # TODO: decide if config checks should be centralised (here: units file must be a
    # CSV and obs. unit ID cols must be fields in all resources)
    if not path:
        return None
    if path.suffix.lower() != ".csv":
        raise ValueError(f"Expected a CSV file, got: {path.name!r}.")

    obs_unit_ids = pl.read_csv(path, has_header=True, infer_schema=True)
    _check_no_nulls_in_df(obs_unit_ids)
    _check_id_cols_in_all_resources(obs_unit_ids.columns, package_properties)
    return obs_unit_ids


def exclude_deleted_obs_units(
    data: pl.DataFrame, obs_unit_ids: pl.DataFrame
) -> pl.DataFrame:
    """Excludes the given observational units from the dataset.

    Both the data and the columns of the observational unit ID should be
    checked against the properties before using this function.
    """
    if obs_unit_ids.is_empty():
        return data
    return data.join(obs_unit_ids, on=obs_unit_ids.columns, how="anti")


def _check_no_nulls_in_df(df: pl.DataFrame) -> None:
    if df.null_count().sum_horizontal().item() > 0:
        raise ValueError(
            "IDs listed in the observational units file must not have "
            "null as a component."
        )


def _check_id_cols_in_all_resources(
    id_cols: list[str], package_properties: SproutProperties
) -> None:
    if not package_properties.resources:
        raise ValueError("No resources found in package properties.")
    fields_by_resource = so.fmap(package_properties.resources, _get_field_names)
    if so.keep(
        fields_by_resource, lambda fields: not _id_cols_in_fields(id_cols, fields)
    ):
        raise ValueError(
            f"The columns specifying the observational unit ID ({id_cols!r}) are not "
            "present in all resources."
        )


def _get_field_names(resource: ResourceProperties) -> list[str]:
    if not resource.schema or not (fields := resource.schema.fields):
        return []
    field_names = so.fmap(fields, lambda field: field.name)
    return cast(list[str], so.keep(field_names, lambda name: name is not None))


def _id_cols_in_fields(id_cols: list[str], fields: list[str]) -> bool:
    return all(so.fmap(id_cols, lambda col: col in fields))
