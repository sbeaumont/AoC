#!/usr/bin/env python3

"""Solution for Advent of Code challenge 2021 - Day X"""

__author__ = "Serge Beaumont"
__date__ = "December 2021"

from collections import defaultdict


LENGTH_TO_DIGIT = {2: 1, 4: 4, 3: 7, 7: 8}
ALL_SEGMENTS = {'a', 'b', 'c', 'd', 'e', 'f', 'g'}


def part_1(entries):
    digit_counts = defaultdict(int)
    for entry in entries:
        signal_patterns, outputs = entry.split('|')
        digits = outputs.strip().split()
        for digit in digits:
            digit_counts[len(digit)] += 1
    # 1 = 2s, 4 = 4s, 7 = 3s, 8 = 7s
    return sum([digit_counts[2], digit_counts[4], digit_counts[3], digit_counts[7]])


def part_2(entries):
    total_value = 0
    for entry in entries:
        signal_patterns, outputs = entry.split('|')
        patterns = signal_patterns.strip().split()
        mapping = dict()
        # Find 1, 4, 7 and 8
        for pattern in patterns:
            if len(pattern) in LENGTH_TO_DIGIT.keys():
                mapping[LENGTH_TO_DIGIT[len(pattern)]] = set(pattern)
        for pattern in patterns:
            pat_set = set(pattern)
            # Find 0, 6 and 9
            if len(pattern) == 6:
                missing_segment = (ALL_SEGMENTS - pat_set).pop()
                if missing_segment in mapping[4] and missing_segment not in mapping[1]:
                    mapping[0] = pat_set
                elif missing_segment in mapping[1]:
                    mapping[6] = pat_set
                else:
                    mapping[9] = pat_set
            # Find 2, 3 and 5
            elif len(pattern) == 5:
                if len(pat_set.intersection(mapping[4])) == 2:
                    mapping[2] = pat_set
                elif len(pat_set.intersection(mapping[1])) == 2:
                    mapping[3] = pat_set
                else:
                    mapping[5] = pat_set

        reverse_mapping = {''.join(sorted(list(pat))): digit for digit, pat in mapping.items()}
        output_digits = [''.join(sorted(v)) for v in outputs.strip().split()]
        total_value += int(''.join([str(reverse_mapping[d]) for d in output_digits]))
    return total_value


def read_puzzle_data(file_number):
    with open(f"AoC-2021-{file_number}-input.txt") as infile:
        lines = [line.strip() for line in infile.readlines()]
    return lines


if __name__ == '__main__':
    DAY = "8"

    test_result_part_1 = part_1(read_puzzle_data(f"{DAY}-test"))
    print("Test Part 1:", test_result_part_1)
    assert test_result_part_1 == 0

    print("     Part 1:", part_1(read_puzzle_data(DAY)))

    test_result_part_2 = part_2(read_puzzle_data(f"{DAY}-test"))
    print("Test Part 2:", test_result_part_2)
    assert test_result_part_2 == 5353

    test_result_part_2 = part_2(read_puzzle_data(f"{DAY}-test-2"))
    print("Test Part 2:", test_result_part_2)
    assert test_result_part_2 == 61229

    print("     Part 2:", part_2(read_puzzle_data(DAY)))
