#!/usr/bin/env python3

"""
Solution for Advent of Code challenge 2019 - Day 5 part 2

Full Intcode computer version
"""

__author__ = "Serge Beaumont"
__date__ = "December 2019"

from intcode_computer import Computer


def solve():
    diagnostic_code_1 = Computer.from_file("AoC-2019-input-5.txt").run_program([1])
    print("Part 1:", diagnostic_code_1)
    assert diagnostic_code_1 == 11049715

    diagnostic_code_2 = Computer.from_file("AoC-2019-input-5.txt").run_program([5])
    print("Part 2:", diagnostic_code_2)
    assert diagnostic_code_2 == 2140710


if __name__ == '__main__':
    solve()
