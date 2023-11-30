#!/usr/bin/env python3

"""Solution for Advent of Code challenge 2022 - Day X"""

__author__ = "Serge Beaumont"
__date__ = "December 2022"


def part_1(entries):
    cycles = 1
    current_score = 1
    test_cycles = (20, 60, 100, 140, 180, 220)
    tc_i = 0
    signal_strength = dict()
    for line in entries:
        next_test_cycle = test_cycles[tc_i]
        cycles += 1 if line == 'noop' else 2
        if cycles > next_test_cycle:
            # expected = (420, 1140, 1800, 2940, 2880, 3960)
            signal_strength[next_test_cycle] = next_test_cycle * current_score
            # assert signal_strength[next_test_cycle] == expected[tc_i], f"Got {signal_strength[next_test_cycle]}, expected {expected[tc_i]}"
            tc_i += 1
        if line.split()[0] == 'addx':
            current_score += int(line.split()[1])
        if tc_i >= len(test_cycles):
            break
    return sum(signal_strength.values())


def part_2(entries):
    return 0


def read_puzzle_data(file_number):
    with open(f"AoC-2022-{file_number}-input.txt") as infile:
        lines = [line.strip() for line in infile.readlines()]
    return lines


if __name__ == '__main__':
    DAY = "10"

    test_result_part_1 = part_1(read_puzzle_data(f"{DAY}-test"))
    print("Test Part 1:", test_result_part_1)
    assert test_result_part_1 == 13140, f"Expected 13140, got {test_result_part_1}"

    print("     Part 1:", part_1(read_puzzle_data(DAY)))
    #
    # test_result_part_2 = part_2(read_puzzle_data(f"{DAY}-test"))
    # print("Test Part 2:", test_result_part_2)
    # assert test_result_part_2 == 0
    #
    # result_part_2 = part_2(read_puzzle_data(DAY))
    # print("     Part 2:", result_part_2)
    # assert result_part_2 == 0