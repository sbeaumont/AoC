#!/usr/bin/env python3

"""Solution for Advent of Code challenge 2025"""

__author__ = "Serge Beaumont"
__date__ = "December 2025"


START_POSITION = 50


def part_1(entries: list[str]):
    position_0_count = 0
    pos = START_POSITION
    for e in entries:
        pos = (pos + (int(e[1:]) if e[0] == 'R' else -int(e[1:]))) % 100
        if pos == 0:
            position_0_count += 1
    return position_0_count


def part_2(entries: list[str]):
    passed_0_count = 0
    pos = START_POSITION
    for e in entries:
        delta = int(e[1:]) if e[0] == 'R' else -int(e[1:])
        if delta > 0:
            steps_to_first_zero = 100 if pos == 0 else 100 - pos
            if delta >= steps_to_first_zero:
                passed_0_count += 1 + (delta - steps_to_first_zero) // 100
        elif delta < 0:
            steps_to_first_zero = 100 if pos == 0 else pos
            if abs(delta) >= steps_to_first_zero:
                passed_0_count += 1 + (abs(delta) - steps_to_first_zero) // 100
        else:
            print(e)
        pos = (pos + delta) % 100

    return passed_0_count


def read_puzzle_data(data_file: str) -> list:
    with open(data_file) as infile:
        return [line.strip() for line in infile.readlines()]


assertions = {
    "Test 1": 3,
    "Part 1": 1168,
    "Test 2": 6,
    "Part 2": None, # 7243 is too high
}

extra_tests = {
    "Test 2": (
        ("AoC-2025-1-test-2-input.txt", 5),
    )
}