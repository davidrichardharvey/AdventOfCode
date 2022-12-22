import numpy as np

with open("example.txt") as file:
    raw = file.readlines()

max_x = 500
min_x = 1000
max_y = 0
min_y = 0
paths = []

for line in raw:
    path = []
    split = line.strip().split(" -> ")
    for coords in split:
        x, y = coords.split(",")
        int_x = int(x)
        int_y = int(y)
        max_x = int_x if int_x > max_x else max_x
        min_x = int_x if int_x < min_x else min_x
        max_y = int_y if int_y > max_y else max_y
        min_y = int_y if int_y < min_y else min_y
        path.append((int_x, int_y))
    paths.append(path)

print(paths)
print(max_x, max_y, min_x, min_y)
height = max_y - min_y
width = max_x - min_x

cave = np.full((height + 1, width + 1), ".")

for path in paths:
    prev = None
    for coords in path:
        if prev:
            x_start = min(coords[0], prev[0]) - min_x
            x_end = max(coords[0], prev[0]) - min_x
            y_start = min(coords[1], prev[1]) - min_y
            y_end = max(coords[1], prev[1]) - min_y
            cave[y_start:y_end+1, x_start:x_end+1] = '#'
        prev = coords

def print_cave(cave):
    for line in cave:
        print(' '.join(line))
    print('')

print_cave(cave)

def drop_sand():
    sand_x = 500 - min_x
    sand_y = 0
    while True:
        if cave[sand_y + 1, sand_x] == '.':
            sand_y += 1
        else:
            if cave[sand_y + 1, sand_x - 1] == '.':
                sand_y += 1
                sand_x -= 1
            elif cave[sand_y + 1, sand_x + 1] == '.':
                sand_y += 1
                sand_x += 1
            else:
                break
    cave[sand_y, sand_x] = 'o'

s = 0
while True:
    try:
        drop_sand()
        print_cave(cave)
        s += 1
    except:
        print(s)
        break