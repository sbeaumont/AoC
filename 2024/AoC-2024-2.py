#!/usr/bin/env python3

"""Solution for Advent of Code challenge 2024"""

__author__ = "Serge Beaumont"
__date__ = "December 2024"


def get_differences(report):
    differences = list()
    for i in range(len(report) - 1):
        differences.append(report[i + 1] - report[i])
    return differences


def check_differences(differences):
    if all(n > 0 for n in differences) or all(n < 0 for n in differences):
        for d in range(len(differences)):
            if abs(differences[d]) < 1 or abs(differences[d]) > 3:
                return False
    else:
        return False
    return True


def check_differences_with_dampener(report, trace=False):
    if trace:
        print(report)
    if check_differences(get_differences(report)):
        return True

    for i in range(len(report)):
        new_report = report[:i] + report[i+1:]
        if trace:
            print(new_report)
        if check_differences(get_differences(new_report)):
            return True

    return False

def part_1(entries: list[str]):
    total = 0
    for e in entries:
        total += 1 if check_differences(get_differences(e)) else 0
    return total


def part_2(entries: list[str], trace=False):
    total = 0
    for e in entries:
        total += 1 if check_differences_with_dampener(e, trace) else 0
    return total


def read_puzzle_data(file_number):
    with open(f"AoC-2024-{file_number}-input.txt") as infile:
        return [[int(level) for level in line.strip().split()] for line in infile.readlines()]


if __name__ == '__main__':
    puzzle_number = int(__file__.split('.')[0].split('-')[-1])
    print(f"Day {puzzle_number}")

    test_result = part_1(read_puzzle_data(f"{puzzle_number}-test"))
    print("Test 1:", test_result)
    assert test_result == 2

    print("Part 1:", part_1(read_puzzle_data(puzzle_number)))
    assert part_1(read_puzzle_data(puzzle_number)) == 524

    test_result_2 = part_2(read_puzzle_data(f"{puzzle_number}-test"))
    print("Test 2:", test_result_2)
    assert test_result_2 == 5

    print("Part 2:", part_2(read_puzzle_data(puzzle_number), trace=False))
