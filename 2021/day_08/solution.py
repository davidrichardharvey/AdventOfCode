from collections import Counter

with open("input.txt") as aoc_input:
    signals = [x.strip().split(" | ") for x in aoc_input.readlines()]

# easy_digits_lengths = [2, 4, 3, 7]
# total = 0
# for line in signals:
#     output = line[1].split(" ")
#     output_len = (len(x) for x in output)
#     easy_digits = (1 for x in output_len if x in easy_digits_lengths)
#     total += sum(easy_digits)
#
# print(total)

total_sum = 0
for signal in signals:
    wire_options = {
        'A': ['a', 'b', 'c', 'd', 'e', 'f', 'g'],
        'B': ['a', 'b', 'c', 'd', 'e', 'f', 'g'],
        'C': ['a', 'b', 'c', 'd', 'e', 'f', 'g'],
        'D': ['a', 'b', 'c', 'd', 'e', 'f', 'g'],
        'E': ['a', 'b', 'c', 'd', 'e', 'f', 'g'],
        'F': ['a', 'b', 'c', 'd', 'e', 'f', 'g'],
        'G': ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    }
    digits = {
        0: 'ABCEFG',
        1: 'CF',
        2: 'ACDEG',
        3: 'ACDFG',
        4: 'BCDF',
        5: 'ABDFG',
        6: 'ABDEFG',
        7: 'ACF',
        8: 'ABCDEFG',
        9: 'ABCDFG'
    }
    signal_line = signal[0].split(' ')
    print(signal_line)
    signal_line.sort(key=len)
    print(signal_line)
    for c in 'CF':
        wire_options[c] = [l for l in wire_options[c] if l.lower() in signal_line[0]]
    for c in 'ACF':
        wire_options[c] = [l for l in wire_options[c] if l.lower() in signal_line[1]]
    for c in 'BCDF':
        wire_options[c] = [l for l in wire_options[c] if l.lower() in signal_line[2]]
    # 3 must contain C and F, which overlap with 1
    for digit in (x for x in signal_line if len(x) == 5):
        if wire_options['C'][0] in digit and wire_options['C'][1] in digit:
            for c in 'ADG':
                wire_options[c] = [l for l in wire_options[c] if l.lower() in digit and l not in wire_options['C']]
    # We now know A and D
    final = {'A': wire_options['A'][0], 'D': wire_options['D'][0]}
    letter_counts = Counter(c for c in ''.join(signal_line).replace(' ', ''))
    print(letter_counts)
    # There should be 6 x B
    # There should be 4 x E
    # There should be 9 x F
    for key, value in letter_counts.items():
        if value == 6:
            final['B'] = key
        elif value == 4:
            final['E'] = key
        elif value == 9:
            final['F'] = key
        elif value == 8 and key != final['A']:
            final['C'] = key
        elif value == 7 and key != final['D']:
            final['G'] = key
    # A and C have 8 (but we know A)
    # D and G have 7 (but we know D)
    print(final)

    output_code = signal[1].split(' ')
    code_sets = [set(code) for code in output_code]
    print(code_sets)

    digit_codes = {}
    for digit, letters in digits.items():
        digit_codes[digit] = set([final[letter] for letter in letters])
    print(digit_codes)

    num_string = ''
    for code in code_sets:
        for number, letter_set in digit_codes.items():
            if letter_set == code:
                num_string += str(number)
    total_sum += int(num_string)

print(total_sum)

# That was probably the most inefficient possible solve!!
