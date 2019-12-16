from math import atan2, degrees
from collections import deque


class Moon(object):

    def __init__(self, x, y, z):
        self.x = x
        self.dx = 0
        self.y = y
        self.dy = 0
        self.z = z
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

if __name__ == "__main__":
    moons = list()
    moons.append(Moon(1, 2, -9))
    moons.append(Moon(-1, -9, -4))
    moons.append(Moon(17, 6, 8))
    moons.append(Moon(12, 4, 2))

    predict(moons, 1000)
