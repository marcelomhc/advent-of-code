import sys
from itertools import permutations
from collections import deque

freqs = dict()

class Amplificator(object):
    def __init__(self, program, phase, value):
        self.program = program
        self.phase = phase
        self.phased = False
        self.done = False
        self.pos = 0
        self.output = 0
        self.input = value

    def set_input(self, value):
        self.input = value

    def get_output(self):
        return self.output

    def get_phase(self):
        self.phased = True
        return self.phase
    
    def get_phased(self):
        return self.phased

    def get_done(self):
        return self.done

    def get_var(self, var, mode):
        if (mode == 0):
            return self.program[var]
        return var

    def amplify(self):

        while(self.program[self.pos] != 99):
            command = self.program[self.pos]
            instruction = command % 100
            command = command // 100
            mode1 = command % 10
            command = command // 10
            mode2 = command % 10

            n_instructions = 0
            if(instruction == 1):
                var1 = self.get_var(self.program[self.pos+1], mode1)
                var2 = self.get_var(self.program[self.pos+2], mode2)
                result = self.program[self.pos+3]
                self.program[result] = var1 + var2
                n_instructions = 4
            elif(instruction == 2):
                var1 = self.get_var(self.program[self.pos+1], mode1)
                var2 = self.get_var(self.program[self.pos+2], mode2)
                result = self.program[self.pos+3]
                self.program[result] = var1 * var2
                n_instructions = 4
            elif(instruction == 3):
                #input
                if(self.phased):
                    data = self.input
                else:
                    data = self.get_phase()
                self.program[self.program[self.pos+1]] = data
                n_instructions = 2
            elif(instruction == 4):
                var1 = self.get_var(self.program[self.pos+1], mode1)
                n_instructions = 2
                self.output = var1
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
                result = self.program[self.pos+3]
                if(var1 < var2):
                    self.program[result] = 1
                else:
                    self.program[result] = 0
                n_instructions = 4
            elif(instruction == 8):
                var1 = self.get_var(self.program[self.pos+1], mode1)
                var2 = self.get_var(self.program[self.pos+2], mode2)
                result = self.program[self.pos+3]
                if(var1 == var2):
                    self.program[result] = 1
                else:
                    self.program[result] = 0
                n_instructions = 4

            self.pos += n_instructions
        self.done = True

def parse_program(filepath):
    with open(filepath, "r") as f:
        program = list(map(int, f.readline().split(',')))
    return program

def int_computer(program):
    #Part 1
    perm = permutations([0, 1, 2, 3, 4]) 

    thrust = 0
    for i in list(perm): 
        amp = 0
        for phase in i:
            amplifier = Amplificator(list(program), phase, amp)
            amplifier.amplify()
            amp = amplifier.get_output()
        thrust = max(thrust, amp)
    print(thrust)

    #Part 2
    perm = permutations([5, 6, 7, 8, 9]) 

    thrust = 0
    for i in list(perm): 
        loop = deque()
        for phase in i:
            amplifier = Amplificator(list(program), phase, 0)
            loop.append(amplifier)
        while(not loop[0].get_done()):
            amplifier = loop[0]
            amplifier.set_input(loop[4].get_output())
            amplifier.amplify()
            loop.rotate(-1)

        thrust = max(thrust, loop[4].get_output())
    print(thrust)

    
if __name__ == "__main__":
    data = parse_program("input/day7.data")
    int_computer(data)