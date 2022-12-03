#!/usr/bin/env python3

"""Solution for Advent of Code challenge 2022 - Day 1"""

__author__ = "Serge Beaumont"
__date__ = "December 2022"


def calories_per_elf(entries):
    calory_totals = list()
    current_total = 0
    for food_item in entries:
        if not food_item:
            calory_totals.append(current_total)
            current_total = 0
        else:
            current_total += int(food_item.strip())
    return calory_totals


def part_1(entries):
    return max(calories_per_elf(entries))


def part_2(entries):
    calory_totals = calories_per_elf(entries)
    calory_totals.sort(reverse=True)
    print(calory_totals[:3])
    return sum(calory_totals[:3])


def read_puzzle_data(file_number):
    with open(f"AoC-2022-{file_number}-input.txt") as infile:
        return [line.strip() for line in infile.readlines()]


test_result = part_1(read_puzzle_data("1-test"))
print("Test:", test_result)
assert test_result == 24000

print("Part 1:", part_1(read_puzzle_data(1)))
print("Part 2:", part_2(read_puzzle_data(1)))
assert part_2(read_puzzle_data(1)) > 136610
