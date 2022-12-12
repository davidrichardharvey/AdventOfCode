from solution import split_bag

def test_split_bag():
    example = "vJrwpWtwJgWrhcsFMMfFFhFp"
    expected = "vJrwpWtwJgWr", "hcsFMMfFFhFp"
    returned = split_bag(example)
    assert expected == returned
