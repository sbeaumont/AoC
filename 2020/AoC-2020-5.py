#!/usr/bin/env python3

"""Solution for Advent of Code challenge 2020 - Day 5"""

__author__ = "Serge Beaumont"
__date__ = "December 2020"

with open(f"AoC-2020-5-input.txt") as infile:
    boarding_passes = [line.strip() for line in infile.readlines()]
    # print(boarding_passes)


def seat(boarding_pass):
    def binary_search(to_search, high_code, high):
        low = 0
        for c in to_search:
            half_size = (high - low + 1) // 2
            if c == high_code:
                low += half_size
            else:
                high -= half_size
        return low

    low_row = binary_search(boarding_pass[:7], 'B', 127)
    low_column = binary_search(boarding_pass[7:], 'R', 7)

    return low_row, low_column, low_row * 8 + low_column


def find_seat(passes):
    seat_ids = sorted([seat(p)[2] for p in passes])
    # print(seat_ids)
    for i in range(1, len(seat_ids) - 1):
        if seat_ids[i] + 1 != seat_ids[i+1]:
            print(f"Part 2: seat ID {seat_ids[i] + 1} is missing.")


if __name__ == '__main__':
    assert seat('FBFBBFFRLR') == (44, 5, 357), f"Got {seat('FBFBBFFRLR')}"
    assert seat('BFFFBBFRRR') == (70, 7, 567), f"Got {seat('BFFFBBFRRR')}"
    assert seat('FFFBBBFRRR') == (14, 7, 119), f"Got {seat('FFFBBBFRRR')}"
    assert seat('BBFFBBFRLL') == (102, 4, 820), f"Got {seat('BBFFBBFRLL')}"

    highest_seat_id = max([seat(p)[2] for p in boarding_passes])
    print("Part 1: highest seat ID is", highest_seat_id)
    assert highest_seat_id == 832

    find_seat(boarding_passes)
