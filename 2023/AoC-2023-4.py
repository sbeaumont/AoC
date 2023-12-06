#!/usr/bin/env python3

"""Solution for Advent of Code challenge 2023 - Day X"""

__author__ = "Serge Beaumont"
__date__ = "December 2023"

import sys
from collections import defaultdict


def find_matches(e) -> int:
    winning, my = e.split(':')[1].split('|')
    winning = [int(n) for n in winning.split()]
    my = [int(n) for n in my.split()]
    return len(list(set(winning) & set(my)))


def part_1(entries):
    total = 0
    for e in entries:
        matches = find_matches(e)
        if matches > 0:
            total += 1 * pow(2, matches - 1)
    return total


def part_2(entries):
    cards = defaultdict(int)
    last_card_nr = int(entries[-1].split(':')[0].split()[1])
    for e in entries:
        card_nr = int(e.split(':')[0].split()[1])
        cards[card_nr] += 1
        matches = find_matches(e)
        for i in range(card_nr + 1, card_nr + 1 + matches):
            if i <= last_card_nr:
                cards[i] += cards[card_nr]
    return sum(cards.values())


def read_puzzle_data(file_number):
    with open(f"AoC-2023-{file_number}-input.txt") as infile:
        lines = [line.strip() for line in infile.readlines()]
    return lines


if __name__ == '__main__':
    DAY = sys.argv[0].split('.')[0].split('-')[-1]
    print("Results for day", DAY)

    test_result_part_1 = part_1(read_puzzle_data(f"{DAY}-test"))
    print("Test Part 1:", test_result_part_1)
    assert test_result_part_1 == 13

    result_part_1 = part_1(read_puzzle_data(DAY))
    print("     Part 1:", result_part_1)
    assert result_part_1 == 15205

    test_result_part_2 = part_2(read_puzzle_data(f"{DAY}-test"))
    print("Test Part 2:", test_result_part_2)
    assert test_result_part_2 == 30

    result_part_2 = part_2(read_puzzle_data(DAY))
    print("     Part 2:", result_part_2)
    assert result_part_2 == 6189740