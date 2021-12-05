#!/usr/bin/env python3

"""Solution for Advent of Code challenge 2021 - Day 3"""

__author__ = "Serge Beaumont"
__date__ = "December 2021"

from statistics import mode
from collections import Counter


def part_1(entries):
    gamma_bits = [mode(bits) for bits in zip(*entries)]
    epsilon_bits = ['0' if e == '1' else '1' for e in gamma_bits]
    gamma = int(''.join(gamma_bits), 2)
    epsilon = int(''.join(epsilon_bits), 2)
    return gamma * epsilon


def part_2(entries):
    def most_common(entry):
        ctr = Counter(entry)
        return '1' if ctr['1'] >= ctr['0'] else '0'

    def least_common(entry):
        ctr = Counter(entry)
        return '0' if ctr['0'] <= ctr['1'] else '1'

    i = 0
    o_g_entries = list(entries)
    while len(o_g_entries) > 1:
        most_common_bits = [most_common(e) for e in zip(*o_g_entries)]
        o_g_entries = [e for e in o_g_entries if e[i] == most_common_bits[i]]
        i += 1
    oxygen_generator_rating = int(o_g_entries[0], 2)

    j = 0
    c02_entries = list(entries)
    while len(c02_entries) > 1:
        least_common_bits = [least_common(e) for e in zip(*c02_entries)]
        c02_entries = [e for e in c02_entries if e[j] == least_common_bits[j]]
        j += 1
    co2_scrubber_rating = int(c02_entries[0], 2)

    return oxygen_generator_rating * co2_scrubber_rating


def read_puzzle_data(file_number):
    with open(f"AoC-2021-{file_number}-input.txt") as infile:
        lines = [line.strip() for line in infile.readlines()]
    return lines


if __name__ == '__main__':
    DAY = "3"

    test_result_part_1 = part_1(read_puzzle_data(f"{DAY}-test"))
    print("Test Part 1", test_result_part_1)
    assert test_result_part_1 == 198

    print("Part 1", part_1(read_puzzle_data(DAY)))

    test_result_part_2 = part_2(read_puzzle_data(f"{DAY}-test"))
    print("Test Part 2", test_result_part_2)
    assert test_result_part_2 == 230

    print("Part 2", part_2(read_puzzle_data(DAY)))
