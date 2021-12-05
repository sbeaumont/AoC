#!/usr/bin/env python3

"""Solution for Advent of Code challenge 2020 - Day 20"""

__author__ = "Serge Beaumont"
__date__ = "December 2020"

from math import prod
from matrixutils import Matrix


class Tile(object):
    def __init__(self, _id, tile_data):
        self._id = _id
        self.m = Matrix(tile_data)
        self.edges = list()
        self.matching = list()
        self.calc_all_edges()
        self.rotate = self.m.rotate
        self.fliplr = self.m.fliplr

    def __str__(self):
        return self.m.to_str()

    def calc_all_edges(self):
        self.edges = list()
        # Top (0, 1)
        top_row = ''.join(self.m.row(0))
        self.edges.append(top_row)
        self.edges.append(top_row[::-1])
        # Right (2, 3)
        right = ''.join(self.m.column(-1))
        self.edges.append(right)
        self.edges.append(right[::-1])
        # Bottom (4, 5)
        bottom_row = ''.join(self.m.row(-1))
        self.edges.append(bottom_row)
        self.edges.append(bottom_row[::-1])
        # Left (6, 7)
        left = ''.join(self.m.column(0))
        self.edges.append(left)
        self.edges.append(left[::-1])

    @property
    def directed_edges(self):
        return [''.join(r) for r in self.m.edges]

    def align(self, other):
        """Align other tile to this one: rotate and flip it as needed."""
        # First rotate as needed
        my_or, other_or = self.match_orientation(other)
        or_diff = (other_or - my_or - 4) % 8
        rotations_needed = -(or_diff // 2)
        other.rotate(rotations_needed)
        # Now check if we still need a flip
        my_or, other_or = self.match_orientation(other)
        or_diff = (other_or - my_or - 4) % 8
        if (or_diff % 2) == 1:
            if my_or in (0, 4):
                other.fliplr()
            else:
                other.flipud()

    def can_match(self, other):
        """Don't care about orientation. Any match is good."""
        return len([value for value in self.edges if value in other.edges]) > 0

    def match_orientation(self, other):
        """The match is done with this tile being the dominant one. The result will show
        any flipping the other tile would need to do."""
        matching_edges = [value for value in self.directed_edges if value in other.edges]
        my_matching_edge = [e for e in self.edges if e in matching_edges][0]
        other_matching_edge = [e for e in other.edges if e in matching_edges][0]
        return self.edges.index(my_matching_edge), other.edges.index(other_matching_edge)


class SeaMonster(object):
    shape = [
        '                  # ',
        '#    ##    ##    ###',
        ' #  #  #  #  #  #   '
    ]

    def __init__(self):
        pass


def load(filename):
    tiles = list()

    def create_tile(tile_id, lines):
        tile_data = [[c for c in ln] for ln in lines]
        new_tile = Tile(tile_id, tile_data)
        tiles.append(new_tile)
        return new_tile

    with open(filename) as infile:
        tile_lines = list()
        tile_id = None
        for line in [ln.strip() for ln in infile.readlines()]:
            if line.startswith("Tile"):
                tile_id = int(line.split(' ')[1][:-1])
            elif line != '':
                tile_lines.append(line)
            else:
                create_tile(tile_id, tile_lines)
                tile_lines = list()
        else:
            create_tile(tile_id, tile_lines)

    return tiles


def match_tiles(tiles):
    total_matches = 0
    for i in range(len(tiles)):
        tile = tiles[i]
        for t in tiles[i+1:]:
            if t.can_match(tile):
                tile.matching.append(t)
                t.matching.append(tile)
                total_matches += 1
    return tiles


def do(filename):
    return match_tiles(load(filename))


do("AoC-2020-20-test-1.txt")

tiles = do("AoC-2020-20-input.txt")
corner_tiles = [tile for tile in tiles if len(tile.matching) == 2]
part_1 = prod([t._id for t in corner_tiles])
print("Part 1:", part_1)
assert part_1 == 29293767579581

root_tile: Tile = corner_tiles[0]
for other in root_tile.matching:
    orientation = root_tile.match_orientation(other)
    print(root_tile._id, orientation[0], other._id, orientation[1])
    # print(root_tile, '\n')
    print(other, '\n')
    root_tile.align(other)
    orientation = root_tile.match_orientation(other)
    print(root_tile._id, orientation[0], other._id, orientation[1])
    # print(root_tile, '\n')
    print(other)
