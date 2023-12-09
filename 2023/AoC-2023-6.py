#!/usr/bin/env python3

"""Solution for Advent of Code challenge 2023 - Day 6"""

__author__ = "Serge Beaumont"
__date__ = "December 2023"

import sys
from math import prod


def ways_to_win(time, distance):
    wins = 0
    for t in range(1, time):
        if ((time - t) * t) > distance:
            wins += 1
    return wins


def part_1(entries):
    def parse_data(entries):
        times = [int(e) for e in entries[0].split()[1:]]
        distances = [int(e) for e in entries[1].split()[1:]]
        return list(zip(times, distances))

    races = parse_data(entries)
    wins = list()
    for time, distance in races:
        wins.append(ways_to_win(time, distance))
    return prod(wins)


def part_2(entries):
    def parse_data(entries):
        time = int(entries[0].split(':')[1].replace(' ', ''))
        distance = int(entries[1].split(':')[1].replace(' ', ''))
        return time, distance

    time, distance = parse_data(entries)
    return ways_to_win(time, distance)


def read_puzzle_data(file_number):
    with open(f"AoC-2023-{file_number}-input.txt") as infile:
        lines = [line.strip() for line in infile.readlines()]
    return lines


if __name__ == '__main__':
    DAY = sys.argv[0].split('.')[0].split('-')[-1]
    print("Results for day", DAY)

    test_result_part_1 = part_1(read_puzzle_data(f"{DAY}-test"))
    print("Test Part 1:", test_result_part_1)
    assert test_result_part_1 == 288

    print("     Part 1:", part_1(read_puzzle_data(DAY)))

    test_result_part_2 = part_2(read_puzzle_data(f"{DAY}-test"))
    print("Test Part 2:", test_result_part_2)
    assert test_result_part_2 == 71503

    result_part_2 = part_2(read_puzzle_data(DAY))
    print("     Part 2:", result_part_2)
    assert result_part_2 == 38220708