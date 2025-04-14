"""Mimicking the functional programming tools from R and the R package purrr."""

from itertools import repeat


def _map2(x: list, y: list, fn: callable) -> list:
    """Use a function on each item in two lists, placed on the first two arguments.

    This function is similar to the `map2()` function from the R package purrr.
    It takes two lists and a function as arguments. The function is applied to
    each pair of elements from the two lists. If the second list has only one
    element, it is repeated for each element in the first list. The output
    is the same size as the first list.

    This makes the function a bit more user-friendly compared to the built-in
    `map()` function, which requires the same length for both lists.

    Args:
        x: The first list to use the function on.
        y: The second list that must have the same items as the first `x` list or one
            item to be repeated.
        fn: The function to use on each pair of items in the two lists above.

    Returns:
        A list of the results from the function used on each item in the two lists.

    Examples:
        ```{python}
        from seedcase_sprout.core.internals.functionals import _map2
        def add(a, b):
            return a + b
        _map2(
            x=[1, 2, 3],
            y=[10],
            fn=add
        )

        _map2(
            x=[1, 2, 3],
            y=[10, 20, 30],
            fn=add
        )
        ```
    """
    if len(y) == 1:
        y = repeat(y[0], len(x))
    return list(map(fn, x, y))
