import re

with open("input.txt") as raw_file:
    call_order = raw_file.readline().strip().split(',')
    raw_file.readline()
    boards = []
    while True:
        new_board = []
        for i in range(5):
            new_board.append(re.split(' +', raw_file.readline().strip()))
        raw_file.readline()
        if new_board[0][0]:
            boards.append(new_board)
        else:
            break


def check_board_win(bingo_board):
    win = ['X', 'X', 'X', 'X', 'X']
    return win in bingo_board or win in list(map(list, zip(*bingo_board)))


def mark_board(bingo_board, number):
    for line in bingo_board:
        for j, n in enumerate(line):
            if n == number:
                line[j] = 'X'


def score_board(bingo_board):
    total = 0
    for line in bingo_board:
        total += sum(map(lambda x: int(x), filter(lambda x: x.isdigit(), line)))
    return total


for num in call_order:
    removals = []
    for position, board in enumerate(boards):
        mark_board(board, num)
        if check_board_win(board):
            if len(boards) > 1:
                removals.append(position)
            else:
                print(boards)
                print(score_board(board), num, score_board(board) * int(num))
                boards.remove(board)
    removals.sort(reverse=True)
    for p in removals:
        boards.pop(p)


