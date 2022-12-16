from aoc_func import read_input_text

program = read_input_text("input.txt")

class ClockCircuit:
    def __init__(self):
        self.strengths = []
        self.cycle = 1
        self.X = 1
    # -20 % 40

    def tick(self):
        if (self.cycle - 20) % 40 == 0:
            self.strengths.append(self.X * self.cycle)
        self.cycle += 1


    def read_line(self, line):
        if line == "noop":
            self.tick()
        else:
            V = int(line.split(" ")[-1])
            self.tick()
            self.tick()
            self.X += V


    def read_program(self, program):
        for line in program:
            self.read_line(line)


cc = ClockCircuit()
cc.read_program(program)
print(cc.strengths)
print(sum(cc.strengths))

# Part 2

class CRT(ClockCircuit):
    def __init__(self):
        super().__init__()
        self.crt_line = ""

    def tick(self):
        position = (self.cycle - 1) % 40

        if position in (self.X - 1, self.X, self.X + 1):
            self.crt_line += "# "
        else:
            self.crt_line += "  "
        self.cycle += 1

        if position == 39:
            print(self.crt_line)
            self.crt_line = ""

crt = CRT()
crt.read_program(program)
