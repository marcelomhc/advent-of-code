def parse_input(filepath):
    with open(filepath, "r") as f:
        grid = [[c for c in line.strip()] for line in f.readlines()]
    return grid


def simulate_seating(grid, behavior, max_seats):
    prev = -1
    occupied = 0

    while prev != occupied:
        prev = occupied
        occupied = 0
        new_grid = [['.' for c in line] for line in grid]
        for x in range(len(grid)):
            for y in range(len(grid[x])):
                new = step(grid, x, y, behavior, max_seats)
                occupied += int(new == '#')
                new_grid[x][y] = new
        grid = new_grid
    print(occupied)


def step(grid, x, y, behavior, max_seats):
    if grid[x][y] != '.':
        adj = behavior(grid, x, y)
        if grid[x][y] == 'L' and adj == 0:
            return '#'
        if grid[x][y] == '#' and adj >= max_seats:
            return 'L'
    return grid[x][y]


def count_adjacent(grid, x, y):
    adj = 0
    for i in [-1, 0, 1]:
        if 0 <= x+i < len(grid):
            for j in [-1, 0, 1]:
                if 0 <= y+j < len(grid[x]):
                    adj += int(grid[x+i][y+j] == '#')
    adj -= int(grid[x][y] == '#')
    return adj


def count_in_sight(grid, x, y):
    adj = 0
    for i in [-1, 0, 1]:
        for j in [-1, 0, 1]:
            ii = i
            jj = j
            while True:
                if not (0 <= x+ii < len(grid) and 0 <= y+jj < len(grid[x])):
                    break
                if grid[x+ii][y+jj] == 'L':
                    break
                if grid[x+ii][y+jj] == '#':
                    adj += 1
                    break
                ii += i
                jj += j

    adj -= int(grid[x][y] == '#')
    return adj


if __name__ == "__main__":
    data = parse_input("input/day11.data")
    simulate_seating(data, count_adjacent, 4)
    simulate_seating(data, count_in_sight, 5)
