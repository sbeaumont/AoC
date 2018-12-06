#!/usr/bin/env python3

"""Solution for Advent of Code challenge 2017

[---](http://adventofcode.com/2017/day/10)"""

from knothash import *

PUZZLE_INPUT = "76,1,88,148,166,217,130,0,128,254,16,2,130,71,255,229"
PART_TWO_END_SEQUENCE = [17, 31, 73, 47, 23]
STRING_LENGTH = 256

# Tests
test_string = list(range(1, 6))
assert reverse_slice(test_string, 0, 3) == [3, 2, 1, 4, 5]
assert reverse_slice(test_string, 1, 3) == [1, 4, 3, 2, 5]
assert reverse_slice(test_string, 0, 5) == [5, 4, 3, 2, 1]
assert reverse_slice(test_string, 4, 4) == [2, 1, 5, 4, 3]
assert reverse_slice([4, 3, 0, 1, 2], 1, 5) == [3, 4, 2, 1, 0]
assert knot_hash(range(5), (3, 4, 1, 5))[0] == [3, 4, 2, 1, 0]

# Part 1
p_input = [int(i) for i in PUZZLE_INPUT.split(',')]
k_hash = knot_hash(range(STRING_LENGTH), p_input)
print("Current position: {}, skip size: {}.".format(k_hash[1], k_hash[2]))
st = k_hash[0]
print("Part 1: The first two numbers are {} and {}, their product is {}.".format(st[0], st[1], st[0] * st[1]))

# Part 2
seq = [ord(c)for c in PUZZLE_INPUT]
solution = full_knot_hash(seq)

print("\nPart 2: {}".format(solution))

assert solution == '4db3799145278dc9f73dcdbc680bd53d'
