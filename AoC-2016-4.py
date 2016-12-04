#!/usr/bin/env python

"""Solution for the Advent of Code challenge 2016, day 4 part 1 and 2.

Pretty printed the full list of decoded rooms because they're fun."""

__author__ = "Serge Beaumont"
__date__ = "December 2016"

import re, pprint

# Load
with open("AoC-2016-4-data.txt", 'r') as content_file:
    content = content_file.read()

pattern = re.compile(r'([a-z]+)(\d+)\[([a-z]{5})\]')

idtotal = 0
realrooms = {}

for line in content.split('\n'):
    # Parse line into its component parts
    nodashes = re.sub('[-]', '', line)
    letters, id, checksum = re.search(pattern, nodashes).groups()

    # Count of unique letters
    letterCount = {}
    for c in set(letters):
        letterCount.setdefault(letters.count(c), []).append(c)

    # Generate full checksum key: reverse count, then alphabetical
    fullkey = []
    for count in sorted(letterCount, reverse=True):
        fullkey.extend(sorted(letterCount[count]))
    fullkeyString = ''.join(fullkey)

    # Compare
    if fullkeyString[:5] == checksum:
        idtotal += int(id)
        # Since we're here anyway, let's get ready for part 2
        realrooms[id] = re.sub('[-]', ' ', re.search('[a-z\-]+', line).group(0)).split()

# Answer to part 1
print("Sum of Sector IDs:", idtotal)

# Part 2: look for "North Pole Objects"

for id, encryptedWords in realrooms.items():
    # Create decoder based on an idea found here: https://stackoverflow.com/questions/3269686/short-rot13-function
    decoder = {}
    for c in (65, 97):
        for i in range(26):
            decoder[chr(i + c)] = chr((i + int(id)) % 26 + c)

    # Decode the room name based on ID
    decodedWords = []
    for encWord in encryptedWords:
        decodedWords.append("".join([decoder.get(c, c) for c in encWord]))
    decodedName = " ".join(decodedWords)

    # Assign the name back to the dict for pretty printing, and check if we found the room.
    realrooms[id] = decodedName
    if 'northpole object' in decodedName:
        print("North Pole Objects room is:", id)

# Because funny.
pprint.pprint(realrooms)