#!/usr/bin/env python3

"""Solution for Advent of Code challenge 2020 - Day 10"""

__author__ = "Serge Beaumont"
__date__ = "December 2020"


from pprint import pprint


def part_1(filename):
    with open(filename) as infile:
        adapters = [int(line.strip()) for line in infile.readlines()]

    adapters.append(0)  # charging outlet
    adapters.append(max(adapters) + 3)  # built-in
    adapters = sorted(adapters)

    jolt_1 = jolt_3 = 0
    for i in range(1, len(adapters)):
        diff = adapters[i] - adapters[i-1]
        if diff == 1:
            jolt_1 += 1
        elif diff == 3:
            jolt_3 += 1
        else:
            print("Huh?", i, adapters[i-1:i+1])
            break
    return jolt_1 * jolt_3, jolt_1, jolt_3


def part_2(filename):
    with open(filename) as infile:
        adapters = [int(line.strip()) for line in infile.readlines()]

    adapters.append(0)  # charging outlet
    adapters.append(max(adapters) + 3)  # built-in
    adapters = sorted(adapters)

    lines = []
    line = []
    for i in range(1, len(adapters)):
        line.append(adapters[i - 1])
        if adapters[i] - adapters[i-1] == 3:
            lines.append(line)
            line = []
    lines.append([adapters[i]])
    #pprint(lines)

    combos = 1
    multiplier = {1: 1, 2: 1, 3: 2, 4: 4, 5: 7}
    for line in lines:
        combos *= multiplier[len(line)]
    #print("Combos", combos)
    assert combos < 4398046511104


if __name__ == '__main__':
    #assert part_1("AoC-2020-10-test-1.txt")[0] == 35, part_1("AoC-2020-10-test-1.txt")[1:3]
    #assert part_1("AoC-2020-10-test-2.txt")[0] == 220
    #assert part_1("AoC-2020-10-input.txt")[0] > 2432
    #print("Part 1:", part_1("AoC-2020-10-input.txt")[0])

    part_2("AoC-2020-10-input.txt")
