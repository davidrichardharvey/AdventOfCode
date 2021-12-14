from tqdm import trange

def return_nth(starting, n):
    current = None
    memory = {}
    for i, s in enumerate(starting, start=1):
        if s not in memory.keys():
            memory[s] = [i]
        else:
            memory[s].append(i)
        current = s
    # print(memory)
    for x in trange(len(starting) + 1, n + 1):
        # print(current)
        if len(memory[current]) == 1:
            current = 0
        else:
            current = x - memory[current][-2] - 1
        if current not in memory.keys():
            memory[current] = [x]
        else:
            memory[current].append(x)
        # print(memory)
    return current

print(return_nth([8,13,1,0,18,9], 30000000))