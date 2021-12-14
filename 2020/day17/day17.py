import numpy as np
np.set_printoptions(threshold=np.inf)

with open("day17example.txt") as file:
    initial_state = file.readlines()
    initial_state = np.array(list(map(lambda x: list(x.strip().replace(".","0").replace("#","1")), initial_state)), dtype=np.int8)
    x, y = initial_state.shape
    state = np.zeros((13, x + 12, y + 12), dtype=np.int8)
    state[6, 6:6+x, 6:6+x] = initial_state


def count_active_neighbours(state_array: np.ndarray, x: int, y: int, z: int) -> int:
    region = state_array[x-1:x+2, y-1:y+2, z-1:z+2]
    print(region)
    return region.sum() - state_array[x, y, z]


def simulate_cycle(state_array: np.ndarray) -> np.ndarray:
    new_array = np.zeros(state_array.shape, dtype=np.int8)
    x, y, z = state_array.shape
    for xi in range(1, x - 2):
        for yi in range(1, y - 2):
            for zi in range(1, z - 2):
                neighs = count_active_neighbours(state_array, xi, yi, zi)
                if state_array[xi, yi, zi] == 1 and 2 >= neighs <= 3:
                    new_array[xi, yi, zi] = 1
                elif state_array[xi, yi, zi] == 0 and neighs == 3:
                    new_array[xi, yi, zi] = 1
    return new_array

