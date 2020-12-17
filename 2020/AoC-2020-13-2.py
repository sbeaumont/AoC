#!/usr/bin/env python3

"""Solution for Advent of Code challenge 2020 - Day 13"""

__author__ = "Serge Beaumont"
__date__ = "December 2020"


test_1_data = [1068781, '7,13,x,x,59,x,31,19']
test_2_data = [3417, '17,x,13,19']
test_3_data = [754018, '67,7,59,61']


def do(bus_data, verbose=False, start=0):
    bus_list = bus_data.split(',')
    buses = dict()
    for i in range(len(bus_list)):
        if bus_list[i] != 'x':
            buses[int(bus_list[i])] = i

    if verbose:
        print(buses)

    slowest_bus = max(buses.keys())
    slow_bus_order = sorted(buses.keys(), reverse=True)
    offsets = [buses[o] for o in slow_bus_order]
    corrections = [o - offsets[0] for o in offsets]
    other_buses = list(zip(slow_bus_order[1:], corrections[1:]))

    if verbose:
        print(slowest_bus, offsets, slow_bus_order, corrections, other_buses)

    if start:
        number_to_try = start - (start % slowest_bus)
        assert number_to_try % slowest_bus == 0
    else:
        number_to_try = 0
    found = False
    while not found:
        number_to_try += slowest_bus
        maybe = True
        for bus, offset in other_buses:
            if (number_to_try + offset) % bus != 0:
                maybe = False
                break
        if verbose and number_to_try % 10000000 == 0:
            print(number_to_try)
        if maybe:
            found = True
    return number_to_try + min(corrections)


if __name__ == '__main__':
    assert do(test_1_data[1]) == test_1_data[0]
    assert do(test_1_data[1], start=3000) == test_1_data[0]
    assert do(test_2_data[1]) == test_2_data[0]
    assert do(test_3_data[1]) == test_3_data[0]

    with open("AoC-2020-13-input.txt") as infile:
        data = [line.strip() for line in infile.readlines()]
    do(data[1], verbose=True, start=100600000000000)
