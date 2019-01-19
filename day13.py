import sys
from collections import defaultdict

class Cart(object):
    def __init__(self, x, y, direction):
        self.x = int(x)
        self.y = int(y)

        self.turns = '<'
        self.turn(direction)

    def position(self):
        return (self.x, self.y)
    
    def turn(self, direction):
        if(direction == 'v'):
            self.dx = 1
            self.dy = 0
            self.direction = 'v'
        elif(direction == '>'):
            self.dx = 0
            self.dy = 1
            self.direction = '>'
        elif(direction == '<'):
            self.dx = 0
            self.dy = -1
            self.direction = '<'
        else:
            self.dx = -1
            self.dy = 0
            self.direction = '^'

    def move(self):
        self.x += self.dx
        self.y += self.dy

    def cross(self):
        if(self.turns == '<'):
            if(self.direction == 'v'):
                self.turn('>')
            elif(self.direction == '>'):
                self.turn('^')
            elif(self.direction == '<'):
                self.turn('v')
            else:
                self.turn('<')
            self.turns = '-'
        elif(self.turns == '>'):
            if(self.direction == 'v'):
                self.turn('<')
            elif(self.direction == '>'):
                self.turn('v')
            elif(self.direction == '<'):
                self.turn('^')
            else:
                self.turn('>')
            self.turns = '<'
        else:
            self.turns = '>'
        
    def obstacle(self, path):
        paths = ['<', 'v', '>', '^']
        if (path == '+'):
            self.cross()
        elif(path == '/'):
            if(self.direction == '<'):
                self.turn('v')
            elif(self.direction == 'v'):
                self.turn('<')
            elif(self.direction == '>'):
                self.turn('^')
            else:
                self.turn('>')
        else:
            if(self.direction == '<'):
                self.turn('^')
            elif(self.direction == 'v'):
                self.turn('>')
            elif(self.direction == '>'):
                self.turn('v')
            else:
                self.turn('<')


def part1(filepath):
    grid, carts = parse(filepath)
    pos = (-1, -1)
    
    while(pos == (-1,-1)):
        pos = tick(carts, grid)

    print pos

def tick(carts, grid):
    cart_pos = sorted(carts.keys(), key=lambda c: (c[0], c[1]))
    for pos in cart_pos:
        curr = carts.pop(pos)
        curr.move()
        new_pos = curr.position()
        if(new_pos in carts.keys()):
            return new_pos
        if(new_pos in grid.keys()):
            curr.obstacle(grid[new_pos])
        carts[new_pos] = curr
    return (-1, -1)


def part2(filepath):
    grid, carts = parse(filepath)
    
    while(len(carts.keys()) > 1):
        tick2(carts, grid)

    print carts.keys()

def tick2(carts, grid):
    cart_pos = sorted(carts.keys(), key=lambda c: (c[0], c[1]))
    for pos in cart_pos:
        if(pos in carts.keys()):
            curr = carts.pop(pos)
            curr.move()
            new_pos = curr.position()
            if(new_pos in carts.keys()):
                carts.pop(new_pos)
            else:
                if(new_pos in grid.keys()):
                    curr.obstacle(grid[new_pos])
                carts[new_pos] = curr

def parse(filepath):
    grid = dict()
    carts = dict()

    with open(filepath, 'r') as f:
        lines = f.readlines()
        for i in range(len(lines)):
            for j in range(len(lines[i])):
                char = lines[i][j]
                if(char == '/' or char == '\\' or char == '+'):
                    grid[(i,j)] = char
                elif(char == '<' or char == '>' or char == 'v' or char == '^'):
                    cart = Cart(i, j, char)
                    carts[(i,j)] = cart

    return grid, carts

if __name__ == "__main__":
    part1(sys.argv[1])
    part2(sys.argv[1])