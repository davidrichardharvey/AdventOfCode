from day17 import count_active_neighbours, state

def test_initial_centre():
    assert count_active_neighbours(state, 6, 7, 7) == 5
    assert count_active_neighbours(state, 6, 6, 7) == 1
    assert count_active_neighbours(state, 5, 6, 6) == 1
