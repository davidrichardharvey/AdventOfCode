from solution import compare_packets

def test_compare_packets():
    l1 = [1,1,3,1,1]
    l2 = [1,1,5,1,1]
    assert compare_packets(l1, l2) is True

    l1 = [[1],[2,3,4]]
    l2 = [[1],4]
    assert compare_packets(l1, l2) is True

    l1 = [9]
    l2 = [[8,7,6]]
    assert compare_packets(l1, l2) is False

    l1 = [[4,4],4,4]
    l2 = [[4,4],4,4,4]
    assert compare_packets(l1, l2) is True

    l1 = [7,7,7,7]
    l2 = [7,7,7]
    assert compare_packets(l1, l2) is False

    l1 = []
    l2 = [3]
    assert compare_packets(l1, l2) is True

    l1 = [[[]]]
    l2 = [[]]
    assert compare_packets(l1, l2) is False

    l1 = [1,[2,[3,[4,[5,6,7]]]],8,9]
    l2 = [1,[2,[3,[4,[5,6,0]]]],8,9]
    assert compare_packets(l1, l2) is False