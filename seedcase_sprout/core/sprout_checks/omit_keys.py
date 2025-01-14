def omit_keys(dictionary: dict, keys: list[str]) -> dict:
    """Returns a new dictionary with the specified keys omitted.

    Args:
        dictionary: The input dictionary.
        keys: A list of keys to omit from the dictionary.

    Returns:
        A new dictionary excluding the specified keys.
    """
    return {key: value for key, value in dictionary.items() if key not in keys}
