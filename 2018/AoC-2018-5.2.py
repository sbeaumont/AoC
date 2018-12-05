#!/usr/bin/env python3

"""Solution for Advent of Code challenge 2018 - Day 5 Part 1
"""

__author__ = "Serge Beaumont"
__date__ = "December 2018"

with open("AoC-2018-5-input.txt") as infile:
    original_polymer = infile.read()

alphabet = "abcdefghijklmnopqrstuvwxyz"
reactors = [''.join(pair) for pair in zip(alphabet, alphabet.upper()) + zip(alphabet.upper(), alphabet)]
print(reactors)


def react(polymer):
    reactors_found = True
    while reactors_found:
        reactors_found = False
        for i in range(len(polymer)-1):
            if polymer[i].lower() == polymer[i+1].lower():
                if (polymer[i].isupper() and polymer[i+1].islower()) or (polymer[i].islower() and polymer[i+1].isupper()):
                    reactors_found = True
                    polymer = polymer[:i] + polymer[i+2:]
                    break
    return polymer


shortest_length = len(original_polymer)
shortest_reactor = ''
for reactor in alphabet:
    redacted_polymer = original_polymer.replace(reactor.upper(), '')
    redacted_polymer = redacted_polymer.replace(reactor.lower(), '')
    new_polymer = react(redacted_polymer)
    if len(new_polymer) < shortest_length:
        shortest_length = len(new_polymer)
        shortest_reactor = reactor

print(shortest_reactor, shortest_length)