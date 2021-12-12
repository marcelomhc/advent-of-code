def get_adjacent(grid, x, y):
    adj = dict()
    delta = [(0, -1), (-1, 0), (0, 1), (1, 0)]
    for i, j in delta:
        if 0 <= x+i < len(grid) and 0 <= y+j < len(grid[x]):
            adj[(x+i, y+j)] = grid[x+i][y+j]
    return adj


def basin_size(grid, x, y, included):
    if (x, y) not in included:
        included.append((x, y))
        adjacent = get_adjacent(grid, x, y)
        for (xx, yy), adj in adjacent.items():
            if (xx, yy) not in included and adj < 9:
                basin_size(grid, xx, yy, included)
        return included
    return []


def find_minimums(grid):
    minimums = dict()
    for x in range(len(grid)):
        for y in range(len(grid[x])):
            adjacent = get_adjacent(grid, x, y).values()
            if grid[x][y] < min(adjacent):
                minimums[(x, y)] = grid[x][y]
    return minimums


def part1(grid):
    minimums = find_minimums(grid).values()
    print(sum(minimums) + len(minimums))


def part2(grid):
    basins = sorted([len(basin_size(grid, x, y, [])) for x, y in find_minimums(grid).keys()], reverse=True)
    print(basins[0]*basins[1]*basins[2])


if __name__ == "__main__":
    with open("input/day09.data", 'r') as f:
        data = [[int(c) for c in line.strip()] for line in f.readlines()]
    part1(data)
    part2(data)
    