"""Constants for the sprout_checks module."""

"""regex for UUID4, from https://gist.github.com/johnelliott/cf77003f72f889abbc3f32785fa3df8d?permalink_comment_id=4318295#gistcomment-4318295"""
UUID4_PATTERN = r"[0-9a-f]{8}-[0-9a-f]{4}-4[0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}"

"""regex for timestamp with format '%Y-%m-%dT%H%M%SZ'. Should match the format used by
BATCH_TIMESTAMP_FORMAT in sprout.core"""
TIMESTAMP_PATTERN = r"^\d{4}-\d{2}-\d{2}T\d{6}Z"

"""regex for batch file name"""
BATCH_FILE_NAME_PATTERN = rf"^{TIMESTAMP_PATTERN}-{UUID4_PATTERN}.parquet$"
