def parse_input(filepath):
    with open(filepath, "r") as f:
        adapters = [x for x in map(int, f.readlines())]
    return adapters


def get_diffs(adapters):
    adapters.append(0)
    adapters.append(max(adapters) + 3)
    adapters.sort()
    diffs = [0 for _ in range(3)]
    for i in range(1, len(adapters)):
        diffs[adapters[i] - adapters[i-1] - 1] += 1
    print(diffs[0]*diffs[2])


def count_comb(adapters):
    options = [1, 2, 3]

    arrangements = [0 for _ in range(max(adapters)+1)]
    arrangements[0] = 1
    adapters.sort()
    for adapter in adapters:
        for option in options:
            if adapter-option >= 0:
                arrangements[adapter] += arrangements[adapter-option]
    print(arrangements[-1])


if __name__ == "__main__":
    data = parse_input("input/day10.data")
    get_diffs(data)
    count_comb(data)
