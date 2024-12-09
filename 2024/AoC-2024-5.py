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

def part_1(puzzle_data: list):
    rules, entries = puzzle_data
    # all_page_numbers_in_rules = {x for xs in rules for x in xs}
    updates = find_correct_updates(condense_rules(rules), entries)
    return calculate_score(updates)


def part_2(puzzle_data: list):
    rules, entries = puzzle_data
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


def read_puzzle_data(data_file: str):
    with open(data_file) as infile:
        lines = infile.readlines()
        empty_line_index = lines.index("\n")

        rule_lines = [line.strip().split('|') for line in lines[:empty_line_index]]
        rules = [(int(line[0]), int(line[1])) for line in rule_lines]

        update_lines = [line.strip().split(',') for line in lines[empty_line_index+1:]]
        updates = [[int(n) for n in line] for line in update_lines]

        return rules, updates


assertions = {
    "Test 1": 143,
    "Part 1": None,
    "Test 2": 123,
    "Part 2": None
}
