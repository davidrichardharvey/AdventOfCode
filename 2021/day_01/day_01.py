filename = "input.txt"

with open(filename) as input_file:
    raw_input = list(map(lambda x: int(x.strip()), input_file.readlines()))


def depth_increase_count(depth_list):
    increase_count = 0
    prev_depth = None
    for depth in depth_list:
        if prev_depth:
            increase_count += int(depth > prev_depth)
        prev_depth = depth
    return increase_count


def depth_increase_window(depth_list):
    increase_count = 0
    prev_window = None
    for i in range(len(depth_list)):
        window = sum(depth_list[i:i+3])
        if prev_window:
            increase_count += int(window > prev_window)
        prev_window = window
    return increase_count


print(depth_increase_window(raw_input))
