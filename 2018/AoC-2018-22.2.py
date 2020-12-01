import numpy as np
import networkx as nx

DEPTH = 11991
TARGET = (6, 797)
REGION_TYPES = {0: '.', 1: '|', 2: '='}


class CaveSystem(object):
    def __init__(self, target, depth):
        self.depth = depth
        self.target = target
        self.cave_size = (target[0] + 1, target[1] + 1)
        self.geo_indexes = np.zeros(self.cave_size, dtype=int)
        self.region_types = np.zeros(self.cave_size, dtype=int)
        self.initialize()

    def geo_index(self, coords):
        if coords in ((0, 0), self.target):
            result = 0
        elif coords[1] == 0:
            result = coords[0] * 16807
        elif coords[0] == 0:
            result = coords[1] * 48271
        else:
            if not self.geo_indexes[coords]:
                self.geo_indexes[coords] = self.erosion_level((coords[0] - 1, coords[1])) * self.erosion_level((coords[0], coords[1] - 1))
            result = self.geo_indexes[coords]
        return result

    def erosion_level(self, coords):
        return (self.geo_index(coords) + self.depth) % 20183

    def region_type(self, coords):
        return self.erosion_level(coords) % 3

    def initialize(self):
        for x in range(self.cave_size[0]):
            for y in range(self.cave_size[1]):
                self.region_types[x, y] = self.region_type((x, y))

    def print(self):
        for x in range(self.cave_size[0]):
            cave_line = []
            for y in range(self.cave_size[1]):
                cave_line.append(REGION_TYPES[self.region_type[x, y]])
            print(''.join(cave_line))


TORCH = 'T'
CLIMBING_GEAR = 'C'
NEITHER = 'N'

# T is Rocky (0) or Narrow (2)
# C is Rocky (0) or Wet    (2)
# N is Wet   (1) or Narrow (2)

# Rocky  (0) is C or T
# Wet    (1) is C or N
# Narrow (2) is T or N

graph = nx.MultiGraph()


class Rescuer(object):
    def __init__(self):
        self.gear = CLIMBING_GEAR
        self.minutes = 0

    def switch_gear(self, to_gear):
        self.gear = to_gear
        self.minutes += 7


cs_test = CaveSystem((10, 10), 510)
cs = CaveSystem(TARGET, DEPTH)
