def get_seats(filepath):
    with open(filepath, 'r') as f:
        seats = [(x[:-4], x[-4:-1]) for x in f.readlines()]
    return seats


def binary_str_to_int(binary_str):
    num = 0
    for char in binary_str:
        num = num*2 + int(char in ['B', 'R'])
    return num


def get_ids(seats):
    ids = []
    for row, col in seats:
        ids.append(binary_str_to_int(row) * 8 + binary_str_to_int(col))
    return ids


def part1(seats):
    print(max(get_ids(seats)))


def part2(seats):
    ids = get_ids(seats)
    ids.sort()
    for i in range(len(ids)-1):
        if abs(ids[i+1] - ids[i]) > 1:
            print((ids[i] + ids[i+1])//2)


if __name__ == "__main__":
    data = get_seats("input/day5.data")
    part1(data)
    part2(data)
