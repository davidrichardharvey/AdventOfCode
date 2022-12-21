from functools import cmp_to_key

def compare_packets(left_list: list, right_list: list):

    if right_list == []:
        return 1
    elif left_list == []:
        return -1

    i = 0
    for left, right in zip(left_list, right_list):
        if isinstance(left, int) and isinstance(right, int):
            if left == right:
                i += 1
                if i == len(left_list):
                    return -1
                elif i == len(right_list):
                    return 1
                continue
            return -1 if left < right else 1
        else:
            left = [left] if isinstance(left, int) else left
            right = [right] if isinstance(right, int) else right
            if left == [] and right == []:
                continue
            return compare_packets(left, right)
    return -1


print(compare_packets([[6]], [[6, 4]]))

total = []
i = 1
results = []
all_packets = []
with open("input.txt") as file:
    while True:
        l1 = eval(file.readline().strip())
        l2 = eval(file.readline().strip())
        all_packets.append(l1)
        all_packets.append(l2)
        ans = compare_packets(l1, l2)
        assert ans is not None
        results.append(ans)
        if ans == -1:
            total.append(i)
        i += 1
        if not file.readline():
            break

print(total)
print(sum(total))
decoder = 1
all_packets.append([[2]])
all_packets.append([[6]])
for i, packet in enumerate(sorted(all_packets, key=cmp_to_key(compare_packets))):
    print(packet)
    if packet == [[2]] or packet == [[6]]:
        decoder *= i + 1

print(decoder)
