with open("input.txt") as file:
    raw = file.readlines()
    raw_pairs = map(lambda x: x.strip().split(","), raw)
    raw_sections = map(lambda x: [x[0].split("-"), x[1].split("-")], raw_pairs)
    sections = list(map(lambda x: (int(x[0][0]), int(x[0][1]), int(x[1][0]), int(x[1][1])), raw_sections))

def contained(start1, end1, start2, end2):
    if start1 <= start2 and end1 >= end2:
        return 1
    elif start1 >= start2 and end1 <= end2:
        return 1
    else:
        return 0

print(sum(contained(start1, end1, start2, end2) for start1, end1, start2, end2 in sections))

# Part 2

def overlap(start1, end1, start2, end2):
    section1 = set(range(start1, end1+1))
    section2 = set(range(start2, end2+1))
    overlap = section1.intersection(section2)
    return 1 if overlap else 0

print(sum(overlap(start1, end1, start2, end2) for start1, end1, start2, end2 in sections))

