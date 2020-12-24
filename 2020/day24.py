from collections import defaultdict


def parse():
    with open('input/day24.data', 'r') as f:
        instructions = []
        for line in f.readlines():
            instruction = []
            i = 0
            while i < len(line.strip()):
                dy = 0
                dx = 2
                if line[i] == 'n' or line[i] == 's':
                    dy = 1 if line[i] == 'n' else -1
                    dx = 1
                    i += 1
                instruction.append((dx, dy) if line[i] == 'e' else (-dx, dy))
                i += 1
            instructions.append(instruction)
        return instructions


def flip(instructions):
    flipped = defaultdict(bool)
    for instruction in instructions:
        dx, dy = map(sum, zip(*instruction))
        flipped[(dx, dy)] = not flipped[(dx, dy)]
    print(sum(map(int, flipped.values())))
    return flipped


def get_adjacent(tile):
    x, y = tile
    return [(x+dx, y+dy) for dx, dy in [(-1, 1), (1, 1), (-2, 0), (2, 0), (-1, -1), (1, -1)]]


def should_flip(is_black, neighbors):
    return (is_black and (neighbors == 0 or neighbors > 2)) or ((not is_black) and neighbors == 2)


def exhibit(tiles, rounds):
    for _ in range(rounds):
        neighbors = defaultdict(int)
        for tile in tiles:
            if tiles.get(tile, False):
                for adjacent in get_adjacent(tile):
                    neighbors[adjacent] = neighbors[adjacent] + 1
        for tile in set().union(*[neighbors, tiles]):
            tiles[tile] = not tiles[tile] if should_flip(tiles[tile], neighbors[tile]) else tiles[tile]
    print(sum(map(int, tiles.values())))


if __name__ == "__main__":
    inst = parse()
    initial = flip(inst)
    exhibit(initial, 100)
