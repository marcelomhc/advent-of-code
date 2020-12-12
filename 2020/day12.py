def get_coordinates(filepath):
    with open(filepath, 'r') as f:
        coordinates = [(x[0], int(x[1:])) for x in f.readlines()]
    return coordinates


def part1(coordinates):
    directions = [(1, 0), (0, -1), (-1, 0), (0, 1)]
    bearing = 0
    x = y = 0
    for action, value in coordinates:
        if action == 'F':
            delta = directions[bearing]
            x += delta[0]*value
            y += delta[1]*value
        elif action == 'N':
            y += value
        elif action == 'S':
            y -= value
        elif action == 'E':
            x += value
        elif action == 'W':
            x -= value
        elif action == 'R':
            bearing += value // 90
            bearing %= 4
        elif action == 'L':
            bearing -= value // 90
            bearing %= 4

    print(abs(x)+abs(y))


def part2(coordinates):
    x = y = 0
    wx = 10
    wy = 1
    for action, value in coordinates:
        if action == 'F':
            x += value*wx
            y += value*wy
        elif action == 'N':
            wy += value
        elif action == 'S':
            wy -= value
        elif action == 'E':
            wx += value
        elif action == 'W':
            wx -= value
        elif action == 'L':
            for _ in range(value // 90):
                wx, wy = -wy, wx
        elif action == 'R':
            for _ in range(value // 90):
                wx, wy = wy, -wx

    print(abs(x)+abs(y))


if __name__ == "__main__":
    data = get_coordinates("input/day12.data")
    part1(data)
    part2(data)
