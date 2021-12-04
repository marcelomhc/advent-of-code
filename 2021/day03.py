def part1(report):
    common = [0 for _ in range(len(report[0]))]
    for number in report:
        for pos in range(len(number)):
            common[pos] += int(number[pos])

    total = len(report)
    epsilon = gamma = ''
    for count in common:
        epsilon += str(int(count > total/2))
        gamma += str(int(count < total/2))

    print(int(epsilon, 2)*int(gamma, 2))


def part2(report):
    oxygen = get_measure(report)
    co2 = get_measure(report, False)

    print(oxygen * co2)


def get_measure(report, most_common=True):
    for pos in range(len(report[0])):
        report = sorted(report, reverse=True)
        digits = sum([int(d[pos]) for d in report])
        if most_common:
            report = report[:digits] if digits >= len(report) / 2 else report[digits:]
        else:
            report = report[:digits] if digits < len(report) / 2 else report[digits:]
        if len(report) == 1:
            break
    return int(report[0], 2)


if __name__ == "__main__":
    with open("input/day03.data", 'r') as f:
        input_data = [x.strip() for x in f.readlines()]
    part1(input_data)
    part2(input_data)
