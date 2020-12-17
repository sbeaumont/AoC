#!/usr/bin/env python3

"""Solution for Advent of Code challenge 2020 - Day 16"""

__author__ = "Serge Beaumont"
__date__ = "December 2020"

from itertools import chain
from math import prod
from collections import defaultdict


def load(filename, verbose=False):
    with open(filename) as infile:
        line = infile.readline().strip()
        rules = dict()
        while line != '':
            field, ranges = line.split(':')
            range_list = [rng for rng in ranges.split(' or ')]
            rules[field] = [[int(n) for n in r.split('-')] for r in range_list]
            line = infile.readline().strip()

        infile.readline()  # Skip the headline
        my_ticket = [int(n) for n in infile.readline().split(',')]
        infile.readline()  # Skip empty line
        infile.readline()  # Skip headline
        tickets = [[int(n) for n in line.split(',')] for line in infile.readlines()]

    if verbose:
        print("Rules:    ", rules)
        print("My Ticket:", my_ticket)
        print("Tickets:  ", tickets)

    return rules, my_ticket, tickets


def merge_rules(rules):
    # The sort guarantees that the low values are in order from low to high
    flattened_ranges = sorted(list(chain(*[ranges for ranges in rules.values()])))
    # Weird copy construct to ensure that the original first range doesn't get changed.
    merged_ranges = list()
    merged_ranges.append(flattened_ranges[0].copy())
    for low, high in flattened_ranges[1:]:
        if merged_ranges[-1][1] + 1 < low:
            # This range's low leaves a gap with the existing highest, add it as a new range
            merged_ranges.append([low, high])
        elif merged_ranges[-1][1] + 1 >= low:
            # This range's low is connecting or overlapping with the last merged range's high
            # So extend the last merged range to the highest of the two.
            merged_ranges[-1][1] = max(merged_ranges[-1][1], high)

    # invert the valid ranges for easy matching later
    invalid_numbers = list()
    for i in range(1, len(merged_ranges)):
        for j in range(merged_ranges[i-1][1] + 1, merged_ranges[i][0]):
            invalid_numbers.append(j)
    lowest = merged_ranges[0][0]
    highest = merged_ranges[-1][1]

    return lowest, highest, invalid_numbers


def find_valid_tickets(rules, tickets):
    lowest, highest, invalid_numbers = merge_rules(rules)

    def is_valid_ticket(ticket):
        for field in ticket:
            if (field < lowest) or (field > highest) or (field in invalid_numbers):
                return False
        return True

    return [t for t in tickets if is_valid_ticket(t)]


def find_field_names(rules, valid_tickets):
    field_values = {i: [ticket[i] for ticket in valid_tickets] for i in range(len(valid_tickets[0]))}

    # Some fields will match multiple rules, collect all matches.
    field_order = defaultdict(list)
    for pos, fv in field_values.items():
        for name, ranges in rules.items():
            low1, high1 = ranges[0]
            low2, high2 = ranges[1]
            valid_values = [v for v in fv if (low1 <= v <= high1) or (low2 <= v <= high2)]
            if valid_values == fv:
                field_order[pos].append(name)

    # By now we have fields that match multiple rules, some have a unique rule-field match.
    # Remove the rule matches from all other fields if a field matches a single rule
    # Keep cycling until all field-rule matches are unique
    while len(list(chain(*field_order.values()))) != len(field_values):
        unique_matches = [v[0] for k, v in field_order.items() if len(field_order[k]) == 1]
        for k, v in field_order.items():
            if len(v) > 1:
                field_order[k] = [name for name in v if (name not in unique_matches)]

    # Change from 0: ['name'] to 0: 'name' for easy processing elsewhere
    field_order = {k: v[0] for k, v in field_order.items()}

    return field_order


def do(filename):
    rules, my_ticket, tickets = load(filename)
    valid_tickets = find_valid_tickets(rules, tickets)
    valid_tickets.append(my_ticket)
    field_names = find_field_names(rules, valid_tickets)

    departure_fields = list()
    for i in range(len(my_ticket)):
        if field_names[i].startswith('departure'):
            departure_fields.append(my_ticket[i])

    # print("Valid Tickets:   ", valid_tickets)
    # print("Field Names:     ", field_names)
    # print("Departure Fields:", departure_fields)

    return prod(departure_fields)


if __name__ == '__main__':
    do("AoC-2020-16-test-2.txt")
    result = do("AoC-2020-16-input.txt")
    print("Part 2:", result)
    assert result == 1265347500049
