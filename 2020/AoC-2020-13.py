#!/usr/bin/env python3

"""Solution for Advent of Code challenge 2020 - Day 13"""

__author__ = "Serge Beaumont"
__date__ = "December 2020"


def load_file(filename):
    with open(filename) as infile:
        return [line.strip() for line in infile.readlines()]


def do(filename):
    data = load_file(filename)
    earliest = int(data[0])
    buses = [int(b) for b in data[1].split(',') if b != 'x']
    first_rides = [earliest - (earliest % bus) + bus for bus in buses]
    first_ride_idx = first_rides.index(min(first_rides))
    first_timestamp = min(first_rides)
    first_bus = buses[first_ride_idx]
    wait_time = first_timestamp - earliest
    print(f"Part 1: {wait_time} * {first_bus} = {wait_time * first_bus}")
    return wait_time * first_bus


if __name__ == '__main__':
    assert do("AoC-2020-13-test-1.txt") == 295
    do("AoC-2020-13-input.txt")