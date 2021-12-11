from pprint import pprint
import re
from statistics import median

with open("input.txt") as aoc_input:
    lines = [x.strip() for x in aoc_input.readlines()]

example = lines[0]
print(example)

def cleanse_brackets(line):
    if '<>' in line:
        line = line.replace('<>', '')
        return cleanse_brackets(line)
    elif '[]' in line:
        line = line.replace('[]', '')
        return cleanse_brackets(line)
    elif '{}' in line:
        line = line.replace('{}', '')
        return cleanse_brackets(line)
    elif '()' in line:
        line = line.replace('()', '')
        return cleanse_brackets(line)
    else:
        match = re.search('[)}>\]]', line)
        # if match:
        #     return match.group(0)
        if not match:
            return line[::-1].replace('[', ']')\
                .replace('(', ')')\
                .replace('<', '>')\
                .replace('{', '}')


scores = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}

c = (cleanse_brackets(line) for line in lines)

def score_bracket_string(bracket_string):
    total = 0
    bs = {')': 1, ']': 2, '}': 3, '>': 4}
    for bracket in bracket_string:
        total *= 5
        total += bs.get(bracket)
    return total

t = (score_bracket_string(brackets) for brackets in c if brackets)
print(median(t))
