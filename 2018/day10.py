import re
import sys

class Light(object):
    def __init__(self, x, y, dx, dy):
        self.x = int(y)
        self.y = int(x)
        self.dx = int(dy)
        self.dy = int(dx)

    def step(self):
        self.x = self.x + self.dx
        self.y = self.y + self.dy

    def step_back(self):
        self.x = self.x - self.dx
        self.y = self.y - self.dy

def parse_input(filepath):
    lights = []
    with open(filepath, "r") as f:
        for line in f:
            result = re.match(r'position=<(.+),\s+(.+)> velocity=<(.+),\s+(.+)>', line)
            light = Light(result.group(1), result.group(2), result.group(3), result.group(4))
            lights.append(light)
    return lights

def part1(lights):
    [x, y, mX, mY] = get_borders(lights)

    step = 0
    while (True):
        for light in lights:
            light.step()
        [nX, nY, nmX, nmY] = get_borders(lights)
        if(nX > x or nY > y or mX > nmX or mY > nmY):
            break
        x = nX
        y = nY
        mX = nmX
        mY = nmY
        step += 1

    print step
    grid = [['.' for _ in range(mY-1, y+2)] for _ in range(mX-1, x+2)]
    dx = abs(mX) - 1
    dy = abs(mY) - 1
    for light in lights:
        light.step_back()
        grid[light.x - dx][light.y - dy] = '#'
    for row in grid:
        for col in row:
            print col,
        print '\n'

# X Y -X -Y
def get_borders(lights):
    borders = []
    borders.append((max(lights, key=lambda l: l.x)).x)
    borders.append((max(lights, key=lambda l: l.y)).y)
    borders.append((min(lights, key=lambda l: l.x)).x)
    borders.append((min(lights, key=lambda l: l.y)).y)
    return borders

if __name__ == "__main__":
    lights = parse_input(sys.argv[1])
    part1(lights)