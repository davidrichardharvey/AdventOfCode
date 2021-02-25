demo = 'FFFBBBFRRR'


def row_parser(seat_string):
    row_min, row_max = (0, 127)
    for x in seat_string[:7]:
        if x == 'F':
            row_max = int(row_min + ((row_max - row_min + 1) / 2) - 1)
        elif x == 'B':
            row_min = int(row_min + ((row_max - row_min + 1) / 2))
    if row_min == row_max:
        return row_min
    else:
        print("IT'S ALL GONE TERRIBLY WRONG")


def column_parser(seat_string):
    col_min, col_max = (0, 7)
    for x in seat_string[-3:]:
        if x == 'L':
            col_max = int(col_min + ((col_max - col_min + 1) / 2) - 1)
        elif x == 'R':
            col_min = int(col_min + ((col_max - col_min + 1) / 2))
    if col_min == col_max:
        return col_min
    else:
        print("IT'S ALL GONE TERRIBLY WRONG")


with open('day5input.txt') as file:
    seat_codes = file.read().split('\n')

seat_ids = map(lambda x: (row_parser(x) * 8) + column_parser(x), seat_codes)
seat_ids = list(seat_ids)
seat_ids = sorted(seat_ids)
print(seat_ids)

last_seat = 98
for x in seat_ids:
    if x - 1 != last_seat:
        print(last_seat, x)
    last_seat = x