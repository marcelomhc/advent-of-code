import sys

freqs = dict()

def fill_orbits(filepath):
    orbits = dict()
    with open(filepath, "r") as f:
        for line in f:
            orb = line.strip().split(')')
            orbits[orb[1]] = orb[0]
    return orbits

def count_orbits(orbits):
    total_orbits = 0
    for key in orbits.keys():
        curr = key
        n_orbits = 0
        while(orbits.get(curr) != None):
            n_orbits += 1
            curr = orbits[curr]
        total_orbits += n_orbits
    print(total_orbits)

def find_distance(orbits):
    path = dict()
    you = 'YOU'
    san = 'SAN'
    path[you] = 0
    while(orbits[you] != 'COM'):
        n = path[you]
        you = orbits[you]
        path[you] = n + 1
    n_san = 0
    while(path.get(san) == None):
        n_san += 1
        san = orbits[san]
    print(n_san + path[san] - 2)

if __name__ == "__main__":
    orbits = fill_orbits("input/day6.data")
    #Part 1
    count_orbits(orbits)
    #Part 2
    find_distance(orbits)