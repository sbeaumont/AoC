#!/usr/bin/env python3

"""
Solution for Advent of Code challenge 2017

[Spiral Memory](http://adventofcode.com/2017/day/3)

    Part 1

    Finds the first position that is higher, and its "loop number". This is the shortest
    manhattan distance of that loop, which corresponds with the midpoints of the edges
    in line with the center position. The rest of the manhattan distance is the minimum
    distance to one of these midpoints.
"""

__author__ = "Serge Beaumont"
__date__ = "December 2017"

# c33333c     c
# 3c222c3    c3
# 32c1c23   c23
# 3210123  0123
# 32c1c23   x23
# 3c222c3    x3
# c33333c     x
#          1246

# n           0  1  2  3  4
# 1 side      0  2  4  6  8
# 4 sides     0  8 16 24 32
# center      1
# cumulative  1  9 25 49 81 <- highest number in loop, next loop starts at +1

# total = (n + (n + 1))^2 = (2n + 1)^2


PUZZLE_INPUT = 312051


def cumulative_loop(n):
    return (2*n+1)**2


def manhattan_distance(position):
    n = 0
    while cumulative_loop(n) < position:
        n += 1

    max_position_in_loop = cumulative_loop(n)
    midpoints = [max_position_in_loop - i*n for i in (1, 3, 5, 7)]
    minimum_difference = min([abs(position - m) for m in midpoints])
    print("Manhattan distance of {} is {}".format(position, n + minimum_difference))


if __name__ == "__main__":
    manhattan_distance(1)
    manhattan_distance(9)
    manhattan_distance(12)
    manhattan_distance(23)
    manhattan_distance(25)
    manhattan_distance(26)
    manhattan_distance(1024)
    manhattan_distance(PUZZLE_INPUT)
