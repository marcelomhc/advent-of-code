import math
import re


def parse(filepath):
    with open(filepath, 'r') as f:
        tiles = {}
        for raw_tile in f.read().split('\n\n'):
            name, *lines = raw_tile.splitlines()
            num = int(name[5:-1])
            tiles[num] = [list(c) for c in lines]
    return tiles


def get_borders(tile):
    return [tile[0], tile[-1], [c[0] for c in tile], [c[-1] for c in tile]]


def find_edges(tiles):
    matches = {}
    for tile in tiles.items():
        matches[tile[0]] = match_tile(tile, tiles)
    return matches


def match_tile(tile, tiles):
    num, img = tile
    borders = get_borders(img)
    total = 0
    for border in borders:
        match = False
        for num2, tile2 in tiles.items():
            borders2 = get_borders(tile2)
            if num != num2:
                for border2 in borders2:
                    if border == border2 or border[::-1] == border2:
                        match = True
                        break
            if match:
                total += 1
                break
    return total


def get_flips(tile):
    return [tile, tile[::-1], [c[::-1] for c in tile], [c[::-1] for c in tile][::-1]]


def get_rotations(tile):
    rotations = [tile]
    last = tile
    for _ in range(3):
        tile = [c[:] for c in tile]
        for x in range(len(tile)):
            for y in range(len(tile[x])):
                tile[x][y] = last[len(tile[x])-y-1][x]
        last = tile
        rotations.append(tile)
    return rotations


def get_options(tile):
    possible = []
    for flip in get_flips(tile):
        for pos in get_rotations(flip):
            if pos not in possible:
                possible.append(pos)
    return possible


def build_img(corner_tile, tiles, dimension):
    remaining = tiles.copy()
    x = y = 0
    edge = image = []
    size = len(remaining)
    init = get_options(corner_tile)

    while len(remaining) > 0:
        if size == len(remaining):
            remaining = tiles.copy()
            x = y = 0
            image = {(x, y): init.pop()}
            edge = image[(x, y)][0]
            y += 1
        size = len(remaining)

        found = False
        for num, tile in remaining.items():
            t_options = get_options(tile)
            for option in t_options:
                if y != 0:
                    border = get_borders(option)[1]
                else:
                    border = get_borders(option)[2]
                if border == edge:
                    found = num
                    image[(x, y)] = option
                    if y == dimension - 1:
                        y = 0
                        edge = [c[-1] for c in image[(x, y)]]
                        x += 1
                    else:
                        edge = option[0]
                        y += 1
                    break
            if found:
                remaining.pop(found)
                break
    return image


def remove_borders(image):
    return {k: [c[1:-1] for c in tile[1:-1]] for k, tile in image.items()}


def merge_image(image, dim):
    img = []
    for y in range(dim, 0, -1):
        for i in range(8):
            line = []
            for x in range(dim):
                tile = image[(x, y-1)]

                line.extend(tile[i])
            img.append(line)
    return img


def find_monsters(image):
    pattern = '#....##....##....###'
    for option in get_options(image):
        matches = 0
        for i in range(len(option)):
            line = ''.join(option[i])
            if len(re.findall(pattern, line)) > 0:
                matches += len(re.findall('.#..#..#..#..#..#...', ''.join(option[i+1])))
        if matches > 0:
            hashes = 0
            for line in option:
                hashes += line.count('#')
            print(hashes - matches * 15)
            break


def evaluate_waters(tiles):
    neighbors = find_edges(tiles)
    dim = math.isqrt(len(tiles))
    current = []

    for key in neighbors:
        if neighbors[key] == 2:
            current = tiles.pop(key)
            break

    find_monsters(merge_image(remove_borders(build_img(current, tiles, dim)), dim))


if __name__ == "__main__":
    t = parse("input/day20.data")
    m = find_edges(t)
    print(math.prod([key if m[key] == 2 else 1 for key in m]))
    evaluate_waters(t)
