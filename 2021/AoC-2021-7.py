#!/usr/bin/env python3

"""Solution for Advent of Code challenge 2021 - Day 7"""

__author__ = "Serge Beaumont"
__date__ = "December 2021"

from collections import Counter
import time


def calculate_min_fuel_cost(entries, calculator):
    crab_sub_positions = Counter(entries)

    min_fuel = sum(entries) * (max(entries) - min(entries))
    for x in range(min(entries), max(entries) + 1):
        fuel_cost = 0
        for pos, amount in crab_sub_positions.items():
            fuel_cost += calculator(pos, x, amount)
        if fuel_cost < min_fuel:
            min_fuel = fuel_cost

    return min_fuel


def part_1(entries):
    def part_1_calculator(pos, x, amount):
        return abs(pos - x) * amount

    return calculate_min_fuel_cost(entries, part_1_calculator)


def part_2(entries):
    fuel_cost_by_distance = [i for i in range(max(entries) - min(entries) + 1)]

    def part_2_calculator(pos, x, amount):
        return sum(fuel_cost_by_distance[:abs(pos - x) + 1]) * amount

    return calculate_min_fuel_cost(entries, part_2_calculator)


def read_puzzle_data(file_number):
    with open(f"AoC-2021-{file_number}-input.txt") as infile:
        lines = [[int(c) for c in line.strip().split(',')] for line in infile.readlines()]
    return lines[0]


if __name__ == '__main__':
    start = time.time()
    DAY = "7"

    test_result_part_1 = part_1(read_puzzle_data(f"{DAY}-test"))
    print("Test Part 1:", test_result_part_1)
    assert test_result_part_1 == 37

    print("     Part 1:", part_1(read_puzzle_data(DAY)))

    test_result_part_2 = part_2(read_puzzle_data(f"{DAY}-test"))
    print("Test Part 2:", test_result_part_2)
    assert test_result_part_2 == 168

    print("     Part 2:", part_2(read_puzzle_data(DAY)))

    print(f"\n{time.time() - start:.4f} seconds to run.")
