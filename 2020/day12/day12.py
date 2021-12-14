with open('day12input.txt') as file:
    actions = [action.replace('\n','') for action in file.readlines()]
    actions = [(action[0], int(action[1:])) for action in actions]

print(actions)

class Ship:
    def __init__(self):
        self.NS = 0
        self.EW = 0
        self.facing = 'E'

    def rotate(self, degrees):
        compass = {0: 'N', 90: 'E', 180: 'S', 270: 'W'}
        facing_to_degrees = {value : key for (key, value) in compass.items()}
        current = facing_to_degrees[self.facing]
        new_degrees = (current + degrees) % 360
        self.facing = compass[new_degrees]

    def forward(self, distance):
        return self.facing, distance

    def north(self, distance):
        self.NS += distance

    def east(self, distance):
        self.EW += distance

    def south(self, distance):
        self.NS -= distance

    def west(self, distance):
        self.EW -= distance

    def take_action(self, action: str, value: int):
        if action == 'F':
            action, value = self.forward(value)
        if action == 'N':
            self.north(value)
        if action == 'E':
            self.east(value)
        if action == 'S':
            self.south(value)
        if action == 'W':
            self.west(value)
        if action == 'R':
            self.rotate(value)
        if action == 'L':
            self.rotate(-value)

    def report(self):
        print(f'NS: {self.NS}, EW: {self.EW}, Facing: {self.facing}')
        print(abs(self.NS) + abs(self.EW))


# ship = Ship()
# for action, value in actions:
#     print(action, value)
#     ship.take_action(action, value)
#     ship.report()

class Waypoint:
    def __init__(self):
        self.wpNS = 1
        self.wpEW = 10
        self.shipNS = 0
        self.shipEW = 0

    def right(self, degrees):
        degrees = degrees % 360
        while degrees > 0:
            self.wpNS, self.wpEW = (-self.wpEW, self.wpNS)
            degrees -= 90

    def left(self, degrees):
        degrees = degrees % 360
        while degrees > 0:
            self.wpNS, self.wpEW = (self.wpEW, -self.wpNS)
            degrees -= 90

    def forward(self, distance):
        self.shipNS += self.wpNS * distance
        self.shipEW += self.wpEW * distance

    def north(self, distance):
        self.wpNS += distance

    def east(self, distance):
        self.wpEW += distance

    def south(self, distance):
        self.wpNS -= distance

    def west(self, distance):
        self.wpEW -= distance

    def take_action(self, action: str, value: int):
        if action == 'F':
            self.forward(value)
        if action == 'N':
            self.north(value)
        if action == 'E':
            self.east(value)
        if action == 'S':
            self.south(value)
        if action == 'W':
            self.west(value)
        if action == 'R':
            self.right(value)
        if action == 'L':
            self.left(value)

    def report(self):
        print(f'Ship NS: {self.shipNS}, EW: {self.shipEW}')
        print(f'Waypoint NS: {self.wpNS}, EW: {self.wpEW}')
        print(abs(self.shipNS) + abs(self.shipEW))


ship = Waypoint()
for action, value in actions:
    print(action, value)
    ship.take_action(action, value)
    ship.report()