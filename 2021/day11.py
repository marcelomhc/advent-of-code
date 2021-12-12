def get_adjacent(grid, x, y):
    adj = set()
    for i in [-1, 0, 1]:
        if 0 <= x+i < len(grid):
            for j in [-1, 0, 1]:
                if 0 <= y+j < len(grid[x]):
                    adj.add((x+i, y+j))
    adj.remove((x, y))
    return adj


def flash(grid, x, y, flashed):
    if (x, y) in flashed:
        return flashed

    flashed.add((x, y))
    for xx, yy in get_adjacent(grid, x, y):
        grid[xx][yy] = grid[xx][yy]+1
        if grid[xx][yy] > 9:
            flash(grid, xx, yy, flashed)
    return flashed


def flash_step(grid):
    flashed = set()
    for x in range(len(grid)):
        for y in range(len(grid[x])):
            grid[x][y] = grid[x][y] + 1
            if grid[x][y] > 9:
                flashed = flash(grid, x, y, flashed)
    for x in range(len(grid)):
        for y in range(len(grid[x])):
            if grid[x][y] > 9:
                grid[x][y] = 0
    return len(flashed)


def part1(grid):
    print(sum([flash_step(grid) for _ in range(100)]))


def part2(grid):
    step = 1
    while flash_step(grid) != 100:
        step += 1
    print(step+100)


if __name__ == "__main__":
    with open("input/day11.data", 'r') as f:
        data = [[int(c) for c in line.strip()] for line in f.readlines()]
    part1(data)
    part2(data)
