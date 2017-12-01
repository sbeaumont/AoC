#!/usr/bin/env python

"""Solution for the Advent of Code challenge 2015, day 14 part 2.

I suck at recursion and such, long live itertools!"""

__author__ = "Serge Beaumont"
__date__ = "December 2016"

DATA = """11
30
47
31
32
36
3
1
5
3
32
36
15
11
46
26
28
1
19
3"""

import itertools, math

TOTAL_EGGNOG = 150

# Load raw data into a nice tuple
containers = tuple([int(s) for s in DATA.split('\n')])

# Recipe taken from itertools documentation
def powerset(iterable):
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    return itertools.chain.from_iterable(itertools.combinations(s, r) for r in range(len(s)+1))

# Find all combinations that add up to the total egg nog
containerCombinations = 0
smallestCombinationLength = len(containers)
for contrs in powerset(containers):
    if sum(contrs) == TOTAL_EGGNOG:
        print(contrs)
        containerCombinations += 1
        if len(contrs) < smallestCombinationLength:
            smallestCombinationLength = len(contrs)

# Again for the minimum number of containers found that will fit the total egg nog
smallestCombination = []
for contrs in itertools.combinations(containers, smallestCombinationLength):
    if sum(contrs) == TOTAL_EGGNOG:
        smallestCombination.append(contrs)

print("\nIterated over these containers:")
print(containers)
print("There are {0} container combinations that total to {1}".format(containerCombinations, TOTAL_EGGNOG))
print("\nThere were {0} sets of the fewest possible containers, {1}.".format(len(smallestCombination), smallestCombinationLength))
print(smallestCombination)