from aoc_func import read_input_text

moves = read_input_text("input.txt")

class Tail:
    def __init__(self, tail=None):
        self.x = 0
        self.y = 0
        self.visited = {'0 0': 1}
        self.tail = tail

    def should_move(self, x_diff, y_diff):
        if abs(x_diff) == 1 and abs(y_diff) == 1:
            return False
        if abs(x_diff) + abs(y_diff) > 1:
            return True

    def move_to_head(self, head_x, head_y):
        x_diff = head_x - self.x
        y_diff = head_y - self.y
        # Only move if not touching
        if self.should_move(x_diff, y_diff):
            # Hacky solution to get the vector
            self.x += round(x_diff / 1.9)
            self.y += round(y_diff / 1.9)

        self.visited[f"{self.x} {self.y}"] = 1
        print(self.x, self.y)
        if self.tail:
            self.tail.move_to_head(self.x, self.y)


class Head:
    def __init__(self, tail):
        self.x = 0
        self.y = 0
        self.tail = tail

    def move(self, direction: str, amount: int):

        for n in range(amount):
            print("STEP!")
            if direction == 'U':
                self.y += 1
            elif direction == 'R':
                self.x += 1
            elif direction == 'D':
                self.y -= 1
            elif direction == 'L':
                self.x -= 1
            print(self.x, self.y, "<-- Head")
            self.tail.move_to_head(self.x, self.y)

# Part 1
#
# head = Head(Tail())
# for move in moves:
#     direction, text_amount = move.split(" ")
#     head.move(direction, int(text_amount))
#
# print(sum(head.tail.visited.values()))

# Part 2

tail = Tail()
k8 = Tail(tail)
k7 = Tail(k8)
k6 = Tail(k7)
k5 = Tail(k6)
k4 = Tail(k5)
k3 = Tail(k4)
k2 = Tail(k3)
k1 = Tail(k2)
head = Head(k1)

for move in moves:
    direction, text_amount = move.split(" ")
    head.move(direction, int(text_amount))
    print("---------")

print(sum(tail.visited.values()))
