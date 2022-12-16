from aoc_func import read_input_text

moves = read_input_text("input.txt")

class Tail:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.visited = {'0 0': 1}

    def move_to_head(self, head_x, head_y):
        x_diff = head_x - self.x
        y_diff = head_y - self.y
        # Only move if not touching
        if abs(x_diff) != abs(y_diff) and abs(x_diff) + abs(y_diff) > 1:
            # Hacky solution to get the vector
            self.x += round(x_diff / 1.9)
            self.y += round(y_diff / 1.9)

        self.visited[f"{self.x} {self.y}"] = 1


class Head:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.tail = Tail()

    def move(self, direction: str, amount: int):
        for n in range(amount):
            if direction == 'U':
                self.y += 1
            elif direction == 'R':
                self.x += 1
            elif direction == 'D':
                self.y -= 1
            elif direction == 'L':
                self.x -= 1
            self.tail.move_to_head(self.x, self.y)


head = Head()
for move in moves:
    direction, text_amount = move.split(" ")
    head.move(direction, int(text_amount))

print(sum(head.tail.visited.values()))

