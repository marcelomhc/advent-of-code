from itertools import combinations 
from math import gcd

class Moon(object):

    def __init__(self, x, y, z):
        self.x = x
        self.ix = x
        self.dx = 0
        self.y = y
        self.iy = y
        self.dy = 0
        self.z = z
        self.iz = z
        self.dz = 0

    def print(self):
        print("x: " + str(self.x) + " y: " + str(self.y) + " z: " + str(self.z) + " ....  dx: " + str(self.dx) + " dy: " + str(self.dy) + " dz: " + str(self.dz))

    def move(self):
        self.x += self.dx
        self.y += self.dy
        self.z += self.dz

    def gravity(self, moons):
        for moon in moons:
            self.dx += self.compare(self.x, moon.x)
            self.dy += self.compare(self.y, moon.y)
            self.dz += self.compare(self.z, moon.z)

    def compare(self, a, b):
        if(a < b):
            return 1
        elif(b < a):
            return -1
        else:
            return 0
    
    def total_energy(self):
        return (abs(self.x) + abs(self.y) + abs(self.z)) * (abs(self.dx) + abs(self.dy) + abs(self.dz))

def apply_gravity(moons):
    for moon in moons:
        moon.gravity(moons)

def tick_time(moons):
    for moon in moons:
        moon.move()

def predict(moons, ticks):
    for _ in range(ticks):
        apply_gravity(moons)
        tick_time(moons)
    
    energy = 0
    for moon in moons:
        energy += moon.total_energy()
    print(energy)

# PART 2
def compare(a, b):
    if(a < b):
        return 1
    elif(b < a):
        return -1
    else:
        return 0

def lcm(a,b):
    return a * b // gcd(a, b)

def find_cycle(moons):
    pairs = [x for x in combinations(moons, 2)]
    stepsx = 0
    stepsy = 0
    stepsz = 0

    initial = False
    while(not initial):
        for a, b in pairs:
            dx = compare(a.x, b.x)
            a.dx += dx
            b.dx -= dx
        for moon in moons:
            moon.x += moon.dx

        stepsx += 1
        initial = all([moon.x == moon.ix and moon.dx == 0 for moon in moons])

    initial = False
    while(not initial):
        for a, b in pairs:
            dy = compare(a.y, b.y)
            a.dy += dy
            b.dy -= dy
        for moon in moons:
            moon.y += moon.dy

        stepsy += 1
        initial = all([moon.y == moon.iy and moon.dy == 0 for moon in moons])

    initial = False
    while(not initial):
        for a, b in pairs:
            dz = compare(a.z, b.z)
            a.dz += dz
            b.dz -= dz
        for moon in moons:
            moon.z += moon.dz

        stepsz += 1
        initial = all([moon.z == moon.iz and moon.dz == 0 for moon in moons])

    print(stepsx)
    print(stepsy)
    print(stepsz)
    print(lcm(stepsx, lcm(stepsy, stepsz)))


if __name__ == "__main__":
    moons = list()
    moons.append(Moon(1, 2, -9))
    moons.append(Moon(-1, -9, -4))
    moons.append(Moon(17, 6, 8))
    moons.append(Moon(12, 4, 2))

    predict(moons, 1000)

    #part 2
    moons = list()
    moons.append(Moon(1, 2, -9))
    moons.append(Moon(-1, -9, -4))
    moons.append(Moon(17, 6, 8))
    moons.append(Moon(12, 4, 2))
    find_cycle(moons)
