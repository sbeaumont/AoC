#!/usr/bin/env python3

"""Solution for Advent of Code challenge 2023 - Day 14"""

__author__ = "Serge Beaumont"
__date__ = "December 2023"

import sys
import itertools
from collections import Counter


def find_cycle(list_of_numbers, x0: int=0):
    c1 = Counter(list_of_numbers)
    c2 = Counter(c1.values())
    print(c2)
    max_nrs = 0
    max_reps = 0
    for reps, nrs in c2.items():
        if nrs > max_nrs:
            max_reps = reps
    g1 = {}
    g2 = {}
    g3 = {}
    for reps, nrs in c2.items():
        if max_reps - 5 <= reps <= max_reps + 5:
            g1[reps] = nrs
        elif reps < max_reps - 5:
            g2[reps] =  nrs
        else:
            g3[reps] = nrs
    return g1, g2, g3

def transpose(list_of_lists):
    transposed = list(map(list, zip(*list_of_lists)))
    return [''.join(line) for line in transposed]

def rotate(list_of_lists):
    transposed = transpose(list_of_lists)
    rotated = [l[::-1] for l in transposed]
    return rotated
    # rotated_list = []
    # for x in range(len(list_of_lists[0])):
    #     rotated_list.append(''.join([list_of_lists[y][x] for y in range(len(list_of_lists))]))
    # return rotated_list



def north_load(columns, direction):
    def column_weight(column):
        total = 0
        max_weight = len(column)
        for i in range(len(column)):
            total += max_weight - i if column[i] == 'O' else 0
        return total

    def roll(column):
        rolled_column = []
        for part in column.split('#'):
            boulders_in_part = part.count('O')
            rolled_part = 'O' * boulders_in_part + '.' * part.count('.')
            rolled_column.append(rolled_part)
        return '#'.join(rolled_column)

    rolled_columns = [roll(c) for c in columns]

    # Orient north, calculate weight and print.
    rotated_n = rolled_columns
    correction = [0, 3, 2, 1]
    for _ in range(correction[direction]):
        rotated_n = rotate(rotated_n)
    total = 0
    for c in rotated_n:
        total += column_weight(c)
    #     print(c, column_weight(c))
    # print(total)
    # print('---')

    return total, rolled_columns


def part_1(entries):
    total, rolled = north_load(transpose(entries))
    return total


def part_2(entries):
    def cycle(entries):
        direction = 0
        for _ in range(4):
            total, entries = north_load(entries, direction)
            entries = rotate(entries)
            direction += 1
        return total, entries

    totals = []
    entries = transpose(entries)
    entries = entries[::-1]
    for i in range(10000):
        total, entries = cycle(entries)
        if total in totals:
            totals.append(total)
            # break
        else:
            totals.append(total)

    counter = find_cycle(totals)

    return counter


def read_puzzle_data(file_number):
    with open(f"AoC-2023-{file_number}-input.txt") as infile:
        lines = [line.strip() for line in infile.readlines()]
    return lines


if __name__ == '__main__':
    DAY = sys.argv[0].split('.')[0].split('-')[-1]
    # print("Results for day", DAY)
    #
    # test_result_part_1 = part_1(read_puzzle_data(f"{DAY}-test"))
    # print("Test Part 1:", test_result_part_1)
    # assert test_result_part_1 == 136
    #
    # print("     Part 1:", part_1(read_puzzle_data(DAY)))

    test_result_part_2 = part_2(read_puzzle_data(f"{DAY}-test"))
    print("Test Part 2:", test_result_part_2)
    # assert test_result_part_2 == 0
    #
    result_part_2 = part_2(read_puzzle_data(DAY))
    print("     Part 2:", result_part_2)
    # assert result_part_2 == 0