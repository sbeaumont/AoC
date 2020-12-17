#!/usr/bin/env python3

"""Solution for Advent of Code challenge 2020 - Day 17"""

__author__ = "Serge Beaumont"
__date__ = "December 2020"

with open("AoC-2020-17-input.txt") as infile:
    file_data = [line.strip() for line in infile.readlines()]


def count_live_neighbours(pd, coord):
    def max_distance(coord1, coord2):
        return max([abs(c1 - c2) for c1, c2 in zip(coord1, coord2)])
    return len([c for c in pd if max_distance(c, coord) == 1])


def boundaries(pd):
    x_min, y_min, z_min, w_min = pd[0]
    x_max, y_max, z_max, w_max = pd[0]
    for cube in pd[1:]:
        x_min = min(x_min, cube[0])
        x_max = max(x_max, cube[0])
        y_min = min(y_min, cube[1])
        y_max = max(y_max, cube[1])
        z_min = min(z_min, cube[2])
        z_max = max(z_max, cube[2])
        w_min = min(w_min, cube[3])
        w_max = max(w_max, cube[3])
    return (x_min, x_max), (y_min, y_max), (z_min, z_max), (w_min, w_max)


pock_dim = list()
for y, line in enumerate(file_data):
    for x, element in enumerate(line):
        if element == '#':
            pock_dim.append((x, y, 0, 0))


for i in range(6):
    print(f"Starting iteration {i}")
    new_pock_dim = list()
    x_rng, y_rng, z_rng, w_rng = boundaries(pock_dim)
    for x in range(x_rng[0]-1, x_rng[1]+2):
        for y in range(y_rng[0]-1, y_rng[1]+2):
            for z in range(z_rng[0]-1, z_rng[1]+2):
                for w in range(z_rng[0] - 1, z_rng[1] + 2):
                    n = count_live_neighbours(pock_dim, (x, y, z, w))
                    active = (x, y, z, w) in pock_dim
                    if (active and ((n == 2) or (n == 3))) or (not active and (n == 3)):
                        new_pock_dim.append((x, y, z, w))
    pock_dim = new_pock_dim

print("Part 2:", len(pock_dim))
