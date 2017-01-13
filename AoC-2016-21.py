#!/usr/bin/env python

"""Solution for the Advent of Code challenge 2016, day 21."""

__author__ = "Serge Beaumont"
__date__ = "December 2016"

import re

PUZZLE_INPUT = 'abcdefgh'

# Load
with open("AoC-2016-21-data.txt", 'r') as content_file:
    lines = [line.strip() for line in content_file]

# Ex. "rotate right 3 steps"
rotatePattern = re.compile(r'rotate (right|left) (\d+) steps?')
# Ex. "rotate based on position of letter f"
indexBasedRotationPattern = re.compile(r'rotate based on position of letter (\w)')
# Ex. "swap letter b with letter a"
swapPattern = re.compile(r'swap (letter|position) (\w) with (letter|position) (\w)')
# Ex. "move position 3 to position 4"
movePattern = re.compile(r'move position (\d+) to position (\d+)')
# Ex. "reverse positions 1 through 4"
reversePattern = re.compile(r'reverse positions (\d+) through (\d+)')

def rotate(input, rotation):
    "Positive rotation values is to the right."
    rotation = rotation % len(input)
    return input[-rotation:] + input[:-rotation]

def swapLetter(input, first, second):
    return swapPosition(input, input.index(first), input.index(second))

def swapPosition(input, first, second):
    l = list(input)
    l[first], l[second] = l[second], l[first]
    return ''.join(l)

def move(input, fromPosition, toPosition):
    l = list(input)
    c = l[fromPosition]
    l.remove(c)
    l.insert(toPosition, c)
    return ''.join(l)

def reverse(input, start, end):
    left, center, right = input[:start], input[start:end+1], input[end+1:]
    #print(left, center, right, center[::-1])
    return left + center[::-1] + right

def parseLines(lines, input, scramble=True):
    result = input
    lines = lines if scramble else lines[::-1]
    for line in lines:
        if re.search(rotatePattern, line):
            direction, amount = re.search(rotatePattern, line).group(1, 2)
            rotation = int(amount) if direction == 'right' else -int(amount)
            rotation = rotation if scramble else -rotation
            result = rotate(result, rotation)
            print("{2} <= ROTATE {0} {1}".format(direction, amount, result))
        elif re.search(indexBasedRotationPattern, line):
            letter = re.search(indexBasedRotationPattern, line).group(1)
            rotation = result.index(letter)
            rotation = 1 + (rotation + 1 if rotation >= 4 else rotation)
            result = rotate(result, rotation)
            print("{2} <= ROTATEBYINDEXOF {0} ({1})".format(letter, rotation, result))
        elif re.search(swapPattern, line):
            swapType, first, second = re.search(swapPattern, line).group(1, 2, 4)
            if swapType == 'letter':
                result = swapLetter(result, first, second)
            else:
                result = swapPosition(result, int(first), int(second))
            print("{3} <= SWAP {0} {1} <-> {2}".format(swapType, first, second, result))
        elif re.search(movePattern, line):
            fromPosition, toPosition = re.search(movePattern, line).group(1, 2)
            result = move(result, int(fromPosition), int(toPosition))
            print("{2} <= MOVE {0} -> {1}".format(fromPosition, toPosition, result))
        elif re.search(reversePattern, line):
            first, second = re.search(reversePattern, line).group(1, 2)
            result = reverse(result, int(first), int(second))
            print("{2} <= REVERSE {0} <-> {1}".format(first, second, result))
        else:
            print("NOT FOUND. ERROR")
    return result


print(PUZZLE_INPUT, "<= original input")
result = parseLines(lines, PUZZLE_INPUT)
print(result, "<= Final output")

print("Unscramble fbgdceah")
lines = lines[::-1]
result = parseLines(lines[::-1], 'fbgdceah')
print(result, "<= Final output Part 2")