import math

class Monkey:
    def __init__(self, items, operation, div, monkey_true, monkey_false):
        self.items = items
        self.operation = operation
        self.div = div
        self.monkey_true = monkey_true
        self.monkey_false = monkey_false
        self.inspect_count = 0

    def inspect(self):
        self.inspect_count += 1
        old = self.items.pop(0)
        new = eval(self.operation)
        return new # // 3

    def throw(self, worry):
        if worry % self.div == 0:
            return self.monkey_true
        else:
            return self.monkey_false

    def catch(self, worry):
        self.items.append(worry)


monkeys = []

with open("input.txt") as file:
    while True:
        if file.readline():
            items = [int(x) for x in file.readline().strip().replace("Starting items: ", "").split(", ")]
            operation = file.readline().strip().replace("Operation: new = ", "")
            div = int(file.readline().strip().split(" ")[-1])
            m1 = int(file.readline().strip().split(" ")[-1])
            m2 = int(file.readline().strip().split(" ")[-1])
            file.readline()
            monkeys.append(Monkey(
                items=items,
                operation=operation,
                div=div,
                monkey_true=m1,
                monkey_false=m2
            ))
        else:
            break

mod = 1
for monkey in monkeys:
    mod *= monkey.div

for round in range(10000):
    for monkey in monkeys:
        for n in range(len(monkey.items)):
            worry = monkey.inspect() % mod
            target = monkey.throw(worry)
            monkeys[target].catch(worry)

for i, monkey in enumerate(monkeys):
    print(f"Monkey {i}: {monkey.inspect_count}")

print(f"Monkey Business = {math.prod(sorted([monkey.inspect_count for monkey in monkeys])[-2:])}")