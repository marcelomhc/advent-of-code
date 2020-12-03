def parse_input(filepath):
    with open(filepath, 'r') as f:
        lines = f.readlines()
        grid = dict()

        for y in range(len(lines)):
            for x in range(len(lines[y])):
                if lines[y][x] == '#':
                    grid[(x, y)] = 1

    return grid, y+1, x+1


def find_trees(parsed, max_y, max_x, slope_x, slope_y):
    x = y = trees = 0
    while y < max_y:
        trees += parsed.get((x, y), 0)
        y += slope_y
        x = (x + slope_x) % max_x
    print("Slope: (", slope_y, slope_x, ") trees: ", trees)
    return trees


def multiply_slopes(parsed, h, w, slopes):
    result = 1
    for x, y in slopes:
        result *= find_trees(parsed, h, w, x, y)

    print(result)


if __name__ == "__main__":
    inp, height, width = parse_input("input/day3.data")
    find_trees(inp, height, width, 3, 1)
    multiply_slopes(inp, height, width, [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)])
