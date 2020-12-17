#!/usr/bin/env python3

"""Solution for Advent of Code challenge 2020 - Day 16"""

__author__ = "Serge Beaumont"
__date__ = "December 2020"

from itertools import chain


def do(filename):
    with open(filename) as infile:
        line = infile.readline().strip()
        rules = dict()
        while line != '':
            field, ranges = line.split(':')
            range_list = [rng for rng in ranges.split(' or ')]
            rules[field] = [[int(n) for n in r.split('-')] for r in range_list]
            line = infile.readline().strip()

        infile.readline()  # Skip the headline
        infile.readline()  # Skip my ticket
        infile.readline()  # Skip empty line
        infile.readline()  # Skip headline
        tickets = [[int(n) for n in line.split(',')] for line in infile.readlines()]

    # print("Rules:    ", rules)
    # print("My Ticket:", my_ticket)
    # print("Tickets:  ", tickets)

    # The sort guarantees that the low values are in order from low to high
    flattened_ranges = sorted(list(chain(*[ranges for ranges in rules.values()])))
    merged_ranges = list()
    merged_ranges.append(flattened_ranges[0].copy())
    for low, high in flattened_ranges[1:]:
        if merged_ranges[-1][1] + 1 < low:
            # This range's low leaves a gap with the existing highest
            merged_ranges.append([low, high])
        elif merged_ranges[-1][1] + 1 >= low:
            # This range's low is connecting or overlapping with the last merged range's high
            # So extend the last merged range to the highest of the two.
            merged_ranges[-1][1] = max(merged_ranges[-1][1], high)

    invalid_numbers = list()
    for i in range(1, len(merged_ranges)):
        for j in range(merged_ranges[i-1][1] + 1, merged_ranges[i][0]):
            invalid_numbers.append(j)
    lowest = merged_ranges[0][0]
    highest = merged_ranges[-1][1]

    error_rate = sum([field for field in chain(*tickets) if (field < lowest) or (field > highest) or (field in invalid_numbers)])

    return error_rate


if __name__ == '__main__':
    assert do("AoC-2020-16-test-1.txt") == 71
    result = do("AoC-2020-16-input.txt")
    print("Part 1:", result)
    assert result == 25984

