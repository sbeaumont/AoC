#!/usr/bin/env python

"""Solution for the Advent of Code challenge 2015, day 4 part 1.

Generate digest, check, try again."""

__author__ = "Serge Beaumont"
__date__ = "December 2016"

import hashlib

# Initialize
secret = 'bgvyzdsv'
number = 0
answer = None

while not answer:
    # Generate hex digest
    hashString = secret + str(number)
    md = hashlib.md5(bytes(hashString, 'utf-8'))
    hexdigest = md.hexdigest()

    # Check
    if str(hexdigest)[0:6] == '000000':
        answer = number
        break

    # Show we're busy every once in a while.
    if number % 1000000 == 0:
        print("Busy... Now at number", number)

    # Next
    number += 1

print("Done. Answer:", answer)

