with open('day9input.txt') as file:
    xmas = file.readlines()
    xmas = list(map(lambda x: int(x.replace('\n','')), xmas))

pre = 25
key_num = None
for x in range(25, len(xmas)):
    window = xmas[x - 25: x]
    num = xmas[x]
    match = False
    for a in range(pre):
        for b in range(pre):
            if a != b and window[a] + window[b] == num:
                match = True
    if not match:
        key_num = num
        break

print(key_num)

for l in range(2, len(xmas)): # Possible lengths of window
    for i in range((len(xmas) + 1) - l):# Possible start indices of window
        potential_window = xmas[i:i+l+1]
        if sum(potential_window) == key_num:
            print(key_num, potential_window)
            print(min(potential_window), max(potential_window))
            print(min(potential_window) + max(potential_window))
            key_window = potential_window
            break




