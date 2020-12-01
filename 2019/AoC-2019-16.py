#!/usr/bin/env python3

"""Solution for Advent of Code challenge 2019 - Day 16"""

__author__ = "Serge Beaumont"
__date__ = "December 2019"


BASE_PATTERN = (0, 1, 0, -1)


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
    test('80871224585914546619083218645595', '24176176')
    test('19617804207202209144916044189917', '73745418')
    test('69317163492948606335995924319873', '52432133')

    # Check data
    print(f"Input data: {load_input(16)}\n")

    # Solve puzzle
    result = do(load_input(16))

    # Output
    print(f"Part 1: {result}")
