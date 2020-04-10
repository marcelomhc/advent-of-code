import random
from collections import defaultdict, deque

freqs = dict()

class IntComputer(object):
    def __init__(self, filepath, base = 0, value = []):
        self.program = self.decode(filepath)
        self.runnable = self.program.copy()
        self.pos = 0
        self.input = deque(value)
        self.base = base
        self.done = False

    def reset(self):
        self.pos = 0
        self.program = self.runnable.copy()
        self.base = 0
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
                value = self.input[0]
                self.input.rotate(-1)
                self.set_result(self.program[self.pos+1], mode1, value)
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

def beam(computer, a, b, d):
    affected = 0
    for y in range(a, a+d):
        for x in range(b, b+d):
            computer.reset()
            computer.set_input([x, y])
            result = computer.run()
            if (result == 0):
                print('.', end='')
            else:
                print('#', end='')
            affected += result
        print('')

    print(affected)

def ship(computer):
    actual = [50, 30]
    movement = [1, 0]
    was_beam = False
    while(True):
        if (is_beam(computer, actual)):
            was_beam = True
            if(is_beam(computer, [a+b*99 for a,b in zip(actual, movement)])):
                if(is_beam(computer, [a+b*99 for a,b in zip(actual, reversed(movement))])):
                    [x,y] = actual
                    print(x*10000+y)
                    return
            else:
                movement = list(reversed(movement))
        elif(was_beam):
            movement = list(reversed(movement))
            was_beam = False
        
        actual = [sum(x) for x in zip(actual, movement)]

def is_beam(computer, position):
        computer.reset()
        computer.set_input(position)
        result = computer.run()
        return result == 1


if __name__ == "__main__":
    computer = IntComputer("input/day19.data", value=[])
    beam(computer, 0, 0, 50)
    ship(computer)