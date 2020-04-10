import sys
from collections import defaultdict, deque

freqs = dict()

class IntComputer(object):
    def __init__(self, program, base = 0, value = 0):
        self.program = program
        self.pos = 0
        self.input = value
        self.base = base
        self.done = False

    def is_done(self):
        return self.done

    def set_input(self, value):
        self.input = value

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
                self.set_result(self.program[self.pos+1], mode1, self.input)
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

def parse_program(filepath):
    with open(filepath, "r") as f:
        program = list(map(int, f.readline().split(',')))
    return program

def print_board(panels):
    keys = panels.keys()
    maxX = max(keys, key=lambda l: l[0])[0]
    maxY = max(keys, key=lambda l: l[1])[1]

    for j in range (maxY+1):
        for i in range ( maxX+1):
            if(panels[(i,j)] == 0):
                print('.', end='')
            elif(panels[(i,j)] == 1):
                print('|', end='')
            elif(panels[(i,j)] == 2):
                print('#', end='')
            elif(panels[(i,j)] == 3):
                print('-', end='')
            elif(panels[(i,j)] == 4):
                print('o', end='')
            else:
                print('#', end='')
        print('')

def check_game(program):
    computer = IntComputer(program)
    board = dict()
    
    while(not computer.is_done()):
        x = computer.run()
        y = computer.run()
        v = computer.run()
        board[(x,y)] = v

    board.pop((None,None))
    print(list(board.values()).count(2))
    #print_board(board)

def play_game(program):
    program[0] = 2
    computer = IntComputer(program)
    board = dict()
    ball = paddle = 0

    computer.set_input(-1)
    while(not computer.is_done()):
        x = computer.run()
        y = computer.run()
        v = computer.run()
        board[(x,y)] = v
        
        ball = x if v == 4 else ball
        paddle = x if v == 3 else paddle
        computer.set_input((ball > paddle) - (paddle > ball))

    board.pop((None,None))
    print(board[(-1,0)])

    
if __name__ == "__main__":
    data = parse_program("input/day13.data")
    d = defaultdict(lambda: 0)
    for i in range(len(data)):
        d[i] = data[i]
    
    check_game(d)
    play_game(d)
