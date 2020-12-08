import re


def parse_rules(filepath):
    with open(filepath, 'r') as f:
        bags = {}
        contain = {}
        for line in f.readlines():
            bag, inside = line.strip().split(' bags contain ')
            bags[bag] = []
            if inside == 'no other bags.':
                continue
            colors = [(int(c[0]), c[2:]) for c in re.split('\\sbag[s]?[,|.]\\s?', inside)[:-1]]

            bags[bag] += colors
            [contain.setdefault(color, []).append(bag) for _, color in colors]
    return contain, bags


def get_bags(rules, bag):
    bags = set()
    for c in rules.get(bag, []):
        bags.add(c)
        bags.update(get_bags(rules, c))
    return bags


def count_inside(rules, bag):
    if len(rules[bag]) == 0:
        return 0
    total = 0
    for qty, color in rules.get(bag):
        total += count_inside(rules, color) * qty + qty
    return total


if __name__ == "__main__":
    wrappers, content = parse_rules("input/day7.data")
    print(len(get_bags(wrappers, 'shiny gold')))
    print(count_inside(content, 'shiny gold'))
