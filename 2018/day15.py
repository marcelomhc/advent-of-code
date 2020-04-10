import sys, copy
from collections import defaultdict

class Creature(object):
    def __init__(self, x, y, race, pwr):
        self.x = x
        self.y = y
        self.dx = 0
        self.dy = 0
        self.race = race
        self.hp = 200
        self.power = pwr
        self.alive = True
        self.target = self
    
    def act(self):
        if(self.alive):
            self.move()
            self.attack()

    def move(self):
        self.x += self.dx
        self.y += self.dy

    def attack(self):
        self.target.attacked(self.power)

    def set_target(self, enemy):
        self.target = enemy
    
    def movement(self, direction):
        if (direction == 0):
            self.dx = 0
            self.dy = 0
        elif(direction == 1):
            self.dx = -1
            self.dy = 0
        elif(direction == 2):
            self.dx = 0
            self.dy = -1
        elif(direction == 3):
            self.dx = 0
            self.dy = 1
        else:
            self.dx = 1
            self.dy = 0

    def attacked(self, damage):
        self.hp -= damage
        if (self.hp < 1):
            self.alive = False

    def __repr__(self):
        return self.race + " - HP " + str(self.hp)

    def __str__(self):
        return self.race + ": (" + str(self.x) + ", " + str(self.y) + ")"

def part1(filepath):
    grid, creatures, elfs, goblins = parse(filepath, 3)

    rounds = 0
    while(True):
        print("Starting round: " + str(rounds+1))
        finished, elfs, goblins, ended = round(grid, creatures, elfs, goblins)
        if (ended):
            rounds += 1
        if (finished):
            break
            
    hp = sum([c.hp for c in creatures.values()])
    print("Finished rounds: " + str(rounds))
    print("Total hp left: " + str(hp))
    print("Outcome: " + str(hp * rounds))

def part2(filepath):
    died = True
    pwr = 4
    while (died):
        grid, creatures, elfs, goblins = parse(filepath, pwr)

        rounds = 0
        while(True):
            finished, e, goblins, ended = round(grid, creatures, elfs, goblins)
            if (ended):
                rounds += 1
            if(e < elfs):
                died = True
                pwr += 1
                print("power " + str(pwr))
                print("lasted " + str(rounds))
                break
            died = False
            if (finished):
                break
            
    hp = sum([c.hp for c in creatures.values()])
    print("Finished rounds: " + str(rounds))
    print("Total hp left: " + str(hp))
    print("Outcome: " + str(hp * rounds))

def round(grid, creatures, e, g):
    units = sorted(creatures.items(), key=lambda c: c[0])

    #roundmap = prepare_round(grid, creatures)
    #printstatus(roundmap, creatures)

    for i in range(len(units)):
        unit = units[i][1]
        if (unit.alive):
            creature = creatures.pop(units[i][0])
            nearest = get_closest((creature.x, creature.y), grid, creature.race, creatures)

            creature.movement(nearest[1])
            creature.move()
            creatures[(creature.x, creature.y)] = creature
            
            target = get_targets(creature, creatures)
            creature.set_target(target)
            if(target != None):
                creature.attack()
                if not (target.alive):
                    creatures.pop((target.x, target.y))
                    if (target.race == 'E'):
                        e -= 1
                    else:
                        g -= 1
                    if(e == 0 or g ==0):
                        return True, e, g, i == len(units) - 1
    return False, e, g, True

def get_targets(creature, creatures):
    x = creature.x
    y = creature.y
    keys = [key for key in creatures.keys() if (creatures[key].race != creature.race)]
    possibles = list()
    possibles += [creatures[(x-1,y)]] if (x-1,y) in keys else []
    possibles += [creatures[(x+1,y)]] if (x+1,y) in keys else []
    possibles += [creatures[(x,y-1)]] if (x,y-1) in keys else []
    possibles += [creatures[(x,y+1)]] if (x,y+1) in keys else []
    if(len(possibles) == 0):
        return None
    return sorted(possibles, key=lambda p: (p.hp, p.x, p.y))[0]

def prepare_round(grid, creatures):
    roundmap = [[c for c in line] for line in grid]
    for creature in creatures.values():
        roundmap[creature.x][creature.y] = creature.race
    return roundmap

def get_closest(pos, grid, race, creatures):
    queue = list()
    visited = list()
    x = pos[0]
    y = pos[1]
    found = [(99999, 0, -1, -1)]

    queue.append((x-1, y, 0, 1))
    queue.append((x, y-1, 0, 2))
    queue.append((x, y+1, 0, 3))
    queue.append((x+1, y, 0, 4))

    while(len(queue) > 0):
        (x, y, d, p) = queue.pop(0)
        if not ((x, y) in visited):
            visited.append((x,y))
            if ((x, y) in creatures.keys()):
                if(creatures[(x,y)].race != race):
                    if (found[0][0] > d):
                        found = [(d, p, x, y)]
                    elif(found[0][0] == d):
                        found.append((d, p, x, y))
                else:
                    continue
            elif (grid[x][y] == '#'):
                continue
            else:            
                queue.append((x-1, y, d+1, p))
                queue.append((x, y-1, d+1, p))
                queue.append((x, y+1, d+1, p))
                queue.append((x+1, y, d+1, p))
    found = sorted(found, key=lambda l: (l[2], l[3]))
    trgt = found[0]
    if(trgt[0] == 0):
        trgt = (trgt[0], 0)
    return trgt

def printstatus(grid, creatures):
    for line in grid:
        for char in line:
            print(char, end="")
        print('')
    print(creatures)
    print(sum([c.hp for c in creatures.values()]))

def parse(filepath, pwr):
    with open(filepath, 'r') as f:
        lines = f.readlines()

        grid = [['.' for _ in range(len(lines[0])-1)] for _ in range(len(lines))]
        goblins = 0
        elfs = 0
        creatures = dict()

        for i in range(len(lines)):
            for j in range(len(lines[i])):
                char = lines[i][j]
                if(char == '#'):
                    grid[i][j] = '#'
                elif(char == 'G'):
                    creatures[(i, j)] = Creature(i, j, 'G', 3)
                    goblins += 1
                elif(char == 'E'):
                    creatures[(i,j)] = Creature(i, j, 'E', pwr)
                    elfs += 1

    return grid, creatures, elfs, goblins

if __name__ == "__main__":
    part1(sys.argv[1])
    part2(sys.argv[1])
if __name__ == "__main__":
    part1(sys.argv[1])
    part2(sys.argv[1])