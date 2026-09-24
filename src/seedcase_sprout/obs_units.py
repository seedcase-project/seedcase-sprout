from copy import deepcopy
from dataclasses import replace
from pathlib import Path
from typing import Optional, cast

import polars as pl
import seedcase_soil as so

from seedcase_sprout.check_data import check_data
from seedcase_sprout.internals import _get_nested_attr
from seedcase_sprout.map_data_types import DATAPACKAGE_TO_POLARS
from seedcase_sprout.properties import (
    FieldProperties,
    FieldType,
    ResourceProperties,
    SproutProperties,
    TableSchemaProperties,
)


def read_obs_unit_file(
    path: Path, package_properties: SproutProperties
) -> pl.DataFrame:
    """Reads the IDs of observational units from a CSV at the given path."""
    if path.suffix.lower() != ".csv":
        raise ValueError(f"Expected a CSV file, got: {path.name!r}.")

    obs_unit_ids = pl.read_csv(path, has_header=True, infer_schema=True)
    _check_id_cols_in_all_resources(obs_unit_ids.columns, package_properties)
    obs_unit_properties = _get_obs_unit_properties(
        obs_unit_ids.columns, package_properties
    )
    if obs_unit_ids.is_empty():
        return _cast_id_cols_to_expected_types(obs_unit_ids, obs_unit_properties)
    _check_no_nulls_in_df(obs_unit_ids)
    return check_data(obs_unit_ids, obs_unit_properties)


def exclude_deleted_obs_units(
    data: pl.DataFrame, obs_unit_ids: pl.DataFrame
) -> pl.DataFrame:
    """Excludes the given observational units from the dataset.

    Both the data and the columns of the observational unit ID should be
    checked against the properties before using this function.
    """
    return data.join(obs_unit_ids, on=obs_unit_ids.columns, how="anti")


def _check_id_cols_in_all_resources(
    id_cols: list[str], package_properties: SproutProperties
) -> None:
    if not package_properties.resources:
        raise ValueError("No resources found in package properties.")
    fields_by_resource = so.fmap(package_properties.resources, _get_field_names)
    if so.keep(
        fields_by_resource, lambda fields: not _all_id_cols_in_resource(id_cols, fields)
    ):
        raise ValueError(
            f"The columns specifying the observational unit ID ({id_cols!r}) are not "
            "present in all resources."
        )


def _get_field_names(resource: ResourceProperties) -> list[str]:
    fields = cast(
        list[FieldProperties],
        _get_nested_attr(resource, "schema.fields", default=[]),
    )
    field_names = so.fmap(fields, lambda field: field.name)
    return cast(list[str], so.keep(field_names, lambda name: name is not None))


def _all_id_cols_in_resource(id_cols: list[str], fields: list[str]) -> bool:
    return all(so.fmap(id_cols, lambda col: col in fields))


def _get_obs_unit_properties(
    id_cols: list[str], package_properties: SproutProperties
) -> ResourceProperties:
    data_resource = cast(list[ResourceProperties], package_properties.resources)[0]
    obs_id_resource = deepcopy(data_resource)
    obs_id_schema = cast(TableSchemaProperties, obs_id_resource.schema)
    obs_id_fields = cast(list[FieldProperties], obs_id_schema.fields)
    obs_id_schema = replace(
        obs_id_schema,
        fields=so.keep(obs_id_fields, lambda field: field.name in id_cols),
    )
    return replace(obs_id_resource, schema=obs_id_schema)


def _cast_id_cols_to_expected_types(
    obs_unit_ids: pl.DataFrame, obs_unit_properties: ResourceProperties
) -> pl.DataFrame:
    fields = cast(
        list[FieldProperties],
        _get_nested_attr(obs_unit_properties, "schema.fields", default=[]),
    )
    polars_schema = {
        str(field.name): _get_obs_unit_polars_type(field.type) for field in fields
    }
    return obs_unit_ids.with_columns(
        pl.col(name).cast(polars_type) for name, polars_type in polars_schema.items()
    )


def _get_obs_unit_polars_type(
    datapackage_type: Optional[FieldType],
) -> type[pl.DataType]:
    polars_type = DATAPACKAGE_TO_POLARS.get(datapackage_type or "any")
    if not polars_type:
        raise NotImplementedError(
            f"Unexpected Data Package type {datapackage_type!r} for observational unit "
            "ID column."
        )
    return polars_type


def _check_no_nulls_in_df(df: pl.DataFrame) -> None:
    if df.null_count().sum_horizontal().item() > 0:
        raise ValueError(
            "IDs listed in the observational units file must not have "
            "null as a component."
        )
