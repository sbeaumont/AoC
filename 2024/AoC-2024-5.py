#!/usr/bin/env python3

"""Solution for Advent of Code challenge 2024"""

__author__ = "Serge Beaumont"
__date__ = "December 2024"

from collections import defaultdict

def condense_rules(rules):
    result = defaultdict(list)
    for rule in rules:
        result[rule[0]].append(rule[1])
    return result

def find_updates(cd, updates, correct=True):
    result = list()
    for e in updates:
        rule_broken = False
        for page_index in range(len(e)):
            page_nr = e[page_index]
            rule_indexes = [e.index(Y) for Y in cd[page_nr] if Y in e]
            if (len(rule_indexes) > 0) and (min(rule_indexes) < page_index):
                rule_broken = True
                break
        if (correct and not rule_broken) or (not correct and rule_broken):
            result.append(e)
    return result

def find_correct_updates(cd, updates):
    return find_updates(cd, updates, correct=True)

def find_incorrect_updates(cd, updates):
    return find_updates(cd, updates, correct=False)

def calculate_score(updates):
    total = 0
    for e in updates:
        middle_index = int(len(e) / 2)
        total += e[middle_index]
    return total

def part_1(rules: list, entries: list[list]):
    # all_page_numbers_in_rules = {x for xs in rules for x in xs}
    updates = find_correct_updates(condense_rules(rules), entries)
    return calculate_score(updates)


def part_2(rules: list, entries: list[list]):
    cd = condense_rules(rules)
    updates = find_incorrect_updates(cd, entries)
    corrected_updates = list()
    for update in updates:
        reordered = list()
        for page in update:
            if (len(reordered) == 0) or (set(reordered) - set(cd[page]) == set(reordered)):
                reordered.append(page)
            else:
                rule_indexes = [reordered.index(Y) for Y in cd[page] if Y in reordered]
                reordered.insert(min(rule_indexes), page)
        corrected_updates.append(reordered)
    return calculate_score(corrected_updates)


def read_puzzle_data(file_number):
    with open(f"AoC-2024-{file_number}-input.txt") as infile:
        lines = infile.readlines()
        empty_line_index = lines.index("\n")

        rule_lines = [line.strip().split('|') for line in lines[:empty_line_index]]
        rules = [(int(line[0]), int(line[1])) for line in rule_lines]

        update_lines = [line.strip().split(',') for line in lines[empty_line_index+1:]]
        updates = [[int(n) for n in line] for line in update_lines]

        return rules, updates


if __name__ == '__main__':
    puzzle_number = int(__file__.split('.')[0].split('-')[-1])
    print(f"Day {puzzle_number}")

    test_result = part_1(*read_puzzle_data(f"{puzzle_number}-test"))
    print("Test 1:", test_result)
    assert test_result == 143

    print("Part 1:", part_1(*read_puzzle_data(puzzle_number)))

    test_result_2 = part_2(*read_puzzle_data(f"{puzzle_number}-test"))
    print("Test 2:", test_result_2)
    assert test_result_2 == 123

    print("Part 2:", part_2(*read_puzzle_data(puzzle_number)))
