#!/usr/bin/env python3

"""Solution for Advent of Code challenge 2021 - Day 6"""

__author__ = "Serge Beaumont"
__date__ = "December 2021"

from collections import Counter, defaultdict


def calculate_generations(entries, nr_of_generations):
    generation = Counter(entries)
    for i in range(nr_of_generations):
        new_generation = defaultdict(int)
        for age, amount in generation.items():
            if age == 0:
                new_generation[8] += amount
                new_generation[6] += amount
            else:
                new_generation[age - 1] += amount
        generation = new_generation
    return sum(generation.values())


def read_puzzle_data(file_number):
    with open(f"AoC-2021-{file_number}-input.txt") as infile:
        lines = [[int(c) for c in line.strip().split(',')] for line in infile.readlines()]
    return lines[0]


if __name__ == '__main__':
    DAY = "6"
    NR_OF_GENERATIONS_PART_1 = 80
    NR_OF_GENERATIONS_PART_2 = 256

    test_result_part_1 = calculate_generations(read_puzzle_data(f"{DAY}-test"), 18)
    print("Test Part 1 (18):", test_result_part_1)
    assert test_result_part_1 == 26

    test_result_part_1 = calculate_generations(read_puzzle_data(f"{DAY}-test"), NR_OF_GENERATIONS_PART_1)
    print("Test Part 1 (80):", test_result_part_1)
    assert test_result_part_1 == 5934

    print("     Part 1:", calculate_generations(read_puzzle_data(DAY), NR_OF_GENERATIONS_PART_1))

    test_result_part_2 = calculate_generations(read_puzzle_data(f"{DAY}-test"), NR_OF_GENERATIONS_PART_2)
    print("Test Part 2:", test_result_part_2)
    assert test_result_part_2 == 26984457539

    print("     Part 2:", calculate_generations(read_puzzle_data(DAY), NR_OF_GENERATIONS_PART_2))
