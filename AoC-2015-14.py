#!/usr/bin/env python

"""Solution for the Advent of Code challenge 2015, day 14 part 1."""

__author__ = "Serge Beaumont"
__date__ = "December 2016"

DATA = """Vixen can fly 8 km/s for 8 seconds, but then must rest for 53 seconds.
Blitzen can fly 13 km/s for 4 seconds, but then must rest for 49 seconds.
Rudolph can fly 20 km/s for 7 seconds, but then must rest for 132 seconds.
Cupid can fly 12 km/s for 4 seconds, but then must rest for 43 seconds.
Donner can fly 9 km/s for 5 seconds, but then must rest for 38 seconds.
Dasher can fly 10 km/s for 4 seconds, but then must rest for 37 seconds.
Comet can fly 3 km/s for 37 seconds, but then must rest for 76 seconds.
Prancer can fly 9 km/s for 12 seconds, but then must rest for 97 seconds.
Dancer can fly 37 km/s for 1 seconds, but then must rest for 36 seconds."""

TOTAL_RACE_TIME = 2503
maxDistance = 0
bestReindeer = None
for line in DATA.split('\n'):
    parts = line.split()
    name = parts[0]
    flyspeed = int(parts[3])
    flytime = int(parts[6])
    resttime = int(parts[13])

    wholecycles = TOTAL_RACE_TIME // (flytime + resttime)
    remainingtime = TOTAL_RACE_TIME % (flytime + resttime)
    if remainingtime > flytime:
        remainingtime = flytime

    distance = (wholecycles * flytime + remainingtime) * flyspeed
    if distance > maxDistance:
        maxDistance = distance
        bestReindeer = name

print("The best reindeer is", bestReindeer, "with", maxDistance)
