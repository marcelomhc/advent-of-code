import re, sys

def part1(filepath):
    nano = parse(filepath)
    nano = sorted(nano, key= lambda l: l[3], reverse=True)
    r = nano[0]
    print('radius: ' + str(r[3]))
    inr = 0
    for robot in nano:
        inr += int((abs(robot[0] - r[0]) + abs(robot[1] - r[1]) + abs(robot[2] - r[2])) <= r[3])
    print(inr)

def part2(filepath):
    nanobots = parse(filepath)

def parse(filepath):
    nanobots = list()
    with open(filepath, 'r') as f:
        for line in f.readlines():
            n = re.match('pos=<(-*\d+),(-*\d+),(-*\d+)>, r=(\d+)', line)
            nanobots.append(tuple(map(int, n.groups())))
        return nanobots

if __name__ == "__main__":
    part1(sys.argv[1])