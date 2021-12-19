from collections import defaultdict


def get_adjacent(x, y):
    return [(x+dx, y+dy) for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]]


def get_risk(grid, x, y):
    dx = x // len(grid)
    dy = y // len(grid)

    max_risk = 9
    risk = (grid[x % len(grid)][y % len(grid)] + dx + dy) % max_risk
    return risk if risk != 0 else max_risk


def min_risk(grid, total_size, xi=0, yi=0):
    risks = defaultdict(lambda: 999999)
    risks[(0, 0)] = 0
    queue = [(xi, yi)]

    while len(queue) > 0:
        xi, yi = queue.pop(0)
        if xi == total_size - 1 and yi == total_size - 1:
            continue

        for x, y in get_adjacent(xi, yi):
            if 0 <= x < total_size and 0 <= y < total_size:
                current_risk = risks[(xi, yi)] + get_risk(grid, x, y)
                if current_risk < risks[(x, y)]:
                    risks[(x, y)] = current_risk
                    queue.append((x, y))
    return risks


def part1(grid):
    risks = min_risk(grid, len(grid))
    print(risks[(len(grid)-1, len(grid)-1)])


def part2(grid):
    total_size = 5*len(grid)
    risks = min_risk(grid, 5*len(grid))
    print(risks[(total_size-1, total_size-1)])


if __name__ == '__main__':
    with open("input/day15.data", 'r') as f:
        data = [[int(c) for c in line.strip()] for line in f.readlines()]
    part1(data)
    part2(data)
