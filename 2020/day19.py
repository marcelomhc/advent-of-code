import re


def parse(filepath):
    with open(filepath, 'r') as f:
        rules = {}
        line = f.readline()
        lines = f.readlines()
        while line != '\n':
            key, matches = line.strip().split(': ')
            rules[int(key)] = [eval(part) if part != "|" else part for part in matches.split(' ')]
            line = lines.pop(0)
    return rules, lines


def get_pattern(rules, idx):
    rule = rules[idx]
    pattern = ''
    for k in rule:
        if k == 'a' or k == 'b':
            return k
        pattern += get_pattern(rules, k) if isinstance(k, int) else k
    return '(' + pattern + ')' if pattern.find('|') else pattern


def count_matches(rules, messages, r):
    pattern = get_pattern(rules, r) + '$'
    matches = 0
    for msg in messages:
        matches += 1 if re.match(pattern, msg.strip()) else 0
    print(matches)


def fix_message(rules, message, r):
    rules[8] = [42, '+']
    rules[11] = [42, 31,
                 '|', 42, 42, 31, 31,
                 '|', 42, 42, 42, 31, 31, 31,
                 '|', 42, 42, 42, 42, 31, 31, 31, 31,
                 '|', 42, 42, 42, 42, 42, 31, 31, 31, 31, 31]
    count_matches(rules, message, r)


if __name__ == "__main__":
    rule_dict, msgs = parse("input/day19.data")
    count_matches(rule_dict, msgs, 0)
    fix_message(rule_dict, msgs, 0)
