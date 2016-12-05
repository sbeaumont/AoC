#!/usr/bin/env python

"""Solution for the Advent of Code challenge 2016, day 5 part 1."""

__author__ = "Serge Beaumont"
__date__ = "December 2016"

import hashlib

def hackDoor(doorID):
    print("Hacking Door ID '{0}'".format(doorID))
    number = 0
    answer = ''
    while len(answer) < 8:
        # Generate hex digest
        hashString = doorID + str(number)
        md = hashlib.md5(bytes(hashString, 'utf-8'))
        hexdigest = str(md.hexdigest())

        # Check
        if hexdigest[0:5] == '00000':
            answer += hexdigest[5]
            print("Found next character.", answer, "in hexdigest", hexdigest)

        number += 1
    return answer

# Test with example
# abcCode = hackDoor('abc')
# print("Answer:", abcCode, "expecting 18f47a30")

part1Code = hackDoor('wtnhxymk')
print("Answer:", part1Code)