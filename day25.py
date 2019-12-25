import random
from collections import defaultdict, deque

freqs = dict()

class IntComputer(object):
    def __init__(self, filepath, base = 0, value = []):
        self.program = self.decode(filepath)
        self.pos = 0
        self.input = value
        self.base = base
        self.done = False

    def decode(self, filepath):
        with open(filepath, "r") as f:
            data = list(map(int, f.readline().split(',')))

        d = defaultdict(lambda: 0)
        for i in range(len(data)):
            d[i] = data[i]
        return d

    def set_input(self, value):
        self.input = deque(value)

    def is_done(self):
        return self.done

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


    def run(self):

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
                if(len(self.input) == 0):
                    value = input()
                    for char in value:
                        self.input.append(ord(char))
                    self.input.append(10)
                self.set_result(self.program[self.pos+1], mode1, self.input[0])
                self.input = self.input[1:]
                n_instructions = 2
            elif(instruction == 4):
                var1 = self.get_var(self.program[self.pos+1], mode1)
                n_instructions = 2
                self.pos += n_instructions
                return var1
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
        self.done = True

def run():
    program = '''north
take sand
north
take space heater
east
take semiconductor
west
south
south
east
take ornament
south
take festive hat
east
take asterisk
south
east
take cake
west
west
take food ration
east
north
west
north
west
west
north
north
west
west
drop cake
drop asterisk
drop sand
drop food ration
west\n'''
    start(program)

def start(program):
    routine = []
    for char in program:
        routine.append(ord(char))
    computer = IntComputer("input/day25.data", value=routine)

    while(not computer.is_done()):
        out = computer.run()
        if(out):
            print(chr(out), end='')

if __name__ == "__main__":
    run()