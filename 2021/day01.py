def part1(data):
    increase = [1 for x in range(1, len(data)) if data[x] > data[x-1]]
    print(sum(increase))


def part2(data):
    windows = [data[x] + data[x-1] + data[x-2] for x in range(2, len(data))]
    part1(windows)


if __name__ == "__main__":
    with open("input/day01.data", 'r') as f:
        input_data = list(map(int, [x for x in f.readlines()]))
    part1(input_data)
    part2(input_data)
