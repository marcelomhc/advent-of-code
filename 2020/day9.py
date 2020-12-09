def parse_program(filepath):
    with open(filepath, "r") as f:
        program = [x for x in map(int, f.readlines())]
    return program


def find_failure(numbers, size):
    for i in range(size, len(numbers)):
        preamble = numbers[i - size:i]
        preamble.sort()
        if not find_sum(preamble, numbers[i]):
            return numbers[i]


def find_sum(preamble, num):
    if len(preamble) == 1:
        return False

    total = preamble[0] + preamble[-1]

    if total == num:
        return True
    elif total < num:
        return find_sum(preamble[1:], num)
    else:
        return find_sum(preamble[:-1], num)


def find_weakness(numbers, failed):
    low = high = 0
    while high <= len(numbers):
        if sum(numbers[low:high]) < failed:
            high += 1
        elif sum(numbers[low:high]) > failed:
            low += 1
        else:
            return max(numbers[low:high]) + min(numbers[low:high])
    return -1


if __name__ == "__main__":
    data = parse_program("input/day9.data")
    failure = find_failure(data, 25)
    print(failure)
    print(find_weakness(data, failure))
