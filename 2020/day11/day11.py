import copy
from pprint import pprint

with open('day11input.txt') as file:
    lines = file.readlines()
    lines = list(line.replace('\n','') for line in lines)
    grid = [list(line) for line in lines]

# grid = [['L','L'],['L','L']]

# def check_adjacent_seats(seat_grid: list, x: int, y: int) -> int:
#     occupied = 0
#     to_check = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
#     for check in to_check:
#         ay = y + check[0]
#         ax = x + check[1]
#         try:
#             if seat_grid[ay][ax] == '#' and ay != -1 and ax != -1:
#                 occupied += 1
#         except IndexError:
#             continue
#     return occupied

def find_new_seating(seat_grid: list) -> list:
    new_grid = copy.deepcopy(grid)
    for iy, line in enumerate(seat_grid):
        for ix, seat in enumerate(line):
            adjacency = check_adjacent_seats(seat_grid, ix, iy)
            # print(ix, iy, seat, adjacency)
            if seat == 'L' and adjacency == 0:
                new_grid[iy][ix] = '#'
            elif seat == '#' and adjacency >= 5:
                new_grid[iy][ix] = 'L'
    return new_grid

def print_grid(seat_grid):
    print('\n')
    for line in seat_grid:
        print(''.join(line))
    print('\n')

def count_occupied_seats(seat_grid):
    occupied_seats = 0
    for line in seat_grid:
        for seat in line:
            if seat == '#':
                occupied_seats += 1
    return occupied_seats

# x = 0
# while True:
#     print(f'=== ROUND {x} ===')
#     # print_grid(grid)
#     new_grid = find_new_seating(grid)
#     if new_grid == grid:
#         print(count_occupied_seats(grid))
#         break
#     else:
#         grid = new_grid
#         x += 1

# Part Two

def check_seat_direction(seat_grid: list, ax: int, ay: int, dx, dy) -> int:
    max_y = len(seat_grid)
    max_x = len(seat_grid[0])
    while True:
        ax += dx
        ay += dy
        if ax in (-1, max_x) or ay in (-1, max_y):
            return False
        elif seat_grid[ay][ax] == 'L':
            return False
        elif seat_grid[ay][ax] == '#':
            return True

def check_adjacent_seats(seat_grid: list, x: int, y: int) -> int:
    to_check = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    adjacent = 0
    for check in to_check:
        if check_seat_direction(seat_grid, x, y, check[0], check[1]):
            adjacent += 1
    return adjacent

x = 0
while True:
    print(f'=== ROUND {x} ===')
    print_grid(grid)
    new_grid = find_new_seating(grid)
    if new_grid == grid:
        print(count_occupied_seats(grid))
        break
    else:
        grid = new_grid
        x += 1