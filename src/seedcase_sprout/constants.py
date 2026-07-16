from importlib.resources import files
from pathlib import Path

"""Constants in the seedcase_sprout module."""

"""The format of the timestamp used in the staging file name."""
STAGING_TIMESTAMP_FORMAT = "%Y-%m-%dT%H%M%SZ"

"""Regex pattern for timestamps with the format '%Y-%m-%dT%H%M%SZ'. Must match the
format used by STAGING_TIMESTAMP_FORMAT"""
STAGING_TIMESTAMP_PATTERN = r"\d{4}-\d{2}-\d{2}T\d{6}Z"

"""The name of the timestamp column added to the staging data (only used internally)."""
STAGING_TIMESTAMP_COLUMN_NAME = "_staging_file_timestamp_"

TEMPLATES_PATH = Path(str(files("seedcase_sprout").joinpath("templates")))
