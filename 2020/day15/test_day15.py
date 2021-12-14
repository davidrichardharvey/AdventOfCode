from day15 import return_nth
import pytest


@pytest.mark.parametrize("test_input, expected", [
    ([1, 3, 2], 1),
    ([2, 1, 3], 10),
    ([1, 2, 3], 27),
    ([2, 3, 1], 78),
    ([3, 2, 1], 438),
    ([3, 1, 2], 1836)
])
def test_return_nth(test_input, expected):
    assert return_nth(test_input, 2020) == expected

def test_without_para():
    assert return_nth([0,3,6], 2020) == 436