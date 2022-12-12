from aoc_func import read_input_text

input = read_input_text("input.txt")

# shape_score = {
#     'X': 1,
#     'Y': 2,
#     'Z': 3
# }
#
# result_score = {
#     'A X': 3,
#     'A Y': 6,
#     'A Z': 0,
#     'B X': 0,
#     'B Y': 3,
#     'B Z': 6,
#     'C X': 6,
#     'C Y': 0,
#     'C Z': 3,
# }

shape_score = {
    'X': 0,
    'Y': 3,
    'Z': 6
}

# Rock = 1, Paper = 2, Scissors = 3
result_score = {
    'A X': 3, # Rock        # Lose
    'A Y': 1,               # Draw
    'A Z': 2,               # Win
    'B X': 1, # Paper
    'B Y': 2,
    'B Z': 3,
    'C X': 2, # Scissors
    'C Y': 3,
    'C Z': 1,
}

scores = list(map(lambda x: shape_score[x[-1]] + result_score[x], input))

print(scores)
print(sum(scores))

