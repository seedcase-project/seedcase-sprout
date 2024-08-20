from sprout.core.generate_next_id import generate_next_id


def test_generate_next_id_generates_first_id_correctly():
    """Given no existing IDs, it should return 1.
    """
    assert generate_next_id([]) == 1

def test_generate_next_id_generates_second_id_correctly():
    """Given one existing ID, it should return that ID + 1.
    """
    assert generate_next_id([1]) == 2

def test_generate_next_id_generates_large_id_correctly():
    """Given multiple, unordered, non-continuous existing IDs, 
    it should return the biggest one + 1.
    """
    assert generate_next_id([6, 333, 1, 45, 2, 3]) == 334
