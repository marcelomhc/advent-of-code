import re


def parse_input(filepath):
    with open(filepath, "r") as f:
        return [re.search('(\d+)-(\d+) (.): (.+)', line).groups() for line in f.readlines()]


def count_valid(passwords):
    valid = 0
    for low, high, letter, password in passwords:
        if int(low) <= password.count(letter) <= int(high):
            valid += 1
    print(valid)


def match_valid(passwords):
    valid = 0
    for low, high, letter, password in passwords:
        matches = int(password[int(low) - 1] == letter) + int(password[int(high) - 1] == letter)
        if matches == 1:
            valid += 1
    print(valid)


if __name__ == "__main__":
    passwords = parse_input("input/day2.data")
    count_valid(passwords)
    match_valid(passwords)
