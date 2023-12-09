#!/usr/bin/env python3

"""Solution for Advent of Code challenge 2023 - Day 5"""

__author__ = "Serge Beaumont"
__date__ = "December 2023"

import sys

def parse_data(entries):
    seeds = [int(e) for e in entries[0].split(':')[1].split()]
    mappings = dict()
    current_mapping = None
    for e in entries[1:]:
        if len(e.strip()) == 0:
            continue
        if e[0].isalpha():
            current_mapping = e.split()[0]
            mappings[current_mapping] = list()
        else:
            mappings[current_mapping].append([int(n) for n in e.split()])
    return seeds, mappings


def map_seed(seed, mappings):
    def map_item(source, mapping):
        for m in mapping:
            if m[1] <= source <= (m[1] + m[2]):
                return m[0] + source - m[1]
        return source

    soil = map_item(seed, mappings['seed-to-soil'])
    fertilizer = map_item(soil, mappings['soil-to-fertilizer'])
    water = map_item(fertilizer, mappings['fertilizer-to-water'])
    light = map_item(water, mappings['water-to-light'])
    temperature = map_item(light, mappings['light-to-temperature'])
    humidity = map_item(temperature, mappings['temperature-to-humidity'])
    location = map_item(humidity, mappings['humidity-to-location'])
    return location


def reverse_map_seed(location, mappings):
    def reverse_map_item(destination, mapping):
        for m in mapping:
            if m[0] <= destination <= (m[0] + m[2]):
                return m[1] + destination - m[0]
        return destination

    humidity = reverse_map_item(location, mappings['humidity-to-location'])
    temperature = reverse_map_item(humidity, mappings['temperature-to-humidity'])
    light = reverse_map_item(temperature, mappings['light-to-temperature'])
    water = reverse_map_item(light, mappings['water-to-light'])
    fertilizer = reverse_map_item(water, mappings['fertilizer-to-water'])
    soil = reverse_map_item(fertilizer, mappings['soil-to-fertilizer'])
    seed = reverse_map_item(soil, mappings['seed-to-soil'])
    return seed


def part_1(entries):
    seeds, mappings = parse_data(entries)
    locations = dict()
    for seed in seeds:
        locations[seed] = map_seed(seed, mappings)
    return min(locations.values())


def part_2(entries):
    # This solution sort-of brute forces: takes a while to run from 0 upwards.
    # Better than the forward solution, though.
    seeds, mappings = parse_data(entries)
    seed_ranges = [(seeds[i], seeds[i + 1]) for i in range(0, len(seeds), 2)]
    location = 0
    result = None
    while not result:
        if location % 1000000 == 0:
            print(f"Location {location}")
        seed = reverse_map_seed(location, mappings)
        for sr in seed_ranges:
            if sr[0] <= seed <= sr[0] + sr[1]:
                return location
        location += 1
    return None


def read_puzzle_data(file_number):
    with open(f"AoC-2023-{file_number}-input.txt") as infile:
        lines = [line.strip() for line in infile.readlines()]
    return lines


if __name__ == '__main__':
    DAY = sys.argv[0].split('.')[0].split('-')[-1]
    print("Results for day", DAY)

    test_result_part_1 = part_1(read_puzzle_data(f"{DAY}-test"))
    print("Test Part 1:", test_result_part_1)
    assert test_result_part_1 == 35

    print("     Part 1:", part_1(read_puzzle_data(DAY)))

    test_result_part_2 = part_2(read_puzzle_data(f"{DAY}-test"))
    print("Test Part 2:", test_result_part_2)
    assert test_result_part_2 == 46

    result_part_2 = part_2(read_puzzle_data(DAY))
    print("     Part 2:", result_part_2)
    assert result_part_2 == 137516820