#!/usr/bin/env python3

"""Solution for Advent of Code challenge 2021 - Day 11"""

__author__ = "Serge Beaumont"
__date__ = "December 2021"


def neighbors8(point):
    """The eight neighbors (with diagonals)."""
    x, y = point
    return ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1),
            (x + 1, y + 1), (x - 1, y - 1), (x + 1, y - 1), (x - 1, y + 1))


def flash(entries, coord, flashed):
    flashed.append(coord)
    for n in neighbors8(coord):
        nx, ny = n
        if 0 <= nx < len(entries[0]) and 0 <= ny < len(entries):
            entries[ny][nx] += 1
            if entries[ny][nx] > 9 and n not in flashed:
                flash(entries, n, flashed)


def do_step(entries):
    # Increase all
    entries = [[e + 1 for e in line] for line in entries]
    # Cascade flashes
    flashed = list()
    for y in range(len(entries)):
        for x in range(len(entries[0])):
            if entries[y][x] > 9 and (x, y) not in flashed:
                flash(entries, (x, y), flashed)
    # Set flashed to 0
    entries = [[0 if e > 9 else e for e in line] for line in entries]
    return entries, len(flashed)


def part_1(entries):
    flashes = 0
    for i in range(100):
        entries, flashed = do_step(entries)
        flashes += flashed
    return flashes


def part_2(entries):
    step = 1
    while True:
        entries, flashed = do_step(entries)
        if flashed == 100:
            return step
        step += 1


def read_puzzle_data(file_number):
    with open(f"AoC-2021-{file_number}-input.txt") as infile:
        lines = [[int(c) for c in line.strip()] for line in infile.readlines()]
    return lines


if __name__ == '__main__':
    DAY = "11"

    test_result_part_1 = part_1(read_puzzle_data(f"{DAY}-test"))
    print("Test Part 1:", test_result_part_1)
    assert test_result_part_1 == 1656

    print("     Part 1:", part_1(read_puzzle_data(DAY)))

    test_result_part_2 = part_2(read_puzzle_data(f"{DAY}-test"))
    print("Test Part 2:", test_result_part_2)
    assert test_result_part_2 == 195

    print("     Part 2:", part_2(read_puzzle_data(DAY)))
