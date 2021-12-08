from itertools import chain
from tqdm import tqdm

with open("input.txt") as input_file:
    fish = (int(x) for x in input_file.readline().strip().split(','))

# for d in tqdm(range(256)):
#     new_fish = (8 for x in fish.copy() if x == 0)
#     old_fish = (x - 1 if x > 0 else 6 for x in fish)
#     fish = chain(old_fish, new_fish)
#
# print(sum(1 for x in fish))

fish_timer = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0}
for f in fish:
    fish_timer[f] += 1

for d in range(256):
    births = fish_timer[0]
    for i in range(0, 8):
        fish_timer[i] = fish_timer[i+1]
    fish_timer[8] = births
    fish_timer[6] += births


print(sum(fish_timer.values()))