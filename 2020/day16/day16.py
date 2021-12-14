with open("day16input.txt") as file:
    lines = [s.replace('\n','') for s in file.readlines()]

lines = list(filter(lambda s: s != '', lines))
rules = filter(lambda x: ": " in x, lines)
rules = map(lambda x: x.split(": ")[1], rules)
rules = map(lambda x: x.split(" or "), rules)
rules = map(lambda x: [(int(a), int(b)) for a, b in (y.split("-") for y in x)], rules)


valid_numbers = []
for rule in rules:
    print(rule)
    for section in rule:
        start, end = section
        for i in range(start, end + 1):
            valid_numbers.append(i)
valid_set = set(valid_numbers)
print(valid_set)

error_rate = 0
for ticket in lines[lines.index("nearby tickets:") + 1:]:
    numbers = [int(x) for x in ticket.split(",")]
    for n in numbers:
        if n not in valid_set:
            error_rate += n
print(error_rate)