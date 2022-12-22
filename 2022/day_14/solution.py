import numpy as np

with open("input.txt") as file:
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
        int_y = int(y) + 1
        max_x = int_x if int_x > max_x else max_x
        min_x = int_x if int_x < min_x else min_x
        max_y = int_y if int_y > max_y else max_y
        min_y = int_y if int_y < min_y else min_y
        path.append((int_x, int_y))
    paths.append(path)

print(paths)
print(max_x, max_y, min_x, min_y)
height = max_y - min_y + 2
width = max_x - min_x

cave = np.full((height + 1, width + 1), ".")
cave[height, :] = '#'


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

class Cave:
    def __init__(self, cave):
        self.cave = cave
        self.sand_x_start = 500 - min_x
        self.sand_y_start = 1

    def print_cave(self):
        for line in self.cave:
            print(' '.join(line))
        print('')

    def drop_sand(self):
        sand_x = self.sand_x_start
        sand_y = self.sand_y_start
        while True:
            if sand_x == 0:
                self.cave = np.insert(self.cave, 0, '.', axis=1)
                self.cave[height, :] = '#'
                sand_x += 1
                self.sand_x_start += 1
            elif sand_x == self.cave.shape[-1] - 1:
                self.cave = np.append(self.cave, np.full((height+1, 1), '.'), axis=1)
                self.cave[height, :] = '#'

            if self.cave[sand_y + 1, sand_x] == '.':
                sand_y += 1
            else:
                if self.cave[sand_y + 1, sand_x - 1] == '.':
                    sand_y += 1
                    sand_x -= 1
                elif self.cave[sand_y + 1, sand_x + 1] == '.':
                    sand_y += 1
                    sand_x += 1
                else:
                    break

        self.cave[sand_y, sand_x] = 'o'

    def check_finish(self):
        return self.cave[self.sand_y_start, self.sand_x_start] == 'o'

c = Cave(cave)

s = 0
while True:
    c.drop_sand()
    s += 1
    if c.check_finish():
        print("FINISHED")
        c.print_cave()
        print(s)
        break

