def read_input_ints(filename):
    with open(filename) as input_file:
        raw_input = list(map(lambda x: int(x.strip()), input_file.readlines()))
    return raw_input


def read_input_text(filename):
    with open(filename) as input_file:
        raw_input = list(map(lambda x: x.strip(), input_file.readlines()))
    return raw_input
