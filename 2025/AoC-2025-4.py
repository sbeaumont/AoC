"""
Solution for Advent of Code challenge 2025

1.
"""

__author__ = "Serge Beaumont"
__date__ = "December 2025"

from os import access

import numpy as np
from aoc.utils import neighbors8


def init_neighbor_counts(entries: list[str]):
    max_x = len(entries[0])
    max_y = len(entries)
    neighbor_counts = np.zeros((max_x, max_y))
    for y in range(max_y):
        for x in range(max_x):
            if entries[y][x] == "@":
                neighbors = [n for n in neighbors8((x, y)) if (0 <= n[0] <= max_x - 1) and (0 <= n[1] <= max_y - 1)]
                for n in neighbors:
                    neighbor_counts[n[0], n[1]] += 1
    return neighbor_counts


def accessible_rolls(entries: list[str], neighbor_counts):
    max_x = len(entries[0])
    max_y = len(entries)
    accessible_rolls = list()
    for y in range(max_y):
        for x in range(max_x):
            if (entries[y][x] == "@") and (neighbor_counts[x, y] < 4):
                accessible_rolls.append((x, y))
    return accessible_rolls


def remove_accessible_rolls(entries: list[str], neighbor_counts, accessible_rolls):
    """In-place removal of accessible rolls"""
    max_x = len(entries[0])
    max_y = len(entries)
    for r_x, r_y in accessible_rolls:
        entries[r_y][r_x] = "."
        neighbors = [n for n in neighbors8((r_x, r_y)) if (0 <= n[0] <= max_x - 1) and (0 <= n[1] <= max_y - 1)]
        for n in neighbors:
            neighbor_counts[n[0], n[1]] -= 1


def part_1(entries: list[str]):
    neighbor_counts = init_neighbor_counts(entries)
    return len(accessible_rolls(entries, neighbor_counts))


def part_2(entries: list[str]):
    neighbor_counts = init_neighbor_counts(entries)
    accessible = accessible_rolls(entries, neighbor_counts)
    total_removed = len(accessible)
    while len(accessible) > 0:
        remove_accessible_rolls(entries, neighbor_counts, accessible)
        accessible = accessible_rolls(entries, neighbor_counts)
        total_removed += len(accessible)
    return total_removed


def read_puzzle_data(data_file: str) -> list:
    with open(data_file) as infile:
        return [[c for c in line.strip()] for line in infile.readlines()]


assertions = {
    "Test 1": 13,
    "Part 1": 1516,
    "Test 2": 43,
    "Part 2": 9122,
}
