import copy

with open('day8input.txt') as file:
    instructions = file.readlines()
    instructions = list(map(lambda x: x.replace('\n','').split(), instructions))


def try_sequence(inst):
    visited = set()
    position = 0
    accumulator = 0
    while True:
        # print(inst[position])
        if position >= len(inst):
            return accumulator
        elif position in visited:
            return None
        else:
            visited.add(position)
            command, value = inst[position]
            if command == 'acc':
                accumulator += int(value)
                position += 1
            elif command == 'nop':
                position += 1
            elif command == 'jmp':
                position += int(value)

for i in range(len(instructions)):
    new_inst = copy.deepcopy(instructions)
    if instructions[i][0] == 'jmp':
        new_inst[i][0] = 'nop'
        x = try_sequence(new_inst)
        if x:
            print(i, new_inst[i], x)
    elif instructions[i][0] == 'nop':
        new_inst[i][0] = 'jmp'
        x = try_sequence(new_inst)
        if x:
            print(i, new_inst[i], x)
