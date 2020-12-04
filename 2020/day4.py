import re


def get_passport_data(filepath):
    with open(filepath, 'r') as f:
        passports = []
        passport = {}
        for line in f.readlines():
            if line == '\n':
                passports.append(passport)
                passport = {}
                continue
            for pair in line.strip().split(' '):
                key, value = pair.split(':')
                passport[key] = value

        # append the last one
        passports.append(passport)
    return passports


def part1(passports):
    required = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    valid = len(passports)
    for passport in passports:
        for field in required:
            if not passport.get(field):
                valid -= 1
                break
    print(valid)


def part2(passports):
    required = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    valid_passports = 0
    for passport in passports:
        v = True
        for field in required:
            if not passport.get(field):
                v = False
                break
            if not validate_fields(field, passport):
                v = False
                break
        if v:
            valid_passports += 1
    print(valid_passports)


def validate_fields(field, passport):
    if field == 'byr':
        return 1920 <= int(passport.get(field)) <= 2002
    if field == 'iyr':
        return 2010 <= int(passport.get(field)) <= 2020
    if field == 'eyr':
        return 2020 <= int(passport.get(field)) <= 2030
    if field == 'hgt':
        h = passport.get(field)
        if h[-2:] == 'cm':
            return 150 <= int(h[0:-2]) <= 193
        elif h[-2:] == 'in':
            return 59 <= int(h[0:-2]) <= 76
        else:
            return False
    if field == 'hcl':
        return re.match('#[0-9|a-f]{6}$', passport.get(field)) is not None
    if field == 'ecl':
        return passport.get(field) in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    if field == 'pid':
        return re.match('\\d{9}$', passport.get(field)) is not None
    return False


if __name__ == "__main__":
    data = get_passport_data("input/day4.data")
    part1(data)
    part2(data)
