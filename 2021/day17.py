def move_x(x, dx):
    x += dx
    dx = dx - 1 if dx > 0 else dx + 1 if x < 0 else 0
    return x, dx


def move_y(y, dy):
    y += dy
    dy -= 1
    return y, dy


def find_x(zone_x):
    xmin, xmax = zone_x
    possibles = set()

    for xi in range(1, xmax+1):
        x = 0
        n = 1
        dx = xi
        while x <= xmax and dx > 0:
            x, dx = move_x(x, dx)
            if xmin <= x <= xmax:
                possibles.add((xi, n))
                if dx == 0:
                    possibles.add((xi, -1))
            n += 1
    return possibles


def find_y(zone_y):
    ymin, ymax = zone_y
    possibles = set()

    for yi in range(ymin, (ymin*-1)+1):
        y = 0
        n = 1
        dy = yi
        while y >= ymin:
            y, dy = move_y(y, dy)
            if ymin <= y <= ymax:
                possibles.add((yi, n))
            n += 1
    return possibles


def part1(zone_x, zone_y):

    xs = find_x(zone_x)
    ys = find_y(zone_y)
    high = []
    for y, n in ys:
        for x, n2 in xs:
            if n >= n2:
                high.append(sum(range(y+1)))
    print(max(high))


def part2(zone_x, zone_y):

    xs = find_x(zone_x)
    ys = find_y(zone_y)
    combinations = set()
    for y, n in ys:
        for x, n2 in xs:
            if n2 == -1:
                step = min([step for x, step in filter(lambda l: (l[0] == x and l[1] != -1), xs)])
                if n >= step:
                    combinations.add((x, y))
            if n == n2:
                combinations.add((x, y))
    print(len(combinations))


if __name__ == '__main__':
    x_min = 60
    x_max = 94
    y_min = -171
    y_max = -136
    part1((x_min, x_max), (y_min, y_max))
    part2((x_min, x_max), (y_min, y_max))
