#!/usr/bin/env python3

"""Solution for Advent of Code challenge 2024"""

__author__ = "Serge Beaumont"
__date__ = "December 2024"

from aoc.utils.utils import neighbors4


class Farm(object):
    def __init__(self, entries):
        self.plots = entries

    def plants_at(self, xy):
        if (0 <= xy[0] < len(self.plots[0])) and (0 <= xy[1] < len(self.plots)):
            return self.plots[xy[1]][xy[0]]
        else:
            return '.'

    @property
    def width(self):
        return len(self.plots[0])

    @property
    def height(self):
        return len(self.plots)

def lift_region(farm: Farm, origin):
    region_type = farm.plants_at(origin)
    visited = set()
    frontier = {origin,}
    region = {origin,}
    while frontier:
        current = frontier.pop()
        visited.add(current)
        for nb in neighbors4(current):
            if (nb not in visited) and (farm.plants_at(nb) == region_type):
                region.add(nb)
                frontier.add(nb)
    return region_type, region


def all_regions(farm: Farm):
    visited = set()
    regions = list()

    for y in range(farm.height):
        for x in range(farm.width):
            if (x, y) not in visited:
                region = lift_region(farm, (x, y))
                regions.append(region)
                visited.update(region[1])
    return regions


def perimeter(region):
    result = 0
    for plot in region:
        for nb in neighbors4(plot):
            if nb not in region:
                result += 1
    return result


def sides(region):
    sides = 0
    min_x = min([r[0] for r in region])
    max_x = max([r[0] for r in region])
    min_y = min([r[1] for r in region])
    max_y = max([r[1] for r in region])
    for y in range(min_y, max_y + 1):
        top_side = (min_x, y) in region and (min_x, y-1) not in region
        if top_side:
            # Initial side at the top
            sides += 1
        bot_side = (min_x, y) in region and (min_x, y+1) not in region
        if bot_side:
            # Initial side at the bottom
            sides += 1
        for x in range(min_x + 1, max_x + 1):
            if (x, y) not in region:
                top_side = False
                bot_side = False
            else:
                if top_side:
                    if (x, y-1) in region:
                        # Side to not-side transition, get ready for a potential new side.
                        top_side = False
                else:
                    if (x, y-1) not in region:
                        # Not-side to side transition: count a new side
                        top_side = True
                        sides += 1

                if bot_side:
                    if (x, y+1) in region:
                        # Side to not-side transition, get ready for a potential new side.
                        bot_side = False
                else:
                    if (x, y+1) not in region:
                        # Not-side to side transition: count a new side
                        bot_side = True
                        sides += 1

    for x in range(min_x, max_x + 1):
        left_side = (x, min_y) in region and (x-1, min_y) not in region
        if left_side:
            # Initial side at the left
            sides += 1
        right_side = (x, min_y) in region and (x+1, min_y) not in region
        if right_side:
            # Initial side at the right
            sides += 1
        for y in range(min_y + 1, max_y + 1):
            if (x, y) not in region:
                left_side = False
                right_side = False
            else:
                if left_side:
                    if (x-1, y) in region:
                        # Side to not-side transition, get ready for a potential new side.
                        left_side = False
                else:
                    if (x-1, y) not in region:
                        # Not-side to side transition: count a new side
                        left_side = True
                        sides += 1

                if right_side:
                    if (x+1, y) in region:
                        # Side to not-side transition, get ready for a potential new side.
                        right_side = False
                else:
                    if (x+1, y) not in region:
                        # Not-side to side transition: count a new side
                        right_side = True
                        sides += 1
    return sides


def part_1(entries: list[str]):
    farm = Farm(entries)
    regions = all_regions(farm)
    price = 0
    for region in regions:
        # print(region[0], perimeter(region[1]), len(region[1]))
        price += perimeter(region[1]) * len(region[1])
    return price


def part_2(entries: list[str]):
    farm = Farm(entries)
    regions = all_regions(farm)
    price = 0
    for region in regions:
        sds = sides(region[1])
        region_price = sds * len(region[1])
        # print(region[0], sds, len(region[1]), region_price)
        price += region_price
    return price


def read_puzzle_data(data_file: str) -> list:
    with open(data_file) as infile:
        return [line.strip() for line in infile.readlines()]


assertions = {
    "Test 1": 1930,
    "Part 1": 1471452,
    "Test 2": 1206,
    "Part 2": 863366,
}

extra_tests = {
    "Test 1" : (
        ("AoC-2024-12-test-input-2.txt", 140),
        ("AoC-2024-12-test-input-3.txt", 772),
    ),
    "Test 2": (
        ("AoC-2024-12-test-input-2.txt", 80),
        ("AoC-2024-12-test-input-3.txt", 436),
        ("AoC-2024-12-test-input-4.txt", 236),
        ("AoC-2024-12-test-input-5.txt", 368),
    )
}