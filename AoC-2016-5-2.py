#!/usr/bin/env python

"""Solution for the Advent of Code challenge 2016, day 5 part 2.

Includes dramatic unlocking sounds and graphics."""

__author__ = "Serge Beaumont"
__date__ = "December 2016"

import hashlib, random

def hackDoor(doorID):
    print("Hacking Door ID '{0}'".format(doorID))
    number = 0
    digitsFound = 0
    answer = list('________')
    while digitsFound < 8:
        # Generate hex digest
        hashString = doorID + str(number)
        md = hashlib.md5(bytes(hashString, 'utf-8'))
        hexdigest = str(md.hexdigest())

        # Check
        if hexdigest[0:5] == '00000':
            if hexdigest[5].isnumeric():
                position = int(hexdigest[5])
                if (position < 8) and (answer[position] == '_'):
                    answer[position] = str(hexdigest[6])
                    digitsFound += 1
                    print("".join(answer), random.choice(('*Beep*', '*Boop*', '*Bidibidi*', '*Brrt*')))

        number += 1
    return "".join(answer)

# Test with example
# print("Answer:", hackDoor('abc'), "expecting 05ace8e3")

import time

start_time = time.clock()

print("Answer:", hackDoor('wtnhxymk'), "in", time.clock() - start_time, "seconds.")
