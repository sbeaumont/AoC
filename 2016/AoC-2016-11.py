#!/usr/bin/env python

"""Solution for the Advent of Code challenge 2016, day 11.

Assignment:

The first floor contains a strontium generator, a strontium-compatible microchip, a plutonium generator, and a plutonium-compatible microchip.
The second floor contains a thulium generator, a ruthenium generator, a ruthenium-compatible microchip, a curium generator, and a curium-compatible microchip.
The third floor contains a thulium-compatible microchip.
The fourth floor contains nothing relevant.

Rules to implement:

As long as I'm not on the top floor:
- If two chips can move up safely, do that.
- If two generators can be brought up safely, do that. Choose generators first that have a match on the closest higher level.
- if a chip and a generator can be brought up safely, do that.
- if a pair can be brought up safely, do that.
(As long as I'm not on the lowest floor:)
- If one chip can be brought down safely, do that.
- If one generator can be brought down safely, do that.
"""

__author__ = "Serge Beaumont"
__date__ = "December 2016"

MAP = {
    4: [],
    3: ['TM'],
    2: ['TG', 'RG', 'RM', 'CG', 'CM'],
    1: ['SG', 'SM', 'PG', 'PM']
}

from AoC201611Level import Level


# Debugging print statements
def printLevels(levels):
    for level in range(4, 0, -1):
        print(levels[level].fullContents())

def printSafety(levels, obj):
    for i in range(4, 0, -1):
        print("Level {0} is {2} for {1}".format(i, obj, 'safe' if levels[i].safe(obj) else 'unsafe'))

def printCanLeave(levels, ):
    for i in range(4, 0, -1):
        for obj in levels[i].contents:
            print("{0} {1} leave alone.".format(obj, 'can' if levels[i].safeToLeave(obj) else 'can not'))

# while len(MAP[4]) < 10:

class Elevator:
    def __init__(self):
        self.currentLevelNumber = 1
        # Initialize Level objects
        self.levels = {}
        for number, level in MAP.items():
            self.levels[number] = Level(number, level)
        # Tell the elevators who their higher neighbours are
        for i in range(1, 4):
            self.levels[i].higher = self.levels[i + 1]
        # Tell the elevators who their lower neighbours are
        for i in range(2, 5):
            self.levels[i].lower = self.levels[i - 1]

    def currentLevel(self):
        return self.levels[self.currentLevelNumber]

    def moveTwoChips(self):
        if self.currentLevel().higher:
            return self._moveTwoItems(self.currentLevel().microchips())
        else:
            return False

    def moveTwoGenerators(self):
        if self.currentLevel().higher:
            return self._moveTwoItems(self.currentLevel().generatorsThatCanLeave())
        else:
            return False

    def _moveTwoItems(self, items):
        movable = []
        for item in items:
            if self.currentLevel().higher.safe(item):
                movable.append(item)
        if len(movable) >= 2:
            self.currentLevel().moveUp(movable[0:2])
            self.currentLevelNumber += 1
            return True
        return False

    def moveChipAndGenerator(self):
        pass

    def moveChipDown(self):
        if self.currentLevel().unpairedMicrochips():
            self.currentLevel().moveDown([self.currentLevel().unpairedMicrochips()[0],])
            self.currentLevelNumber -= 1
            return True
        return False

    def moveGeneratorDown(self):
        pass

    def singleCycle(self):
        if self.moveTwoChips(): return
        if self.moveTwoGenerators(): return
        if self.moveChipAndGenerator(): return
        if self.moveChipDown(): return
        if self.moveGeneratorDown(): return
        print("Nothing happened!")

if __name__ == '__main__':
    elevator = Elevator()
    for i in range(3):
        elevator.singleCycle()
    printLevels(elevator.levels)
    print("Elevator is at", elevator.currentLevelNumber)