import sys
from collections import defaultdict, deque

freqs = dict()

class IntComputer(object):
    def __init__(self, program, base, panels):
        self.program = program
        self.pos = 0
        self.output = 0
        self.base = base
        self.move_out = False
        self.panels = panels
        self.position = (0,0)
        self.direction = deque([(0,1), (-1,0), (0,-1), (1,0)])

    def get_output(self):
        return self.output

    def get_var(self, var, mode):
        if (mode == 0):
            return self.program[var]
        elif(mode == 2):
            return self.program[var+self.base]
        return var

    def set_result(self, parameter, mode, value):
        if(mode == 2):
            var = self.base + parameter
        else:
            var = parameter
        self.program[var] = value

    def move(self, direction):
        if(direction == 0):
            self.direction.rotate(-1)
        else:
            self.direction.rotate(1)

        self.position = tuple(map(sum, zip(self.position, self.direction[0])))


    def paint(self):

        while(self.program[self.pos] != 99):
            command = self.program[self.pos]
            instruction = command % 100
            command = command // 100
            mode1 = command % 10
            command = command // 10
            mode2 = command % 10
            command = command // 10
            mode3 = command % 10

            n_instructions = 0
            if(instruction == 1):
                var1 = self.get_var(self.program[self.pos+1], mode1)
                var2 = self.get_var(self.program[self.pos+2], mode2)
                self.set_result(self.program[self.pos+3], mode3, var1 + var2)
                n_instructions = 4
            elif(instruction == 2):
                var1 = self.get_var(self.program[self.pos+1], mode1)
                var2 = self.get_var(self.program[self.pos+2], mode2)
                self.set_result(self.program[self.pos+3], mode3, var1 * var2)
                n_instructions = 4
            elif(instruction == 3):
                #input
                self.set_result(self.program[self.pos+1], mode1, self.panels[self.position])
                n_instructions = 2
            elif(instruction == 4):
                var1 = self.get_var(self.program[self.pos+1], mode1)
                n_instructions = 2
                if(self.move_out):
                    self.panels[self.position] = self.output
                    self.move(var1)
                else:
                    self.output = var1
                self.move_out = not self.move_out
            elif(instruction == 5):
                var1 = self.get_var(self.program[self.pos+1], mode1)
                var2 = self.get_var(self.program[self.pos+2], mode2)
                if (var1 != 0):
                    self.pos = var2
                else:
                    n_instructions = 3
            elif(instruction == 6):
                var1 = self.get_var(self.program[self.pos+1], mode1)
                var2 = self.get_var(self.program[self.pos+2], mode2)
                if (var1 == 0):
                    self.pos = var2
                else:
                    n_instructions = 3
            elif(instruction == 7):
                var1 = self.get_var(self.program[self.pos+1], mode1)
                var2 = self.get_var(self.program[self.pos+2], mode2)
                if(var1 < var2):
                    result = 1
                else:
                    result = 0
                self.set_result(self.program[self.pos+3], mode3, result)
                n_instructions = 4
            elif(instruction == 8):
                var1 = self.get_var(self.program[self.pos+1], mode1)
                var2 = self.get_var(self.program[self.pos+2], mode2)
                if(var1 == var2):
                    result = 1
                else:
                    result = 0
                self.set_result(self.program[self.pos+3], mode3, result)
                n_instructions = 4
            elif(instruction == 9):
                var1 = self.get_var(self.program[self.pos+1], mode1)
                self.base += var1
                n_instructions = 2

            self.pos += n_instructions
        return self.panels

def parse_program(filepath):
    with open(filepath, "r") as f:
        program = list(map(int, f.readline().split(',')))
    return program

def print_panels(panels):
    keys = panels.keys()
    minX = min(keys, key=lambda l: l[0])[0]
    maxX = max(keys, key=lambda l: l[0])[0]
    minY = min(keys, key=lambda l: l[1])[1]
    maxY = max(keys, key=lambda l: l[1])[1]

    for j in range (maxY, minY-1, -1):
        for i in range (minX, maxX+1):
            if(panels[(i,j)] == 0):
                print('.', end='')
            else:
                print('#', end='')
        print('')

    print(minX, maxX, minY, maxY)

def count_panels(program, panels):
    computer = IntComputer(program, 0, panels)
    panels = computer.paint()

    print(len(panels.values()))

    print_panels(panels)

    
if __name__ == "__main__":
    data = parse_program("input/day11.data")
    panels = defaultdict(lambda: 0)
    panels[(0,0)] = 1 #part 2
    d = defaultdict(lambda: 0)
    for i in range(len(data)):
        d[i] = data[i]
    
    count_panels(d, panels)