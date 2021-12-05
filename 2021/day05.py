import re


def part1(data):
    find_overlaps(data)


def part2(data):
    find_overlaps(data, True)


def find_overlaps(data, count_diagonals=False):
    diagram = {}
    for x1, y1, x2, y2 in data:
        dx = 1 if x2 >= x1 else -1
        dy = 1 if y2 >= y1 else -1

        if x1 == x2 or y1 == y2:
            for x in range(x1, x2 + dx, dx):
                for y in range(y1, y2 + dy, dy):
                    diagram[(x, y)] = diagram.get((x, y), 0) + 1
        elif count_diagonals:
            for x, y in zip(range(x1, x2 + dx, dx), range(y1, y2 + dy, dy)):
                diagram[(x, y)] = diagram.get((x, y), 0) + 1
    print(sum([1 if x > 1 else 0 for x in diagram.values()]))


if __name__ == "__main__":
    with open("input/day05.data", 'r') as f:
        vents = [list(map(int, d)) for d in (re.findall(r'(\d+)+', x) for x in f.readlines())]
    part1(vents)
    part2(vents)
