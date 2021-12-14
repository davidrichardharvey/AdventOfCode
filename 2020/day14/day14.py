def read_mem_input(line):
    line = line.strip('\n')
    line = line.split(' = ')
    if line[0] == 'mask':
        return (line[0], line[1])
    else:
        address = line[0].split('[')[1][:-1]
        return (address, line[1])

with open('day14input.txt') as file:
    lines = file.readlines()
    lines = map(read_mem_input, lines)

# print(list(lines))

def set_bit(value, bit_index):
    return value | (1 << bit_index)


def clear_bit(value, bit_index):
    return value & ~(1 << bit_index)

memory = {}
mask = None

for x in lines:
    if x[0] == "mask":
        mask = x[1]
        print(mask)
    else:
        bnum = bin(int(x[1]))
        if mask:
            for i in range(0,36):
                if mask[i] == '1':
                    bnum = bin(set_bit(eval(bnum), 35 - i))

                elif mask[i] == '0':
                    bnum = bin(clear_bit(eval(bnum), 35 - i))

        print(bnum)
        memory[int(x[0])] = int(bnum, 2)

print(memory)
print(sum(memory.values()))



