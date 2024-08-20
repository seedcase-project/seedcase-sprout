def create_next_id(existing_ids: list[int]) -> int:
    """Generates the next ID in a sequence, given a list of existing IDs. Starts at 1.

    Args:
        existing_ids: A list of existing IDs

    Returns:
        The newly generated ID
    """
    return max(existing_ids) + 1 if existing_ids else 1
