import random
from collections import defaultdict, deque

freqs = dict()

class IntComputer(object):
    def __init__(self, filepath, base = 0, value = []):
        self.program = self.decode(filepath)
        self.pos = 0
        self.input = deque(value)
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

class Droid(object):
    def __init__(self, grid):
        self.grid = grid
        self.direction = deque([(0,-1), (1,0), (0,1), (-1,0)])
        for position, element in grid.items():
            if element == 94:
                self.pos = position

    def move(self):
        if(self.try_move(self.direction[0])):
            self.pos = tuple(map(sum, zip(self.pos, self.direction[0])))
            return 'F'
        elif(self.try_move(self.direction[1])):
            self.direction.rotate(-1)
            return 'R'
        elif(self.try_move(self.direction[-1])):
            self.direction.rotate(1)
            return 'L'
        else:
            return 'X'

    def try_move(self, delta):
        dx, dy = delta
        x, y = self.pos
        if (self.grid.get((x+dx, y+dy), -1) == 35):
            return True
        return False

class KMP:
    def partial(self, pattern):
        """ Calculate partial match table: String -> [Int]"""
        ret = [0]

        for i in range(1, len(pattern)):
            j = ret[i - 1]
            while j > 0 and pattern[j] != pattern[i]:
                j = ret[j - 1]
            ret.append(j + 1 if pattern[j] == pattern[i] else j)
        return ret

    def search(self, T, P):
        """
        KMP search main algorithm: String -> String -> [Int]
        Return all the matching position of pattern string P in S
        """
        partial, j = self.partial(P), 0

        for i in range(len(T)):
            while j > 0 and T[i] != P[j]:
                j = partial[j - 1]
            if T[i] == P[j]: j += 1
            if j == len(P):
                return (i - (j - 1))
        return -1

def intersections(panels):
    keys = panels.keys()
    maxX = max(keys, key=lambda l: l[0])[0]
    maxY = max(keys, key=lambda l: l[1])[1]
    alingment = 0

    for j in range (maxY):
        for i in range (maxX+1):
            pixel = panels[(i,j)]
            if (pixel == 35 and is_intersection((i,j), panels)):
                alingment += i*j
            print(chr(panels[(i,j)]), end='')
    print(alingment)

def is_intersection(pos, grid):
    x,y = pos
    intersection = True
    for position in [(x+1,y), (x-1,y), (x,y+1), (x,y-1)]:
        intersection = intersection and grid.get(position, -1) == 35
    return intersection

def explore(computer):
    grid = dict()
    x = y = 0

    while(not computer.is_done()):
        point = computer.run()
        if(point != None):
            grid[(x,y)] = point
            if(point == 10):
                x = 0
                y += 1
            else:
                x += 1
    intersections(grid)
    return grid

def clean(droid):
    routine = walk(droid) + [ord('n'), 10]
    print(routine)
    computer = IntComputer("input/day17.data", value=routine)
    computer.program[0] = 2

    while(not computer.is_done()):
        out = computer.run()
        if(out != None):
            print(chr(out), end='')

def walk(droid):
    steps = 0
    path = list()
    direction = droid.move()
    turn = 'X'
    while(direction != 'X'):
        if(direction == 'F'):
            steps += 1
        else:
            path.append((turn, str(steps)))
            turn = direction
            steps = 0
        direction = droid.move()
    path.append((turn,str(steps)))
    path = path[1:]

    A,B,C,routine = compress(path)
    print(routine)

    routine = [ord(c) for c in ",".join(routine)] + [10] + [ord(c) for c in ",".join([x for t in A for x in t])] + [10] + [ord(c) for c in ",".join([x for t in B for x in t])] + [10] + [ord(c) for c in ",".join([x for t in C for x in t])] + [10]

    return routine

def compress(path):

    for i in range(1,9):
        patterns = path.copy()
        A = patterns[:i]

        patterns = replace_list(patterns, A, [])
        for j in range(1,9):
            patternsB = patterns.copy()
            B = patternsB[:j]

            patternsB = replace_list(patternsB, B, [])
            if(len(patternsB) == 0):
                continue
            for k in range(1,9):
                patternsC = patternsB.copy()
                C = patternsC[:k]
                #print(patternsC)
                patternsC = replace_list(patternsC, C, [])
                if(len(patternsC) == 0):
                    routine = path.copy()
                    routine = replace_list(routine, C, [])
                    routine = replace_list(routine, B, [])
                    routine = replace_list(routine, A, [])
                    if(len(routine) == 0):
                        routine = path.copy()
                        routine = replace_list(routine, C, ['C'])
                        routine = replace_list(routine, B, ['B'])
                        routine = replace_list(routine, A, ['A'])
                        return A,B,C,routine

def replace_list(patterns, A, B):
    k = KMP().search(patterns, A)
    while(k != -1):
        patterns = patterns[:k:] + B + patterns[k+len(A):]
        k = KMP().search(patterns, A)
    return patterns

if __name__ == "__main__":
    computer = IntComputer("input/day17.data", value=[])
    
    grid = explore(computer)
    
    clean(Droid(grid))
