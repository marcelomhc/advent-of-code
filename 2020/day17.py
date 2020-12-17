def parse3d(filepath):
    with open(filepath, "r") as f:
        z = 0
        grid = {}
        lines = f.readlines()
        for y in range(len(lines)):
            for x in range(len(lines[y])):
                if lines[y][x] == '#':
                    grid[(x, y, z)] = 1

    return grid


def parse4d(filepath):
    with open(filepath, "r") as f:
        z = w = 0
        grid = {}
        lines = f.readlines()
        for y in range(len(lines)):
            for x in range(len(lines[y])):
                if lines[y][x] == '#':
                    grid[(x, y, z, w)] = 1

    return grid


def part1(cubes, cycles):
    for _ in range(cycles):
        neighbors = {}
        for x, y, z in cubes.keys():
            for i in [-1, 0, 1]:
                for j in [-1, 0, 1]:
                    for k in [-1, 0, 1]:
                        count = neighbors.get((x+i, y+j, z+k), 0)
                        neighbors[(x+i, y+j, z+k)] = count + 1
            neighbors[(x, y, z)] -= 1
        new_cubes = {}
        for position in neighbors.keys():
            if neighbors[position] == 3:
                new_cubes[position] = 1
            elif neighbors[position] == 2 and cubes.get(position, 0) == 1:
                new_cubes[position] = 1
        cubes = new_cubes
    print(sum(cubes.values()))


def part2(cubes, cycles):
    for _ in range(cycles):
        neighbors = {}
        for x, y, z, w in cubes.keys():
            for i in [-1, 0, 1]:
                for j in [-1, 0, 1]:
                    for k in [-1, 0, 1]:
                        for m in [-1, 0, 1]:
                            count = neighbors.get((x+i, y+j, z+k, w+m), 0)
                            neighbors[(x+i, y+j, z+k, w+m)] = count + 1
            neighbors[(x, y, z, w)] -= 1
        new_cubes = {}
        for position in neighbors.keys():
            if neighbors[position] == 3:
                new_cubes[position] = 1
            elif neighbors[position] == 2 and cubes.get(position, 0) == 1:
                new_cubes[position] = 1
        cubes = new_cubes
    print(sum(cubes.values()))


if __name__ == "__main__":
    part1(parse3d("input/day17.data"), 6)
    part2(parse4d("input/day17.data"), 6)
