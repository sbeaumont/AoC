#!/usr/bin/env python3

"""Solution for Advent of Code challenge 2018 - Day 20 part 1"""

__author__ = "Serge Beaumont"
__date__ = "December 2018"

rooms = dict()

direction_to_delta = {'W': (-1, 0), 'N': (0, 1), 'E': (1, 0), 'S': (0, -1)}
inverse_direction = {'W': 'E', 'N': 'S', 'E': 'W', 'S': 'N'}


def go_to(coord1, direction):
    delta = direction_to_delta[direction]
    coord2 = (coord1[0] + delta[0], coord1[1] + delta[1])
    get_room(coord1)[direction] = coord2
    get_room(coord2)[inverse_direction[direction]] = coord1
    return coord2


def get_room(coord):
    if coord not in rooms:
        rooms[coord] = dict()
    return rooms[coord]


def walk_path(xy, pth, i=0):
    back_xy = xy
    while i < len(pth):
        c = pth[i]
        if c in ('E', 'S', 'W', 'N'):
            xy = go_to(xy, c)
        elif c == '(':
            walk_path(xy, pth, i+1)
            break
        elif c == '|':
            walk_path(back_xy, pth, i+1)
            break
        elif c == ')':
            pass
        i += 1


if __name__ == '__main__':
    walk_path((0, 0), "ESSWWN(E|NNENN(EESS(WNSE|)SSS|WWWSSSSE(SW|NNNE)))")
    from pprint import pprint
    pprint(rooms)

