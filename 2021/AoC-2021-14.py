#!/usr/bin/env python3

"""Solution for Advent of Code challenge 2021 - Day 14"""

__author__ = "Serge Beaumont"
__date__ = "December 2021"

from collections import Counter, defaultdict


def create_polymer(entries, steps):
    """Naive list insert method"""
    polymer_template, pair_insertion_rules = entries

    polymer = list(polymer_template)
    for i in range(steps):
        new_polymer = polymer.copy()
        for j in range(len(polymer) - 2, -1, -1):
            pair = ''.join(polymer[j:j+2])
            if pair in pair_insertion_rules:
                new_polymer.insert(j + 1, pair_insertion_rules[pair])
        polymer = new_polymer

    element_counter = Counter(polymer).most_common()

    return element_counter[0][1] - element_counter[-1][1]


def create_polymer_2(entries, steps):
    """Slightly better append method"""
    polymer_template, pair_insertion_rules = entries

    polymer = list(polymer_template)
    for i in range(steps):
        print("Step:", i+1)
        new_polymer = list()
        for j in range(len(polymer)):
            pair = ''.join(polymer[j:j+2])
            new_polymer.append(pair[0])
            if pair in pair_insertion_rules:
                new_polymer.append(pair_insertion_rules[pair])
        polymer = new_polymer

    element_counter = Counter(polymer).most_common()

    return element_counter[0][1] - element_counter[-1][1]


def create_polymer_3(entries, steps):
    """Smartypants method. Count pairs and elements"""
    polymer_template, pair_insertion_rules = entries

    # Initialize pair count
    pairs = defaultdict(int)
    for i in range(len(polymer_template) - 1):
        pairs[polymer_template[i:i+2]] += 1

    # Initialize element count
    element_count = defaultdict(int)
    for e in polymer_template:
        element_count[e] += 1

    for i in range(steps):
        new_pairs = defaultdict(int)
        for pair in list(pairs.keys()):
            if pair in pair_insertion_rules:
                insert_element = pair_insertion_rules[pair]
                element_count[insert_element] += pairs[pair]
                new_pairs[pair[0] + insert_element] += pairs[pair]
                new_pairs[insert_element + pair[1]] += pairs[pair]
            else:
                new_pairs[pair] = pairs[pair]
        pairs = new_pairs

    max_count = max(element_count.values())
    min_count = min(element_count.values())

    return max_count - min_count


def read_puzzle_data(file_number):
    with open(f"AoC-2021-{file_number}-input.txt") as infile:
        lines = [line.strip() for line in infile.readlines()]
        polymer_template = lines[0]
        pair_insertion_rules = {line.split(' ->')[0]: line.split(' -> ')[1] for line in lines[2:]}
    return polymer_template, pair_insertion_rules


if __name__ == '__main__':
    DAY = "14"

    test_result_part_1 = create_polymer_3(read_puzzle_data(f"{DAY}-test"), 10)
    print("Test Part 1:", test_result_part_1)
    assert test_result_part_1 == 1588

    print("     Part 1:", create_polymer_3(read_puzzle_data(DAY), 10))

    test_result_part_2 = create_polymer_3(read_puzzle_data(f"{DAY}-test"), 40)
    print("Test Part 2:", test_result_part_2)
    assert test_result_part_2 == 2188189693529

    print("     Part 2:", create_polymer_3(read_puzzle_data(DAY), 40))
