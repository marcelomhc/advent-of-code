def get_dots(filename):
    with open(filename, 'r') as f:
        dots, instructions = f.read().split('\n\n')
        dots = set([tuple(map(int, x.split(','))) for x in dots.split('\n')])
        instructions = [instruction[11:].split('=') for instruction in instructions.split('\n')]
        return dots, instructions


def print_code(dots):
    max_x = max(dots, key=lambda l: l[0])[0]
    max_y = max(dots, key=lambda l: l[1])[1]

    for y in range(max_y+1):
        for x in range(max_x+1):
            if (x, y) in dots:
                print('#', end='')
            else:
                print(' ', end='')
        print('')


def folding_step(dots, line, orientation):
    line = int(line)
    folded_dots = set()
    for x, y in dots:
        if orientation == 'x' and x > line:
            x = line * 2 - x
        elif orientation == 'y' and y > line:
            y = line * 2 - y
        folded_dots.add((x, y))
    return folded_dots


def part1(dots, instructions):
    for orientation, line in instructions:
        print(len(folding_step(dots, line, orientation)))
        return


def part2(dots, instructions):
    for orientation, line in instructions:
        dots = folding_step(dots, line, orientation)
    print_code(dots)


if __name__ == "__main__":
    positions, folding = get_dots("input/day13.data")
    part1(positions, folding)
    part2(positions, folding)
