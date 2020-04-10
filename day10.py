from math import atan2, degrees
from collections import deque

def parse(filepath):
    with open(filepath, 'r') as f:
        lines = f.readlines()

        grid = dict()

        for i in range(len(lines)):
            for j in range(len(lines[i])):
                char = lines[i][j]
                if(char == '#'):
                    grid[(j,i)] = set()
    return grid

def find_monitoring_station(grid):
    get_angles(grid)
    maxlen = 0
    for asteroid in grid.keys():
        if(len(grid[asteroid]) > maxlen):
            maxlen = len(grid[asteroid])
            pos = asteroid
    print(maxlen)
    print(pos)
    return pos


def get_angles(grid):
    asteroids = grid.keys()
    for asteroid in asteroids:
        for asteroid2 in asteroids:
            if(asteroid2 != asteroid):
                angle = get_angle(asteroid, asteroid2)
                grid[asteroid].add(angle)

def get_angle(a, b):
    x,y = a
    x1,y1 = b
    return atan2(y-y1, x1-x)

def vaporize_from(asteroid, grid):
    vaporization = dict()
    for asteroid2 in grid.keys():
        if(asteroid2 != asteroid):
            angle = get_angle(asteroid, asteroid2)
            vaporization.setdefault((degrees(angle)+360)%360, list()).append(asteroid2)

    rotation = deque(sorted(vaporization))
    while(rotation[0] < 90):
        rotation.rotate(-1)
    vaporized = 0
    while(vaporized < 200):
        angle = rotation[0]
        rotation.rotate(1)
        asteroids = vaporization.get(angle)
        if(len(asteroids) == 0):
            continue
        curr = sorted(asteroids, key=lambda l: abs(asteroid[0] - l[0]) + abs(asteroid[1]-l[1]))[0]

        asteroids.remove(curr)
        vaporized += 1
    print(curr[0]*100+curr[1])


if __name__ == "__main__":
    grid = parse("input/day10.data")
    station = find_monitoring_station(grid)
    print('Vaporizing')
    vaporize_from(station, grid)

