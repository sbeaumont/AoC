#!/usr/bin/env python3

"""Solution for Advent of Code challenge 2019 - Day X"""

__author__ = "Serge Beaumont"
__date__ = "December 2019"


def load_input(day):
    with open(f"AoC-2019-input-{day}.txt") as infile:
        return [[int(y) for y in x.strip().split(',')] for x in infile.readlines()]


def do(data):
    return data


def test(test_data, expected):
    test_result = do(test_data)
    assert test_result == expected, f"Expected {expected} but got {test_result}"


if __name__ == '__main__':
    # Run tests
    test('testdata', 'testdata')

    # Check data
    print(f"Input data: {load_input(0)}\n")

    # Solve puzzle
    result = do(load_input(0))

    # Output
    print(f"Part 1: {result}")
