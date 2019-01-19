def part1(input):
    size = 300
    grid = [[0 for _ in range(size)] for _ in range(size)]

    for row in range(1, size+1):
        for col in range(1, size+1):
            rackId = row+10
            grid[row-1][col-1] = (((rackId*col+input)*rackId) % 1000) // 100 - 5

    max_power = (0, -1, -1)
    for row in range(size-3):
        for col in range(size-3):
            power = get_power(grid, row, col, 3)
            if power > max_power[0]:
                max_power = (power, row+1, col+1)

    print(max_power)

def part2(input):
    size = 300
    grid = [[0 for _ in range(size)] for _ in range(size)]

    for row in range(1, size+1):
        for col in range(1, size+1):
            rackId = row+10
            grid[row-1][col-1] = (((rackId*col+input)*rackId) % 1000) // 100 - 5

    max_power = (0, -1, -1, 0)
    for row in range(size):
        for col in range(size):
            square = min(size-row, size-col)
            for i in range(1, square):
                power = get_power(grid, row, col, i)
                if power > max_power[0]:
                    max_power = (power, row+1, col+1, square)

    print(max_power)

def part22(input):
    size = 300
    grid = [[0 for _ in range(size)] for _ in range(size)]

    for row in range(1, size+1):
        for col in range(1, size+1):
            rackId = row+10
            grid[row-1][col-1] = (((rackId*col+input)*rackId) % 1000) // 100 - 5

    max_power = (-999999, -1, -1, 0)
    for square in range(1, size+1):
        for row in range(size-square+1):
            if(row == 0):
                row_power = get_power(grid, 0, 0, square)
            else:
                row_power = row_power + power_row(grid, row+square-1, 0, square) - power_row(grid, row-1, 0, square)
            if row_power > max_power[0]:
                max_power = (row_power, row+1, 1, square)

            col_power = row_power
            for col in range(1, size-square):
                col_power = col_power + power_col(grid, row, col+square-1, square) - power_col(grid, row, col-1, square)
                if col_power > max_power[0]:
                    max_power = (col_power, row+1, col+1, square)
    print(max_power)

def power_col(grid, row, col, square):
    power = 0
    for i in range(square):
        power += grid[row+i][col]
    return power

def power_row(grid, row, col, square):
    power = 0
    for i in range(square):
        power += grid[row][col+i]
    return power


def get_power(grid, row, col, size):
    power = 0
    for i in range(row, row+size):
        for j in range(col, col+size):
            power += grid[i][j]
    return power

if __name__ == "__main__":
    part1(3613)
    part22(3613)