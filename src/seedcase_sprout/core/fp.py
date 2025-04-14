"""Mimicking the functional programming tools from R and the R package purrr."""


def _map(x: list, fn: callable) -> list:
    """Map a function over a list."""
    return list(map(fn, x))
