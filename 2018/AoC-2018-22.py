import numpy as np

DEPTH = 11991
TARGET = (6, 797)
REGION_TYPES = {0: '.', 1: '|', 2: '='}


class CaveSystem(object):
    def __init__(self, target, depth):
        self.depth = depth
        self.target = target
        self.cave_size = (target[0] + 1, target[1] + 1)
        self.geo_indexes = np.zeros(self.cave_size, dtype=int)
        self.erosion_levels = np.zeros(self.cave_size, dtype=int)
        self.risk_level = self.calculate()

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

    def calculate(self):
        risk_level = 0
        for x in range(self.cave_size[0]):
            for y in range(self.cave_size[1]):
                el = self.erosion_level((x, y)) % 3
                self.erosion_levels[x, y] = el
                risk_level += el
        return risk_level

    def print(self):
        for x in range(self.cave_size[0]):
            cave_line = []
            for y in range(self.cave_size[1]):
                el = self.erosion_level((x, y)) % 3
                cave_line.append(REGION_TYPES[el])
            print(''.join(cave_line))


cs_test = CaveSystem((10, 10), 510)
assert cs_test.risk_level == 114, f"Expected 114, got {cs_test.risk_level}"

cs = CaveSystem(TARGET, DEPTH)
print(f"Risk level of cave system to {TARGET} at depth {DEPTH} is {cs.risk_level}")
cs.print()

unique, counts = np.unique(cs.erosion_levels, return_counts=True)
for u, c in zip(unique, counts):
    print(f"Type {u} count {c}, risk level {u * c}")
