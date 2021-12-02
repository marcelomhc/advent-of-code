def part1(data):
    horizontal = depth = 0
    for (direction, steps) in data:
        if direction == 'forward':
            horizontal += steps
        elif direction == 'up':
            depth -= steps
        else:
            depth += steps
    print(horizontal*depth)


def part2(data):
    horizontal = depth = aim = 0
    for (direction, steps) in data:
        if direction == 'forward':
            horizontal += steps
            depth += aim * steps
        elif direction == 'up':
            aim -= steps
        else:
            aim += steps
    print(horizontal*depth)


if __name__ == "__main__":
    with open("input/day02.data", 'r') as f:
        input_data = [(d, int(n)) for (d, n) in [x.strip().split(' ') for x in f.readlines()]]
    part1(input_data)
    part2(input_data)
