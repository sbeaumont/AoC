#!/usr/bin/env python3

"""Solution for Advent of Code challenge 2020 - Day 17"""

__author__ = "Serge Beaumont"
__date__ = "December 2020"

with open("AoC-2020-17-input.txt") as infile:
    file_data = [line.strip() for line in infile.readlines()]

print(file_data)


def neighbours3d(coords):
    x, y, z = coords
    return \
    ((x+1, y, z-1), (x - 1, y, z-1), (x, y+1, z-1), (x, y-1, z-1), (x, y, z-1), (x+1, y+1, z-1), (x-1, y-1, z-1), (x+1, y-1, z-1), (x-1, y+1, z-1),
     (x+1, y, z  ), (x - 1, y, z  ), (x, y+1, z  ), (x, y-1, z  ),              (x+1, y+1, z  ), (x-1, y-1, z  ), (x+1, y-1, z  ), (x-1, y+1, z  ),
     (x+1, y, z+1), (x - 1, y, z+1), (x, y+1, z+1), (x, y-1, z+1), (x, y, z+1), (x+1, y+1, z+1), (x-1, y-1, z+1), (x+1, y-1, z+1), (x-1, y+1, z+1))


def intersection(lst1, lst2):
    lst3 = [value for value in lst1 if value in lst2]
    return lst3


def count_live_neighbours(pd, coords):
    return len(intersection(pock_dim, neighbours3d(coords)))


def boundaries(pd):
    x_min, y_min, z_min = pd[0]
    x_max, y_max, z_max = pd[0]
    for cube in pd[1:]:
        x_min = min(x_min, cube[0])
        x_max = max(x_max, cube[0])
        y_min = min(y_min, cube[1])
        y_max = max(y_max, cube[1])
        z_min = min(z_min, cube[2])
        z_max = max(z_max, cube[2])
    return (x_min, x_max), (y_min, y_max), (z_min, z_max)


pock_dim = list()
for y, line in enumerate(file_data):
    for x, element in enumerate(line):
        if element == '#':
            pock_dim.append((x, y, 0))

origin_neighbours = neighbours3d((0, 0, 0))
assert len(origin_neighbours) == 26, len(origin_neighbours)
assert (0, 0, 0) not in origin_neighbours

print(pock_dim)
print(neighbours3d((0,0,0)))
print(intersection(pock_dim, neighbours3d((0,0,0))))
print(count_live_neighbours(pock_dim, (0,0,0)))

for i in range(6):
    new_pock_dim = list()
    x_rng, y_rng, z_rng = boundaries(pock_dim)
    for x in range(x_rng[0]-1, x_rng[1]+2):
        for y in range(y_rng[0]-1, y_rng[1]+2):
            for z in range(z_rng[0]-1, z_rng[1]+2):
                n = count_live_neighbours(pock_dim, (x, y, z))
                active = (x, y, z) in pock_dim
                if (active and ((n == 2) or (n == 3))) or (not active and (n == 3)):
                    new_pock_dim.append((x, y, z))
    pock_dim = new_pock_dim

print(len(pock_dim))
