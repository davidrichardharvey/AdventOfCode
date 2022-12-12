from aoc_func import read_input_text

bags = read_input_text("input.txt")


def split_bag(bag):
    split_at = len(bag)//2
    return bag[:split_at], bag[split_at:]


def repeated_letter(bags):
    return list(set(bags[0]).intersection(set(bags[1])))[0]


def letter_to_priority(letter):
    return ord(letter) - 38 if letter.isupper() else ord(letter) - 96


priorities = map(lambda x: letter_to_priority(repeated_letter(x)), map(split_bag, bags))
print(sum(priorities))

# Part 2

badges = []

i = 0
while i < len(bags):
    badges.append(list(set(bags[i]).intersection(set(bags[i+1]).intersection(set(bags[i+2]))))[0])
    i += 3

print(badges)

print(sum(map(letter_to_priority, badges)))