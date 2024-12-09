#!/usr/bin/env python3

"""Solution for Advent of Code challenge 2024"""

__author__ = "Serge Beaumont"
__date__ = "December 2024"

import re


def transpose(entries):
    transposed = list()
    for x in range(len(entries[0])):
        vertical_line = list()
        for y in range(len(entries)):
            vertical_line.append(entries[y][x])
        transposed.append(''.join(vertical_line))
    return transposed


def rotate_left(entries):
    rotated = list()
    for x in range(len(entries[0])-1, -1, -1):
        line = list()
        for y in range(len(entries)):
            line.append(entries[y][x])
        rotated.append(''.join(line))
    return rotated


def scan_horizontal(entries):
    total = 0
    pattern = r'(?=(XMAS)|(SAMX))'
    for e in entries:
        total += len(re.findall(pattern, e))
    return total


def transpose_diagonal(entries):
    # print(entries)
    diagonals = list()
    # Along top row
    for x in range(len(entries[0])):
        y = 0
        line = list()
        for x_sub in range(x, len(entries[0])):
            line.append(entries[y][x_sub])
            y += 1
        diagonals.append(''.join(line))
    # Along left column, skip 0 (no duplicate)
    for y in range(1, len(entries)):
        x = 0
        line = list()
        for y_sub in range(y, len(entries)):
            line.append(entries[y_sub][x])
            x += 1
        diagonals.append(''.join(line))
    return diagonals


def part_1(entries: list[str]):
    total = 0
    total += scan_horizontal(entries)
    total += scan_horizontal(transpose(entries))
    total += scan_horizontal(transpose_diagonal(entries))
    total += scan_horizontal(transpose_diagonal(rotate_left(entries)))
    return total


def part_2(entries: list[str]):
    ms_sets = (
        ('M', 'M', 'S', 'S'),
        ('S', 'M', 'M', 'S'),
        ('S', 'S', 'M', 'M'),
        ('M', 'S', 'S', 'M'),
    )

    total = 0
    for x in range(1, len(entries[0])-1):
        for y in range(1, len(entries)-1):
            if entries[y][x] == 'A':
                x_neighbours = (entries[y-1][x-1], entries[y-1][x+1], entries[y+1][x+1], entries[y+1][x-1])
                if x_neighbours in ms_sets:
                    total += 1
    return total


def read_puzzle_data(data_file: str) -> list:
    with open(data_file) as infile:
        return [line.strip() for line in infile.readlines()]


assertions = {
    "Test 1": 18,
    "Part 1": 2390,
    "Test 2": 9,
    "Part 2": 1809
}
