from collections import defaultdict, Counter
import sys, re

def part1(filepath):
    soil = parse(filepath)

    keys = soil.keys()
    borders = [
        min(keys, key=lambda k: k[0])[0],
        max(keys, key=lambda k: k[0])[0],
        min(keys, key=lambda k: k[1])[1],
        max(keys, key=lambda k: k[1])[1]
    ]

    flowdown((500, borders[2]), soil, borders, False)
    print(Counter(soil.values()))

def part2(filepath):
    soil = parse(filepath)

    keys = soil.keys()
    borders = [
        min(keys, key=lambda k: k[0])[0],
        max(keys, key=lambda k: k[0])[0],
        min(keys, key=lambda k: k[1])[1],
        max(keys, key=lambda k: k[1])[1]
    ]

    flowdown((500, borders[2]), soil, borders, True)
    print(Counter(soil.values()))

def flowdown(pos, soil, borders, dry):
    (x, y) = pos
    while(soil[(x,y)] != '#' and y <= borders[3]):
        if(not dry):
            soil[(x,y)] = '~'
        y=y+1
    if (y > borders[3]):
        return
    return flowsides((x, y-1), soil, borders, dry)

def flowsides(pos, soil, borders, dry):
    (x,y) = pos
    left = right = x
    max_left = max_right = x
    while(soil[(max_left,y+1)] == '#'):
        max_left -= 1
    while(soil[(max_right,y+1)] == '#'):
        max_right += 1
    over = False
    while(not over):
        left = right = x
        while(max_left < left and soil[left,y] != '#'):
            if(soil[left,y+1] == '.'):
                flowdown((left,y), soil, borders, dry)
            left -= 1
        while(right < max_right and soil[right,y] != '#'):
            if(soil[right,y+1] == '.'):
                flowdown((right,y), soil, borders, dry)
            right += 1
        over = left == max_left or right == max_right
        if(not over or not dry):
            for i in range(left+1,right):
                soil[(i,y)] = '~'
        y = y-1

    y += 1
    if(soil[left,y] == '.'):
        flowdown((left,y), soil, borders, dry)
    if(soil[right,y] == '.'):
        flowdown((right, y), soil, borders, dry)
        

def parse(filepath):
    grid = defaultdict(lambda: '.')
    with open(filepath, 'r') as f:
        for line in f.readlines():
            x = re.match('.*x=(\d+)(?:..)(\d+)?', line)
            y = re.match('.*y=(\d+)(?:..)(\d+)?', line)

            x1 = int(x.group(1))
            y1 = int(y.group(1))
            x2 = x.group(2)
            y2 = y.group(2)

            if(x2 != None):
                for i in range(x1, int(x2)+1):
                    grid[(i, y1)] = '#'
            else:
                for j in range(y1, int(y2)+1):
                    grid[(x1, j)] = '#'
    return grid

def printsoil(soil):
    keys = soil.keys()
    maxX = max(keys, key=lambda k: k[0])
    minX = min(keys, key=lambda k: k[0])
    maxY = max(keys, key=lambda k: k[1])
    minY = min(keys, key=lambda k: k[1])

    for j in range(minY[1]-1, maxY[1]+1):
        for i in range(minX[0], maxX[0]+1):
            if(j == minY[1]-1 and i == 500):
                print '+',
                continue
            print soil[(i,j)],    
        print '' 

if __name__ == "__main__":
    part1(sys.argv[1])
    part2(sys.argv[1])