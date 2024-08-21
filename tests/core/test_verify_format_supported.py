from pytest import mark, raises

from sprout.core.verify_format_supported import (
    SUPPORTED_FORMATS,
    UnsupportedFormatError,
    verify_format_supported,
)


@mark.parametrize("extension", SUPPORTED_FORMATS)
def test_accepts_supported_format(tmp_path, extension):
    """Given a supported file format, should return the path to the file."""
    file_path = tmp_path / f"test.{extension}"
    assert verify_format_supported(file_path) == file_path

@mark.parametrize("extension", ["xyz", "rtf", "tar.gz", "123", "*^%#", ".", " ", ""])
def test_rejects_unsupported_format(tmp_path, extension):
    """Given an unsupported file format, should raise an UnsupportedFormatError."""
    file_path = tmp_path / f"test.{extension}"
    with raises(UnsupportedFormatError):
        verify_format_supported(file_path)
