from aoc_func import read_input_ints

with open("input.txt") as input:
    elves = []
    elf_calories = []
    current_elf = []
    for line in input.readlines():
        if line.strip():
            input_int = int(line.strip())
            current_elf.append(input_int)
        else:
            elves.append(current_elf)
            elf_calories.append(sum(current_elf))
            current_elf = []

print(elves)
print(elf_calories)
print(max(elf_calories))

top3 = sorted(elf_calories)[-3:]
print(top3)
print(sum(top3))
