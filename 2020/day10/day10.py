with open('day10input.txt') as file:
    lines = file.readlines()
    adapters = sorted(list(int(line.replace('\n', '')) for line in lines))

# print(adapters)
#
# one_jolts = 0
# three_jolts = 1
#
# for i in range(1, len(adapters)):
#     diff = adapters[i] - adapters[i-1]
#     print(adapters[i], adapters[i - 1], diff)
#     if diff == 1:
#         one_jolts += 1
#     elif diff == 3:
#         three_jolts += 1
#
# print(one_jolts, three_jolts, one_jolts * three_jolts)

# PART TWO
adapters.append(adapters[-1] + 3)     # Add the target adapter value to the end of the list
counter = {0: 1}                # Dict that will count how many ways to reach a jolts value (1 way to reach 0)
print(adapters)
for adapter in adapters:
    # The loop will iterate through the list of all adapters and will count the amount of ways to reach that
    # specific adapter jolts value. Counting will default to 0, if there is no way to reach that value.
    counter[adapter] = counter.get(adapter - 3, 0) + counter.get(adapter - 2, 0) + counter.get(adapter - 1, 0)

print("Part 2: The number of ways to reach jolts value of " + str(adapters[-1]) + " is " + str(counter[adapters[-1]]))
