def parse_program(filepath):
    with open(filepath, "r") as f:
        program = []
        for line in f.readlines():
            inst, offset = line.strip().split(' ')
            program.append((inst, int(offset)))
    return program


def find_loop(program):
    acc = i = 0
    executed = set()
    while i < len(program):
        inst, offset = program[i]

        if i in executed:
            break
        executed.add(i)
        if inst == 'acc':
            acc += offset
        if inst == 'jmp':
            i += offset - 1
        i += 1

    return acc, i


def fix_loop(program):
    for i in range(len(program)):
        inst, offset = program[i]
        if inst == 'nop':
            program[i] = ('jmp', offset)
        elif inst == 'jmp':
            program[i] = ('nop', offset)
        acc, j = find_loop(program)

        if j == len(program):
            return acc

        program[i] = (inst, offset)


if __name__ == "__main__":
    data = parse_program("input/day8.data")
    accumulator, _ = find_loop(data)
    print(accumulator)
    print(fix_loop(data))
