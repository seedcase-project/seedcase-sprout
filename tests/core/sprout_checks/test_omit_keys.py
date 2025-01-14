from pytest import mark

from seedcase_sprout.core.sprout_checks.omit_keys import omit_keys


@mark.parametrize(
    "dictionary,keys,expected",
    [
        ({}, [], {}),
        ({}, ["a", "c"], {}),
        ({"a": "aaa"}, [], {"a": "aaa"}),
        ({"a": "aaa", "b": "bbb"}, ["b"], {"a": "aaa"}),
        ({"a": "aaa", "b": "bbb", "c": "ccc"}, ["a", "c"], {"b": "bbb"}),
    ],
)
def test_omits_correct_items(dictionary, keys, expected):
    """Should omit the correct items."""
    assert omit_keys(dictionary, keys) == expected
