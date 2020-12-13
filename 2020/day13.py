def get_buses(filepath):
    with open(filepath, 'r') as f:
        departure = int(f.readline())
        buses = [((int(bus) - i) % int(bus), int(bus)) for i, bus in enumerate(f.readline().split(',')) if bus != 'x']
    return departure, buses


def wait_time(timetable):
    departure, buses = timetable
    min_t = total = departure
    for _, bus in buses:
        if departure % bus == 0:
            return 0
        wait = bus - (departure % bus)
        if wait < min_t:
            min_t = wait
            total = bus * wait
    print(total)


def contest(timetable):
    _, buses = timetable
    buses.sort(key=lambda l: l[1], reverse=True)
    total, step = buses.pop(0)

    for remainder, mod in buses:
        while total % mod != remainder:
            total += step
        step *= mod
    print(total)


if __name__ == "__main__":
    data = get_buses("input/day13.data")
    wait_time(data)
    contest(data)
