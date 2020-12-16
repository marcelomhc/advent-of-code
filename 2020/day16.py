import re


def parse(filepath):
    with open(filepath, 'r') as f:
        line = f.readline()
        rules = {}
        while line != '\n':
            field, l1, h1, l2, h2 = re.match('(.*): (\\d+)-(\\d+) or (\\d+)-(\\d+)', line).groups()
            rules[field] = [(int(l1), int(h1)), (int(l2), int(h2))]
            line = f.readline()

        # My ticket
        f.readline()
        my_ticket = [num for num in map(int, f.readline().strip().split(','))]

        # nearby tickets
        f.readline()
        f.readline()
        nearby_tickets = [[field for field in map(int, line.strip().split(','))] for line in f.readlines()]
        return rules, my_ticket, nearby_tickets


def find_range(rules):
    range_list = [item for sublist in rules.values() for item in sublist]
    range_list.sort()
    low, high = range_list.pop(0)
    for l1, h1 in range_list:
        if l1 < low <= h1:
            low = l1
        if h1 > high >= l1:
            high = h1
    return low, high


def filter_tickets(tickets, rules):
    filtered = []
    total = 0
    low, high = find_range(rules)
    for ticket in tickets:
        filtered.append(ticket)
        for field in ticket:
            if not low <= field <= high:
                total += field
                filtered.pop(-1)
                break
    print(total)
    return filtered


def result(my_ticket, fields):
    total = 1
    for key in fields.keys():
        if key.startswith('departure'):
            total *= my_ticket[fields[key]]
    return total


def find_fields(rules, tickets, my_ticket):
    by_field = [*map(list, zip(*tickets))]
    fields = {}

    while len(rules) > 0:
        for i in range(len(by_field)):
            opt = rules.copy()
            for rule in rules:
                (l1, h1), (l2, h2) = rules[rule]
                for num in by_field[i]:
                    if not (l1 <= num <= h1 or l2 <= num <= h2):
                        opt.pop(rule)
                        break
            if len(opt) == 1:
                for r in opt.keys():
                    rules.pop(r)
                    fields[r] = i
                break

    print(result(my_ticket, fields))


if __name__ == "__main__":
    ranges, my, nearby = parse("input/day16.data")
    valid = filter_tickets(nearby, ranges)
    find_fields(ranges, valid, my)
