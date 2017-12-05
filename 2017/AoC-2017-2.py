#!/usr/bin/env python3

"""Solution for Advent of Code challenge 2017

[Corruption Checksum](http://adventofcode.com/2017/day/2)"""

__author__ = "Serge Beaumont"
__date__ = "December 2017"


from aoctools import *
import math

# divisorGenerator taken from
# https://stackoverflow.com/questions/171765/what-is-the-best-way-to-get-all-the-divisors-of-a-number


def divisor_generator(n):
    large_divisors = []
    for i in range(1, int(math.sqrt(n) + 1)):
        if n % i == 0:
            yield i
            if i*i != n:
                large_divisors.append(n / i)
    for divisor in reversed(large_divisors):
        yield int(divisor)


def find_divisors(list_of_ints):
    for number in sorted(list_of_ints, reverse=True):
        divisors = list(divisor_generator(number))[:-1]
        intersection = list(set(line) & set(divisors))
        if len(intersection) > 0:
            return number, intersection[0]


lines = convert_to_ints(load_and_split_file("AoC-2017-2-input.txt"))

checksum = 0
for line in lines:
    checksum += max(line) - min(line)
print("Part 1: {0}".format(checksum))

checksum_2 = 0
for line in lines:
    n, d = find_divisors(line)
    checksum_2 += int(n / d)
print("Part 2: {0}".format(checksum_2))