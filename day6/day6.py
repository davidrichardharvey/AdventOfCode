def get_file_contents(filename):
    with open(filename) as file:
        contents = file.read()
    inputs = contents.split('\n\n')
    inputs = map(lambda x: list(map(lambda x: set(x), x.split('\n'))), inputs)
    return list(inputs)

answers = get_file_contents('day6.txt')
counter = 0
for x in answers:
    a = set.intersection(*x)
    print(a)
    counter += len(a)

print(counter)