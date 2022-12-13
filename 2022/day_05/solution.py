crates = []
raw_instructions = []

with open("input.txt") as file:
    while True:
        line = file.readline().strip("\n").ljust(11)
        if not line.strip():
            break
        crates.append(line)
    while file:
        line = file.readline().strip("\n")
        if line:
            raw_instructions.append(line)
        else:
            break

num_of_stacks = int(crates[-1].strip().split(" ")[-1])
stacks = []
for n in range(num_of_stacks):
    stacks.append([])

i = len(crates) - 2

while i >= 0:
    line = crates[i]
    pos = 1
    for n in range(num_of_stacks):
        if line[pos] != ' ':
            stacks[n].append(line[pos])
        pos += 4
    i -= 1


def extract_instructions(line):
    num_string = line.replace("move ","").replace("from ","").replace("to ","")
    nums = num_string.split(" ")
    return [int(i) for i in nums]

instructions = map(extract_instructions, raw_instructions)

for instruction in instructions:
    buffer = [] # Part 2
    num = instruction[0]
    start = instruction[1] - 1
    end = instruction[2] - 1
    for i in range(num):
        # stacks[end].append(stacks[start].pop())  # Part 1
        buffer.append(stacks[start].pop()) # Part 2
    for j in range(len(buffer)):
        stacks[end].append(buffer.pop()) # Part 2

    # ^ This is bad and I don't like it, but it works

ans = ""
for stack in stacks:
    print(stack)
    ans += stack[-1]

print(ans)