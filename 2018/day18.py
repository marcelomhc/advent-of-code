import sys
from collections import defaultdict, Counter

def part1(filepath):
    camp = parse(filepath)
    
    for _ in range(10):
        camp = round(camp)

    t = l = 0
    for line in camp:
        c = Counter(line)
        t += c['|']
        l += c['#']
    printgrid(camp)
    print(t*l)

def part2(filepath):
    camp = parse(filepath)

    pattern = dict()
    for _ in range(100):
        camp = round(camp)
    r = 100
    pattern[r] = camp
    while(True):
        camp = round(camp)
        r+=1
        if(camp in pattern.values()):
            i = [k for (k,c) in pattern.items() if c == camp]
            break
        pattern[r] = camp
    
    left = (1000000000-r) % (r - i[0])
    for _ in range(left):
        camp = round(camp)
    t = l = 0
    for line in camp:
        c = Counter(line)
        t += c['|']
        l += c['#']
    printgrid(camp)
    print(t*l)
    

def round(camp):
    new = list()
    for i in range(len(camp)):
        line = camp[i]
        new_line = list()
        for j in range(len(line)):
            new_line.append(update(camp, i, j))
        new.append(new_line)
    return new

def update(camp, i, j):
    c = defaultdict(int)
    for dx, dy in [(-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]:
        ii = i + dx
        jj = j + dy
        if(ii < 0 or ii > len(camp)-1 or jj < 0 or jj > len(camp[ii])-1):
            continue
        c[camp[ii][jj]] = c[camp[ii][jj]] + 1

    if(camp[i][j] == '.'):
        if (c['|'] > 2):
            return '|'
        else:
            return '.'
    elif(camp[i][j] == '|'):
        if(c['#'] > 2):
            return '#'
        else:
            return '|'
    else:
        if('#' in c.keys() and '|' in c.keys()):
            return '#'
        else:
            return '.'

def parse(filepath):
    with open(filepath, 'r') as f:
        camp = list()
        for line in f.readlines():
            l = list()
            for c in line:
                if(c != '\n'):
                    l.append(c)
            camp.append(l)
    return camp

def printgrid(grid):
    for line in grid:
        for char in line:
            print char,
        print('')


if __name__ == "__main__":
    #part1(sys.argv[1])
    part2(sys.argv[1])