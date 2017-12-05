#!/usr/bin/env python3

"""Solution for Advent of Code challenge 2017

[High-Entropy Passphrases](http://adventofcode.com/2017/day/4)"""

__author__ = "Serge Beaumont"
__date__ = "December 2017"


from aoctools import load_and_split_file

passphrases = load_and_split_file('AoC-2017-4-input.txt')

valid_passphrases = [passphrase for passphrase in passphrases if len(set(passphrase)) == len(passphrase)]
print("Part 1: {} valid in {} passphrases".format(len(valid_passphrases), len(passphrases)))

valid_and_no_anagrams = list()
for passphrase in valid_passphrases:
    sorted_passphrase = [''.join(sorted(word)) for word in passphrase]
    if len(set(sorted_passphrase)) == len(sorted_passphrase):
        valid_and_no_anagrams.append(passphrase)

print("Part 2: {} valid and no anagram in {} passphrases".format(len(valid_and_no_anagrams), len(passphrases)))