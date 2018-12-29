#!/usr/bin/env python3

"""Solution for Advent of Code challenge 2018 - Day X part 1"""

__author__ = "Serge Beaumont"
__date__ = "December 2018"

import time


def load_file(file_name):
    with open(file_name) as infile:
        data = ([line.strip() for line in infile])
    return data


def do(file_name):
    data = load_file(file_name)

    print(data)


if __name__ == "__main__":
    start = time.time()

    do("AoC-2018-X-input.txt")

    print(f"{time.time() - start:.4f} seconds to run.")
