#!/usr/bin/env python3

"""Solution for Advent of Code challenge 2020 - Day 2"""

__author__ = "Serge Beaumont"
__date__ = "December 2020"

import re


def do(filename, check_function):
    with open(filename) as infile:
        entries = [entry.replace('\n', ' ').split() for entry in infile.read().split('\n\n')]
        passports = list()
        for entry in entries:
            passport = dict()
            for field in entry:
                key, value = field.split(':')
                passport[key] = value
            passports.append(passport)

    valid_passports = 0
    for passport in passports:
        if check_function(passport):
            valid_passports += 1

    return valid_passports


def check_1(passport):
    passport_fields = set(passport.keys())
    if 'cid' in passport_fields:
        passport_fields.remove('cid')
    return passport_fields == {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}


def check_2(passport):
    def is_correct_year(field, low, high):
        return re.match(r'^\d{4}$', field) and (low <= int(field) <= high)

    if not check_1(passport):
        return False

    byr_ok = is_correct_year(passport['byr'], 1920, 2002)
    iyr_ok = is_correct_year(passport['iyr'], 2010, 2020)
    eyr_ok = is_correct_year(passport['eyr'], 2020, 2030)
    hgt_ok = False
    if re.match(r'^\d+(cm|in)$', passport['hgt']):
        height = int(passport['hgt'][:-2])
        if passport['hgt'][-2:] == 'cm':
            hgt_ok = 150 <= height <= 193
        else:
            hgt_ok = 59 <= height <= 76
    hcl_ok = re.match(r'^#[0-9a-f]{6}$', passport['hcl'])
    ecl_ok = passport['ecl'] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    pid_ok = re.match(r'^\d{9}$', passport['pid'])

    return byr_ok and iyr_ok and eyr_ok and hgt_ok and hcl_ok and ecl_ok and pid_ok


if __name__ == '__main__':
    assert do("AoC-2020-4-test-1.txt", check_1) == 2
    print("Part 1:", do("AoC-2020-4-input-1.txt", check_1))

    assert do("AoC-2020-4-test-2.txt", check_2) == 0
    assert do("AoC-2020-4-test-3.txt", check_2) == 4
    part_2 = do("AoC-2020-4-input-1.txt", check_2)
    print("Part 2:", part_2)
    assert part_2 == 121

