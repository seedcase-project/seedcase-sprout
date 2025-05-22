from typing import Callable

from pytest import raises

from seedcase_sprout.core.check_datapackage.check_error import CheckError


def assert_raises_errors(
    fn: Callable, error_type: type[BaseException], error_count: int = None
) -> None:
    """Asserts that the function raises a group of errors of the given type."""
    with raises(ExceptionGroup) as error_info:
        fn()

    errors = error_info.value.exceptions
    assert all(isinstance(error, error_type) for error in errors)
    if error_count is not None:
        assert len(errors) == error_count


def assert_raises_check_errors(fn: Callable, error_count: int = None) -> None:
    """Asserts that the function raises a group of `CheckError`s."""
    assert_raises_errors(fn, CheckError, error_count)
