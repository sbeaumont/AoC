#!/usr/bin/env python3

"""Solution for Advent of Code challenge 2017 - Day 17 part 2"""

__author__ = "Serge Beaumont"
__date__ = "December 2018"

import collections
import time

STEPS_PER_INSERTION = 354
TOTAL_INSERTIONS = 50000000

start = time.time()

print(f"Calculating {TOTAL_INSERTIONS} insertions...")
printer_buffer = collections.deque([0])
for i in range(TOTAL_INSERTIONS - 1):
    printer_buffer.rotate(-STEPS_PER_INSERTION)
    printer_buffer.append(i + 1)
    # When you want to see some progress...
    # if (i % 1000000 == 0) and (i > 0):
    #     print(i)
pb = list(printer_buffer)
print(f"Part 2: The value after 0 is {pb[pb.index(0)+1]}")

end = time.time()
print(f"{end - start:.4f} seconds to run.")
