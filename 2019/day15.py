import random
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

class Droid(object):
    def __init__(self):
        self.pos = (0, 0)
        self.board = dict()
        self.board[(0,0)] = 1
        self.found = False
        self.movement = -1
        self.oxygen = None

        self.direction = deque([1])

    def right_hand(self):
        pass

    def try_move(self):
        options = [1,2,3,4]

        for option in options.copy():
            tentative = self.locate(option)
            if (tentative not in self.board.keys()):
                self.movement = option
                return self.movement
            elif(self.board[tentative] == 0):
                options.remove(option)

        self.movement = random.choice(options)
        return self.movement

    def map(self, result):
        position = self.locate(self.movement)
        if(result == 0):
            self.board[position] = 0
            return

        self.pos = position
        self.board[position] = result

        if(result == 2):
            self.found = True
            self.oxygen = self.pos

    def locate(self, movement):
        x, y = self.pos

        if(movement == 1):
            y += 1
        elif(movement == 2):
            y -= 1
        elif(movement == 3):
            x += 1
        elif(movement == 4):
            x -= 1
        
        return (x,y)

def parse_program(filepath):
    with open(filepath, "r") as f:
        program = list(map(int, f.readline().split(',')))
    return program

def print_board(panels):
    keys = panels.keys()
    minX = min(keys, key=lambda l: l[0])[0]
    maxX = max(keys, key=lambda l: l[0])[0]
    minY = min(keys, key=lambda l: l[1])[1]
    maxY = max(keys, key=lambda l: l[1])[1]

    for j in range (maxY, minY-1, -1):
        for i in range (minX, maxX+1):
            if(j == i == 0):
                print('o', end='')
            elif(panels.get((i,j),-1) == 0):
                print('#', end='')
            elif(panels.get((i,j),-1) == 1):
                print('.', end='')
            elif(panels.get((i,j),-1) == 2):
                print('X', end='')
            else:
                print(' ', end='')
        print('')

def explore(program):
    computer = IntComputer(program)

    droid = Droid()

    while(len(droid.board) < 1660):
        computer.set_input(droid.try_move())
        droid.map(computer.run())
    
    print_board(droid.board)
    return droid

def neighboors(pos):
    x,y = pos
    return [(x+1,y), (x-1,y), (x,y+1), (x,y-1)]
    
def bfs(board, src, dst):
    queue = list()
    queue.append((0, src))
    visited = set()

    while(src != dst):
        steps, src = queue.pop(0)
        if (src not in visited):
            visited.add(src)
            for neighboor in neighboors(src):
                if(board[neighboor] in (1,2)):
                    queue.append((steps + 1, neighboor))
    print(steps)
    
def fill(board, src):
    queue = list()
    queue.append((0, src))
    visited = set()
    maxMin = 0

    while(list(board.values()).count(1) > 0):
        minutes, src = queue.pop(0)
        if (src not in visited):
            maxMin = max(minutes, maxMin)
            board[src] = 9
            visited.add(src)
            for neighboor in neighboors(src):
                if(board[neighboor] in (1,2)):
                    queue.append((minutes + 1, neighboor))
    
    print(maxMin)

if __name__ == "__main__":
    data = parse_program("input/day15.data")
    d = defaultdict(lambda: 0)
    for i in range(len(data)):
        d[i] = data[i]
    
    droid = explore(d)
    bfs(droid.board, (0,0), droid.oxygen)
    fill(droid.board, droid.oxygen)
