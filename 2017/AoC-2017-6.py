#!/usr/bin/env python3

"""Solution for Advent of Code challenge 2017

[Memory Reallocation](http://adventofcode.com/2017/day/6)"""

__author__ = "Serge Beaumont"
__date__ = "December 2017"

PUZZLE_INPUT = "10	3	15	10	5	15	5	15	9	2	5	8	5	2	3	6"


def input_to_list(input_string):
    return [int(bank) for bank in input_string.split()]


def redistribute(banks):
    highest_bank_index = banks.index(max(banks))
    blocks = banks[highest_bank_index]
    banks[highest_bank_index] = 0
    for i in range(1, blocks + 1):
        banks[(highest_bank_index + i) % len(banks)] += 1


def find_first_duplicate_redistribution(initial_banks):
    banks = initial_banks
    configurations = set()
    redistributions = 0
    while len(configurations) == redistributions:
        redistributions += 1
        highest_bank_index = banks.index(max(banks))
        blocks = banks[highest_bank_index]
        banks[highest_bank_index] = 0
        for i in range(1, blocks + 1):
            banks[(highest_bank_index + i) % len(banks)] += 1
        configurations.add(str(banks))

    print("It took {} redistributions to get a duplicate.".format(redistributions))

    return banks


def find_reoccurrence_of(initial_banks):
    banks = list(initial_banks)
    redistribute(banks)
    redistributions = 1
    while initial_banks != banks:
        redistributions += 1
        redistribute(banks)

    print("It took {} redistributions to get a duplicate.".format(redistributions))

    return banks


if __name__ == '__main__':
    print("Test...")
    find_first_duplicate_redistribution(input_to_list("0 2 7 0"))
    print("Part 1...")
    first_round = find_first_duplicate_redistribution(input_to_list(PUZZLE_INPUT))
    print("Part 2...")
    print("Part 1 distribution was {}".format(first_round))
    second_round = find_reoccurrence_of(first_round)
    print("Part 2 distribution was {}".format(second_round))
