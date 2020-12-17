#!/usr/bin/env python3

"""Solution for Advent of Code challenge 2020 - Day 13"""

__author__ = "Serge Beaumont"
__date__ = "December 2020"

from mathutils import combine_phased_rotations

test_1_data = [1068781, '7,13,x,x,59,x,31,19']
test_2_data = [3417, '17,x,13,19']
test_3_data = [754018, '67,7,59,61']


def do(bus_data):
    bus_list = bus_data.split(',')
    buses = list()
    for i in range(len(bus_list)):
        if bus_list[i] != 'x':
            buses.append((int(bus_list[i]), i))
    current = buses[0]
    for i in range(1, len(buses)):
        current = combine_phased_rotations(current[0], current[1], buses[i][0], buses[i][1])
    return current[0] - current[1]


if __name__ == '__main__':
    assert do(test_1_data[1]) == test_1_data[0]
    assert do(test_1_data[1]) == test_1_data[0]
    assert do(test_2_data[1]) == test_2_data[0]
    assert do(test_3_data[1]) == test_3_data[0]

    with open("AoC-2020-13-input.txt") as infile:
        data = [line.strip() for line in infile.readlines()]
    part_2 = do(data[1])
    print("Part 2:", part_2)
