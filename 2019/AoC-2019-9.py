#!/usr/bin/env python3

"""Solution for Advent of Code challenge 2019 - Day X"""

__author__ = "Serge Beaumont"
__date__ = "December 2019"

from intcode_computer import Computer


def load_input(day):
    with open(f"AoC-2019-input-{day}.txt") as infile:
        return [int(y) for y in infile.read().strip().split(',')]


def do(program, input_values=[]):
    computer = Computer(program, debug=False)
    computer.run_program(input_values)
    return computer.output


if __name__ == '__main__':
    # Run tests
    test1 = do([109, 1, 204, -1, 1001, 100, 1, 100, 1008, 100, 16, 101, 1006, 101, 0, 99])
    assert test1 == [109, 1, 204, -1, 1001, 100, 1, 100, 1008, 100, 16, 101, 1006, 101, 0,
                     99], f"Test 1 output: {test1}"

    test2 = do([1102, 34915192, 34915192, 7, 4, 7, 99, 0])
    assert len(str(test2[0])) == 16, f"Test 2 output: {test2}"

    test3 = do([104, 1125899906842624, 99])
    assert test3[0] == 1125899906842624, f"Test 3 output: {test3}"

    # Part 1
    result = do(load_input(9), [1])
    print(f"Part 1: {result}")

    # Part 2
    result = do(load_input(9), [2])
    print(f"Part 2: {result}")
