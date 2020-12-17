#!/usr/bin/env python3

"""Solution for Advent of Code challenge 2020 - Day 3"""

__author__ = "Serge Beaumont"
__date__ = "December 2020"


def do(filename, right, down, verbose=False):
    with open(filename) as infile:
        forest = [list(line.strip()) for line in infile.readlines()]
        num_lines = len(forest)
        line_length = len(forest[0])

    x = y = trees = 0
    while y < num_lines:
        if forest[y][x] == '#':
            forest[y][x] = 'X'
            trees += 1
        else:
            forest[y][x] = 'O'
        x = (x + right) % line_length
        y += down

    if verbose:
        for line in forest:
            print(''.join(line))
        print("Number of trees hit", trees)

    return trees


if __name__ == '__main__':
    assert do("AoC-2020-3-test-1.txt", 3, 1, True) == 7
    hit31 = do("AoC-2020-3-input.txt", 3, 1)
    print("Part 1:", hit31)
    hit11 = do("AoC-2020-3-input.txt", 1, 1)
    hit51 = do("AoC-2020-3-input.txt", 5, 1)
    hit71 = do("AoC-2020-3-input.txt", 7, 1)
    hit12 = do("AoC-2020-3-input.txt", 1, 2)
    print("Part 2:", hit11 * hit31 * hit51 * hit71 * hit12)

