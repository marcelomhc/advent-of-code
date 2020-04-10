import sys
import re
from collections import defaultdict

def part1(input):
    max_x = 0
    max_y = 0
    for point in input:
        max_x = max(point[0], max_x)
        max_y = max(point[1], max_y)

    print(len(input))

    infinite = set()
    covers = defaultdict(int)
    for i in range(max_x + 1):
        for j in range(max_y + 1):
            min_dist = defaultdict(list)
            minimum = 10000
            for point in input:
                dist = get_dist((i, j), point)
                min_dist[dist].append(point)
                minimum = min(minimum, dist)
            if(len(min_dist[minimum]) == 1):
                covers[min_dist[minimum][0]] += 1
                if(i == 0 or j == 0 or i == max_x or j == max_y):
                    infinite.add(min_dist[minimum][0])

    print covers
    print(len(covers))
    print infinite
    ok = max([covers[point] for point in input if point not in infinite])
    print ok

def part2(input):
    max_x = 0
    max_y = 0
    for point in input:
        max_x = max(point[0], max_x)
        max_y = max(point[1], max_y)

    print(len(input))

    grid = [[0 for i in range(max_y+1)] for i in range(max_x+1)]
    for i in range(max_x + 1):
        for j in range(max_y + 1):
            dist = 0
            for point in input:
                dist += get_dist((i, j), point)
            grid[i][j] = dist

    total = 0
    for i in range(max_x + 1):
        for j in range(max_y + 1):
            total += int(grid[i][j] < 10000)

    print total

def get_dist(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def main(filepath):
    input = []
    with open(filepath, 'r') as f:
        input = [tuple(map(int, line.split(', '))) for line in f.readlines()]
    part2(input)


if __name__ == "__main__":
    main(sys.argv[1])