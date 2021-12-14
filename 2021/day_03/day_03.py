from aoc_func import read_input_text
from statistics import multimode

diagnostic = read_input_text("input.txt")
print(diagnostic)


def find_most_common_bit(diagnostic_list, index):
    ones = 0
    for number in diagnostic_list:
        ones += int(number[index])
    zeroes = len(diagnostic_list) - ones
    return '1' if ones > zeroes else '0'


gamma = ''
for i in range(len(diagnostic[0])):
    gamma += find_most_common_bit(diagnostic, i)

epsilon = ''.join('1' if x == '0' else '0' for x in gamma)

# print(gamma, int(gamma, 2))
# print(epsilon, int(epsilon, 2))
#
# print(int(gamma, 2) * int(epsilon, 2))


def oxygen_generator_rating(diagnostic_list):
    d = diagnostic_list.copy()
    for index in range(len(d[0])):
        most_common = max(multimode(map(lambda x: x[index], d)))
        d = list(filter(lambda x: x[index] == most_common, d))
        if len(d) == 1:
            return d[0]


def co2_scrubber_rating(diagnostic_list):
    d = diagnostic_list.copy()
    for index in range(len(d[0])):
        least_common = '0' if max(multimode(map(lambda x: x[index], d))) == '1' else '1'
        d = list(filter(lambda x: x[index] == least_common, d))
        if len(d) == 1:
            return d[0]


o2 = oxygen_generator_rating(diagnostic)
co2 = co2_scrubber_rating(diagnostic)

print(int(o2, 2) * int(co2, 2))
