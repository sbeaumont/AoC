#!/usr/bin/env python3

"""Solution for Advent of Code challenge 2017 - Day 17 part 2"""

__author__ = "Serge Beaumont"
__date__ = "December 2018"

import collections

STEPS_PER_INSERTION = 354
printer_buffer = collections.deque([0])
print(printer_buffer)

for i in range(50000000 - 1):
    printer_buffer.rotate(-STEPS_PER_INSERTION)
    printer_buffer.append(i + 1)

    # print(printer_buffer)

    if (i % 1000000 == 0) and (i > 0):
        print i

pb = list(printer_buffer)
print(pb[pb.index(0)+1])
