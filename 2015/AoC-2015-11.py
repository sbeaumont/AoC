#!/usr/bin/env python

"""Solution for the Advent of Code challenge 2015, day 11 parts 1 and 2.

Policy:
1. 8 lowercase letters
2. 1 increasing straight of 3 letters
3. At least 2 different non overlapping pairs of letters
4. No letters i, o or l

Solutions:
1. Stop iterating when you reach 9 characters.
2. There are actually only 14 combinations possible, so fine to list them all out in a regex.
3. Find doubles with a regex, check if the set of unique doubles is two or larger.
4. Create a new "alphabet" that is referenced when incrementing.
"""

__author__ = "Serge Beaumont"
__date__ = "December 2016"

import re

password = list("vzbxkghb")
LETTERS = "abcdefghjkmnpqrstuvwxyz"
STRAIGHTS = "abc|bcd|cde|def|efg|pqr|qrs|rst|stu|tuv|uvw|vwx|wxy|xyz"
DOUBLES = r"([a-z])\1"

def increment(passwordChars, position):
    """Increment the word based on the new alphabet."""
    digitIndex = LETTERS.index(passwordChars[position])
    if digitIndex + 1 < len(LETTERS):
        passwordChars[position] = LETTERS[digitIndex + 1]
    else:
        passwordChars[position] = LETTERS[0]
        increment(passwordChars, position - 1)

# First solution is part 1, second solution is part 2 of the challenge
for i in range(2):
    while len(password) <= 8:
        increment(password, -1)

        # Doubles
        passwordString = "".join(password)
        doubles = re.findall(DOUBLES, passwordString)
        doublesOK = (len(doubles) >= 2) and (len(set(doubles)) >= 2)

        # Straight run
        straightOK = re.search(STRAIGHTS, passwordString)

        if doublesOK and straightOK:
            print("Found new password", passwordString)
            break
