#!/usr/bin/env python3

"""Solution for Advent of Code challenge 2020 - Day 15"""

__author__ = "Serge Beaumont"
__date__ = "December 2020"

from collections import defaultdict

puzzle_input = [16, 11, 15, 0, 1, 7]
tests = [[[0, 3, 6], 436], [[1, 3, 2], 1], [[2, 1, 3], 10], [[1, 2, 3], 27], [[2, 3, 1], 78], [[3, 2, 1], 438], [[3, 1, 2], 1836]]


def do(starting_list: list, iterations=2020):
    nr_dict = defaultdict(list)
    last_spoken = starting_list[-1]
    for i, n in enumerate(starting_list):
        nr_dict[n].append(i)
    for i in range(len(starting_list), iterations):
        if len(nr_dict[last_spoken]) == 1:
            nr_dict[0].append(i)
            last_spoken = 0
        else:
            diff_nr = nr_dict[last_spoken][-1] - nr_dict[last_spoken][-2]
            nr_dict[diff_nr].append(i)
            last_spoken = diff_nr
    return last_spoken


if __name__ == '__main__':
    for test in tests:
        test_result = do(test[0])
        assert test_result == test[1], f"Input {test[0]}, expected {test[1]}, got {test_result}"
    print("Part 1:", do(puzzle_input))
    print("Part 2:", do(puzzle_input, 30000000))
