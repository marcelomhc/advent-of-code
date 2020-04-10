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
        self.repeat = 0

    def decode(self, filepath):
        with open(filepath, "r") as f:
            data = list(map(int, f.readline().split(',')))

        d = defaultdict(lambda: 0)
        for i in range(len(data)):
            d[i] = data[i]
        return d

    def add_package(self, value):
        self.input += value

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
                if(len(self.input) > 0):
                    value = self.input[0]
                    self.input = self.input[1:]
                else:
                    value = -1
                    self.repeat += 1
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
            if(self.repeat == 5):
                self.repeat = 0
                return
        self.done = True

def run_network():
    network = [IntComputer("input/day23.data", value=[address]) for address in range(50)]

    dest = 0
    while(True):
        for computer in network:
            dest = computer.run()
            x = computer.run()
            y = computer.run()
            if(dest == 255):
                print(y)
                return
            if(dest):
                network[dest].add_package([x,y])

def run_nat_network():
    network = [IntComputer("input/day23.data", value=[address]) for address in range(50)]

    dest = 0
    nats = set()
    while(True):
        idle = 0
        for computer in network:
            dest = computer.run()
            x = computer.run()
            y = computer.run()
            if(dest == 255):
                nat = (x,y)
            elif(dest):
                network[dest].add_package([x,y])
            else:
                idle += 1
        if(idle == 50):
            if nat in nats:
                print(nat[1])
                return
            nats.add(nat)
            network[0].add_package(list(nat))

if __name__ == "__main__":
    run_network()
    run_nat_network()