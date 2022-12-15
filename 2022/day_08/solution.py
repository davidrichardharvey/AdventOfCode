import numpy as np

with open("input.txt") as file:
    raw = [line.strip() for line in file.readlines()]
    forest = list(map(lambda x: list(int(tree) for tree in x), map(lambda y: list(y), raw)))

grid = np.array(forest)

def visible(y, x):
    tree = grid[y, x]
    # top
    if max(grid[:y, x]) < tree:
        return True
    # bottom
    if max(grid[y+1:, x]) < tree:
        return True
    # left
    if max(grid[y, :x]) < tree:
        return True
    # right
    if max(grid[y, x+1:]) < tree:
        return True

total = 0
max_y, max_x = grid.shape
for y in range(max_y):
    for x in range(max_x):
        if y == 0 or x == 0 or y == max_y - 1 or x == max_x - 1:
            total += 1
        elif visible(y, x):
            total += 1

print(total)


def scenic_score(y, x):
    tree_height = grid[y, x]
    if y == 0 or x == 0 or y == max_y - 1 or x == max_x - 1:
        return 0

    up_score = 0
    for tree in np.flip(grid[:y, x]):
        up_score += 1
        if tree >= tree_height:
            break

    down_score = 0
    for tree in grid[y+1:, x]:
        down_score += 1
        if tree >= tree_height:
            break

    left_score = 0
    for tree in np.flip(grid[y, :x]):
        left_score += 1
        if tree >= tree_height:
            break

    right_score = 0
    for tree in grid[y, x+1:]:
        right_score += 1
        if tree >= tree_height:
            break

    return up_score * down_score * left_score * right_score

max_score = 0
for y in range(max_y):
    for x in range(max_x):
        max_score = max(max_score, scenic_score(y, x))

print(max_score)