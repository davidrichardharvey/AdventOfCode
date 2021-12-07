from aoc_func import read_input_text
import numpy as np

lines = read_input_text("input.txt")
lines = [x.split(' -> ') for x in lines]
lines = [[x[0].split(','), x[1].split(',')] for x in lines]
lines = [(int(x[0][0]), int(x[0][1]), int(x[1][0]), int(x[1][1])) for x in lines]
print(lines)

max_x = max(map(lambda x: max(x[0], x[2]), lines))
max_y = max(map(lambda y: max(y[1], y[3]), lines))

print(max_x, max_y)

grid = np.zeros((max_x + 1, max_y + 1), int)
print(grid)

for instruction in lines:
    y1, x1, y2, x2 = instruction
    if x1 == x2:
        y1, y2 = (y1, y2) if y1 < y2 else (y2, y1)
        grid[x1, y1:y2+1] += 1
    elif y1 == y2:
        x1, x2 = (x1, x2) if x1 < x2 else (x2, x1)
        grid[x1:x2+1, y1] += 1
    else:
        # Solve diagonals
        xs = range(x1, x2+1) if x1 < x2 else range(x1, x2-1, -1)
        ys = range(y1, y2+1) if y1 < y2 else range(y1, y2-1, -1)
        for i, x in enumerate(xs):
            y = ys[i]
            grid[x, y] += 1

print(grid)

print((grid > 1).sum())
