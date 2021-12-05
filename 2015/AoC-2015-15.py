#!/usr/bin/env python

"""Solution for the Advent of Code challenge 2015, day 15 part 1.

"""

__author__ = "Serge Beaumont"
__date__ = "December 2016"

DATA = """Sugar: capacity 3, durability 0, flavor 0, texture -3, calories 2
Sprinkles: capacity -3, durability 3, flavor 0, texture 0, calories 9
Candy: capacity -1, durability 0, flavor 4, texture 0, calories 1
Chocolate: capacity 0, durability 0, flavor -2, texture 2, calories 8"""

import numpy as np

# Initialize
highScore = 0
highScoreMix = None
calorieHighScore = 0
calorieHighScoreMix = None

# Load data
propertyMatrix = []
for line in DATA.split('\n'):
    name, props = line.split(':')
    properties = []
    for prop in props.split(','):
        propname, value = prop.split()
        properties.append(int(value))
    propertyMatrix.append(properties)
baseMatrix = np.array(propertyMatrix).T[0:-1]
calorieMatrix = np.array(propertyMatrix).T[-1]

def score(mix):
    # Multiply all_ingredients with chosen mix
    mixed = baseMatrix * np.array(mix)
    # Add properties and multiply them for final score
    mixedSums = np.sum(mixed, axis=1)
    # Set negative totals to 0
    mixedSums = [0 if x < 0 else x for x in mixedSums]
    return np.multiply.reduce(mixedSums)

def permuteMix(soFar, rest):
    global highScore, highScoreMix, calorieHighScore, calorieHighScoreMix
    if len(rest) == 1:
        mixToScore = soFar + (100 - sum(soFar),)
        sc = score(mixToScore)
        # Score for Part 1
        if sc > highScore:
            highScore = sc
            highScoreMix = mixToScore
        # Score for Part 2
        if sum(calorieMatrix * mixToScore) == 500 and sc > calorieHighScore:
            calorieHighScore = sc
            calorieHighScoreMix = mixToScore
    else:
        for i in range(rest[0], 100):
            if sum(soFar) + i <= 100:
                permuteMix(soFar + (i,), rest[1:])

permuteMix(tuple(), (0,0,0,0))
print("High score is", highScore, "for mix", highScoreMix)
print("High score for a 500 calorie cookie is", calorieHighScore, "for mix", calorieHighScoreMix)
