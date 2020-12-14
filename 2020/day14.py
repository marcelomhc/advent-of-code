def get_buses(filepath):
    with open(filepath, 'r') as f:
        program = []
        for line in f.readlines():
            inst, value = line.strip().split(' = ')
            if inst == 'mask':
                program.append((-1, value))
            else:
                program.append((int(inst[4:-1]), int(value)))

    return program


def part1(program):
    mem = {}
    or_mask = and_mask = 0
    for inst, value in program:
        if inst == -1:
            or_mask, and_mask = int(value.replace('X', '0'), 2), int(value.replace('X', '1'), 2)
        else:
            mem[inst] = (value & and_mask) | or_mask

    print(sum(mem.values()))


def get_floating(mask: str):
    pos = []
    rev = ''.join(reversed(mask))
    for i in range(len(rev)):
        if rev[i] == 'X':
            pos.append(pow(2, i))
    return pos


def part2(program):
    mem = {}
    floating = []
    mask = ''

    for inst, value in program:
        if inst == -1:
            mask = int(value.replace('X', '1'), 2)
            floating = get_floating(value)
        else:
            addresses = [(inst | mask)]
            for position in floating:
                addresses += [address & ~position for address in addresses]

            for address in addresses:
                mem[address] = value

    print(sum(mem.values()))


if __name__ == "__main__":
    data = get_buses("input/day14.data")
    part1(data)
    part2(data)
