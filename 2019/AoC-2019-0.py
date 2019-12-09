#!/usr/bin/env python3

"""Solution for Advent of Code challenge 2019 - Day X"""

__author__ = "Serge Beaumont"
__date__ = "December 2019"


def load_input(day):
    with open(f"AoC-2019-input-{day}.txt") as infile:
        return [[int(y) for y in x.split(',')] for x in infile.readlines()]


def do(data):
    return False


if __name__ == '__main__':
    # Run tests
    assert do(data)

    # Load data
    data = load_input(0)
    print(data)

    # Solve puzzle
    result = do(data)

    # Output
    print(f"Part 1: {data}")
