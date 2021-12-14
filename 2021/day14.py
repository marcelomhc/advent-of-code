from collections import Counter, defaultdict


def parse_input(filename):
    with open(filename, 'r') as f:
        polymer = f.readline().strip()
        f.readline()
        instructions = dict()
        for line in f.readlines():
            template, result = line.strip().split(' -> ')
            instructions[template] = result
        return polymer, instructions


# Brute force
def part1(polymer, instructions):
    for _ in range(10):
        new_polymer = polymer[0]
        for i in range(1, len(polymer)):
            new_polymer += instructions.get(polymer[i-1:i+1], '') + polymer[i]
        polymer = new_polymer

    collection = Counter(polymer).values()
    print(max(collection) - min(collection))


# Count pairs
def part2(polymer, instructions):
    frequency = defaultdict(int)
    for i in range(1, len(polymer)):
        frequency[polymer[i-1:i+1]] = 1

    for _ in range(40):
        insert = defaultdict(int)
        for pair, count in frequency.items():
            insert[pair[0] + instructions[pair]] += count
            insert[instructions[pair] + pair[1]] += count
            insert[pair] -= count

        for pair, count in insert.items():
            frequency[pair] += count

    letters = defaultdict(float)
    letters[polymer[0]] = 0.5
    letters[polymer[-1]] = 0.5
    for pair, count in frequency.items():
        letters[pair[0]] += count/2
        letters[pair[1]] += count/2
    print(int(max(letters.values())-min(letters.values())))


if __name__ == '__main__':
    p, r = parse_input("input/day14.data")
    part1(p, r)
    part2(p, r)
