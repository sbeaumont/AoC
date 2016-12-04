#!/usr/bin/env python

"""Solution for the Advent of Code challenge 2015, day 14 part 2."""

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

import pprint

class Reindeer(object):
    def __init__(self, name, flyspeed, flytime, resttime):
        self.name = name
        self.flyspeed = flyspeed
        self.flytime = flytime
        self.resttime = resttime
        self.points = 0
        self.distance = 0

    def isFlying(self, time):
        remainingtime = time % (self.flytime + self.resttime)
        return (remainingtime >= 1) and (remainingtime <= self.flytime)

    def move(self, time):
        if self.isFlying(time):
            self.distance += self.flyspeed

    def __repr__(self):
        return "Reindeer {0.name}: (Sp{0.flyspeed}/F{0.flytime}s/R{0.resttime}s) pts:{0.points} dst:{0.distance}".format(self)

# Initialize reindeer
reindeer = []
for line in DATA.split('\n'):
    parts = line.split()
    reindeer.append(Reindeer(parts[0], int(parts[3]), int(parts[6]), int(parts[13])))

# Race!

TOTAL_RACE_TIME = 2503

maxDistance = 0
for time in range(1, TOTAL_RACE_TIME + 1):
    # Move reindeer and push maxDistance forward if needed
    for deer in reindeer:
        deer.move(time)
        if deer.distance > maxDistance:
            maxDistance = deer.distance

    # Best reindeer now get a point
    for deer in reindeer:
        if deer.distance == maxDistance:
            deer.points += 1

# Determine winner
mostPoints = 0
winner = None
for deer in reindeer:
    if deer.points > mostPoints:
        winner = deer
        mostPoints = deer.points

print("Winner is {0.name} with {0.points} points.\n".format(winner))

pprint.pprint(reindeer)
