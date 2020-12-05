def get_seats(filepath):
    with open(filepath, 'r') as f:
        seats = [(x[:-4], x[-4:-1]) for x in f.readlines()]
    return seats


def binary_str_to_int(binary_str):
    num = 0
    for i in range(len(binary_str)):
        num = num * 2
        num = num + int(binary_str[i] in ['B', 'R'])
    return num


def get_ids(seats):
    ids = []
    for row, col in seats:
        row_n = binary_str_to_int(row)
        col_n = binary_str_to_int(col)
        ids.append(row_n * 8 + col_n)
    return ids


def part1(seats):
    seats = sorted(seats, key=lambda x: x[0], reverse=True)
    ids = get_ids(seats)
    print(max(ids))


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
