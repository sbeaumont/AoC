"""
Solution for Advent of Code challenge 2017

[Spiral Memory](http://adventofcode.com/2017/day/3)

Part 2
"""

import itertools

PUZZLE_INPUT = 312051

# cute way to calculate all permutations of (x, y) deltas
neighbour_deltas = [d for d in itertools.product([-1, 0, 1], [-1, 0, 1]) if d != (0, 0)]
direction_vectors = ((1, 0), (0, 1), (-1, 0), (0, -1))


def spiral_memory(max_value):
    x = y = 0
    visited_coordinates = dict()
    visited_coordinates[(0, 0)] = 1
    direction = 0
    # edge_length, edge_pos and make_longer are all to spiral outwards, one step at a time.
    edge_length = 1
    edge_pos = 0
    make_longer = False
    while visited_coordinates[(x, y)] < max_value:
        edge_pos += 1
        x += direction_vectors[direction][0]
        y += direction_vectors[direction][1]
        neighbours = [(x + d[0], y + d[1]) for d in neighbour_deltas]
        visited_coordinates[(x, y)] = sum([visited_coordinates.get(coord, 0) for coord in neighbours])
        if edge_pos == edge_length:
            direction = (direction + 1) % 4
            edge_pos = 0
            # this make_longer bool flip is to use a length twice: 1, 1, 2, 2, 3, 3...
            if make_longer:
                edge_length += 1
            make_longer = not make_longer
    print("The first value larger than {} is {}".format(max_value, visited_coordinates[(x, y)]))


if __name__ == '__main__':
    spiral_memory(800)
    spiral_memory(PUZZLE_INPUT)