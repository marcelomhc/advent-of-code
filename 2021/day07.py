def part1(position):
    position.sort()
    median = position[len(position) // 2]

    ans = 0
    for pos in position:
        ans += abs(pos-median)
    print(ans)


def part2(position):
    mean = round(sum(position)/len(position)) - 1
    ans = 0

    for pos in position:
        ans += sum([i+1 for i in range(abs(pos-mean))])
    print(ans)


if __name__ == "__main__":
    with open("input/day07.data", 'r') as f:
        crabs = list(map(int, f.readline().split(',')))
    part1(crabs)
    part2(crabs)
