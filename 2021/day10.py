point_table = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137,
    '(': 1,
    '[': 2,
    '{': 3,
    '<': 4
}

pairs = {
    ')': '(',
    '}': '{',
    ']': '[',
    '>': '<'
}


def find_corrupted(line):
    stack = []

    for char in line:
        if char not in pairs.keys():
            stack.append(char)
        else:
            current = stack.pop()
            if current != pairs[char]:
                return point_table[char], None

    return 0, stack


def part1(data):
    print(sum([find_corrupted(line)[0] for line in data]))


def part2(data):
    scores = list()
    for incomplete in [find_corrupted(line)[1] for line in data]:
        if incomplete:
            points = 0
            for c in incomplete[::-1]:
                points = points*5 + point_table[c]
            scores.append(points)
    print(sorted(scores)[len(scores)//2])


if __name__ == "__main__":
    with open("input/day10.data", 'r') as f:
        chunks = [line.strip() for line in f.readlines()]
    part1(chunks)
    part2(chunks)
