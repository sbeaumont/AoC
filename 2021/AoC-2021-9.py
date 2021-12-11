#!/usr/bin/env python3

"""Solution for Advent of Code challenge 2021 - Day 9"""

__author__ = "Serge Beaumont"
__date__ = "December 2021"

from math import prod


def max_point(entries):
    return len(entries[0]), len(entries)


def neighbors4(point, max_pt):
    """The four neighbors (without diagonals)."""
    x, y = point
    max_x, max_y = max_pt
    all_neighbors = [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]
    return [c for c in all_neighbors if (0 <= c[0] < max_x) and (0 <= c[1] < max_y)]


def heights(coord, entries):
    x, y = coord
    height_at_coord = int(entries[y][x])
    other_heights = [int(entries[c[1]][c[0]]) for c in neighbors4(coord, max_point(entries))]
    return height_at_coord, other_heights


def low_points(entries):
    result = dict()
    for y in range(len(entries)):
        for x in range(len(entries[0])):
            height_at_coord, hghts = heights((x, y), entries)
            if height_at_coord < min(hghts):
                result[(x, y)] = height_at_coord
    return result


def flood_fill(entries, visited, coord):
    if int(entries[coord[1]][coord[0]]) == 9:
        return
    visited.append(coord)
    for c in neighbors4(coord, max_point(entries)):
        if not c in visited:
            flood_fill(entries, visited, c)


def part_1(entries):
    return sum([h + 1 for h in low_points(entries).values()])


def part_2(entries):
    """Flood fill from all low points"""
    basin_sizes = list()
    for coord, height in low_points(entries).items():
        visited = list()
        flood_fill(entries, visited, coord)
        basin_sizes.append(len(visited))
    return prod(sorted(basin_sizes)[-3:])


def read_puzzle_data(file_number):
    with open(f"AoC-2021-{file_number}-input.txt") as infile:
        lines = [line.strip() for line in infile.readlines()]
    return lines


if __name__ == '__main__':
    DAY = "9"

    test_result_part_1 = part_1(read_puzzle_data(f"{DAY}-test"))
    print("Test Part 1:", test_result_part_1)
    assert test_result_part_1 == 15

    print("     Part 1:", part_1(read_puzzle_data(DAY)))

    test_result_part_2 = part_2(read_puzzle_data(f"{DAY}-test"))
    print("Test Part 2:", test_result_part_2)
    assert test_result_part_2 == 1134

    print("     Part 2:", part_2(read_puzzle_data(DAY)))
