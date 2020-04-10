import sys
import re
from collections import defaultdict, Counter

def part1(filepath):
    pots, transitions = parse_input(filepath)

    for _ in range(20):
        pots = gen_step(pots, transitions)
        
    print(sum([i[0] for i in pots.items() if i[1]]))

def part2(filepath):
    pots, transitions = parse_input(filepath)

    total = sum([i for i in pots.keys()])

    pots = gen_step(pots, transitions)
    gen = 1
    diff = [0,0,0]
    diff.append(sum([i for i in pots.keys()]) - total)
    while (diff[-1] != diff[-2] or diff[-1] != diff[-3] or diff[-1] != diff[-4]):
        total = sum([i for i in pots.keys()])
        pots = gen_step(pots, transitions)
        gen+=1
        diff.append(sum([i for i in pots.keys()]) - total)
        
    print(diff)
    print(gen)
    print((50000000000 - gen)*diff[-1] + sum([i for i in pots.keys()]))

def gen_step(pots, transitions):
    gen = defaultdict(bool)
    left = min(pots.keys()) - 2
    right = max(pots.keys()) + 2
    for idx in range(left, right+1):
        if  transitions[(pots[idx-2], pots[idx-1], pots[idx], pots[idx+1], pots[idx+2])]:
            gen[idx] = True
    return gen

def same_gen(gen1, gen2):
    gen1v = [i[0] for i in gen1.items()]
    gen2v = [i[0] for i in gen2.items()]

    if not (len(gen1v) == len(gen2v)):
        return False

    gen1v = sorted(gen1v)
    gen2v = sorted(gen2v)

    for i in range(len(gen1v)):
        if not (gen1v[i] - gen1v[0] == gen2v[i] - gen2v[0]):
            return False
    return True

def parse_input(filepath):
    pots = defaultdict(bool)
    transitions = defaultdict(bool)
    with open(filepath, 'r') as f:
        initial = f.readline()
        initial = initial[15:-1]
        for i in range(len(initial)):
            pots[i] = (initial[i] == '#')
        f.readline()
        lines = map(lambda o: list(map(lambda oo: oo == '#', o)), re.findall(r'(.)(.)(.)(.)(.) => (.)\n', f.read(), re.MULTILINE))
        for entry in lines:
            transitions[(entry[0], entry[1], entry[2], entry[3], entry[4])] = entry[5]
    return pots,transitions

if __name__ == "__main__":
    part1(sys.argv[1])
    part2(sys.argv[1])