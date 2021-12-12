def dfs(cave_paths, path, cave='start', dup=False):
    paths = 0
    if cave not in path or not cave.islower() or (dup and 'dup' not in path):
        if dup and cave in path and cave.islower():
            path.append('dup')
        else:
            path.append(cave)

        if cave == 'end':
            return 1
        for neighbor in cave_paths[cave]:
            current_path = [c for c in path]
            paths += dfs(cave_paths, current_path, neighbor, dup)
    return paths


def part1(data):
    print(dfs(data, []))


def part2(data):
    print(dfs(data, [], dup=True))


def create_graph(filename):
    with open(filename, 'r') as f:
        paths = dict()
        for line in f.readlines():
            cave1, cave2 = line.strip().split('-')
            if cave2 != 'start':
                paths.setdefault(cave1, list()).append(cave2)
            if cave1 != 'start':
                paths.setdefault(cave2, list()).append(cave1)
        paths.pop('end')
        return paths


if __name__ == "__main__":
    graph = create_graph("input/day12.data")
    part1(graph)
    part2(graph)
