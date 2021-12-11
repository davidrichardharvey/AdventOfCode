import numpy as np
import pandas as pd
from math import prod

with open("input.txt") as aoc_input:
    heightmap = np.array([list(x.strip()) for x in aoc_input.readlines()], int)

print(heightmap)


def get_local_coordinates(x, y, max_x, max_y):
    x1 = max(x - 1, 0)
    x2 = min(x + 2, max_x)
    y1 = max(y - 1, 0)
    y2 = min(y + 2, max_y)
    return x1, x2, y1, y2


def check_low_point(heightmap_array, x, y):
    max_y, max_x = heightmap_array.shape
    x1, x2, y1, y2 = get_local_coordinates(x, y, max_x, max_y)
    square = heightmap_array[y1: y2, x1: x2]
    return square.min() == heightmap_array[y, x]

low_id = 100

def assign_basin(heightmap, x, y):
    if heightmap[y, x] != 9 and heightmap[y, x] != low_id:
        heightmap[y, x] = low_id
        max_y, max_x = heightmap.shape
        if x != 0:
            assign_basin(heightmap, max(x - 1, 0), y)
        if x != max_x:
            assign_basin(heightmap, min(x + 1, max_x - 1), y)
        if y != 0:
            assign_basin(heightmap, x, max(y - 1, 0))
        if y != max_y:
            assign_basin(heightmap, x, min(y + 1, max_y - 1))


lowest_points = []
for y in range(heightmap.shape[0]):
    for x in range(heightmap.shape[1]):
        if check_low_point(heightmap, x, y):
            lowest_points.append(heightmap[y, x])
            assign_basin(heightmap, x, y)
            low_id += 1

# print(sum(lowest_points) + len(lowest_points))
# print(len(lowest_points))
print(heightmap)
counts = np.unique(heightmap, return_counts=True)
freq = pd.Series(counts[1][1:], index=counts[0][1:]).sort_values(ascending=False)
print(freq)
print(prod(freq[0:3]))

