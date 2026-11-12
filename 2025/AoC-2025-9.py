"""
Solution for Advent of Code challenge 2025

1.
"""

__author__ = "Serge Beaumont"
__date__ = "December 2025"


from operator import itemgetter
from math import inf
from itertools import combinations

from aoc.visualize import Visualizer, COLORS


def partition_along_axis(entries: list, axis: int) -> tuple[list, list]:
    sorted_by_axis = sorted(entries, key=itemgetter(axis))
    half_way_index = len(entries) // 2
    return sorted_by_axis[:half_way_index], sorted_by_axis[half_way_index:]


def quadrants(entries: list) -> tuple[list, list, list, list]:
    """Return points in quadrants top left, top right, bottom left, bottom right"""
    left, right = partition_along_axis(entries, 0)
    bottom_left, top_left = partition_along_axis(left, 1)
    bottom_right, top_right = partition_along_axis(right, 1)
    return top_left, top_right, bottom_left, bottom_right


def bounding_box(entries: list) -> tuple[tuple[int, int], tuple[int, int]]:
    min_x = min_y = inf
    max_x = max_y = 0
    for x, y in entries:
        if x > max_x:
            max_x = x
        if y > max_y:
            max_y = y
        if x < min_x:
            min_x = x
        if y < min_y:
            min_y = y
    return (min_x, min_y), (max_x, max_y)


def largest_box(points_1, points_2) -> tuple[tuple[int, int], tuple[int, int]]:
    largest_box = 0
    largest_box_points = None
    for p1 in points_1:
        for p2 in points_2:
            box_size = abs(p1[0] - p2[0] + 1) * abs(p1[1] - p2[1] + 1)
            if box_size > largest_box:
                largest_box = box_size
                largest_box_points = (p1, p2)
    return largest_box_points, largest_box


def part_1(entries: list[str]):
    top_left, top_right, bottom_left, bottom_right = quadrants(entries)
    candidate_sizes = list()

    if len(top_left) > 100:
        top_left_corner = quadrants(top_left)[0]
        bottom_right_corner = quadrants(bottom_right)[3]
        candidate_1, candidate_1_size = largest_box(top_left_corner, bottom_right_corner)
        candidate_sizes.append(candidate_1_size)

        top_right_corner = quadrants(top_right)[1]
        bottom_left_corner = quadrants(bottom_left)[2]
        candidate_2, candidate_2_size = largest_box(top_right_corner, bottom_left_corner)
        candidate_sizes.append(candidate_2_size)
    else:
        for q1, q2 in combinations(quadrants(entries), 2):
            candidate_box, candidate_box_size = largest_box(q1, q2)
            candidate_sizes.append(candidate_box_size)

    return max(candidate_sizes)


def part_2(entries: list[str]):
    print(len(entries))
    # bounds = Visualizer.boundaries(entries)
    # viz = Visualizer(boundaries=bounds, scale=0.01)
    # viz.draw_polyline(entries, color=COLORS[5], width=1)
    # viz.draw_line((entries[0], entries[-1]), color=COLORS[0], width=1)
    # viz.show()

    # Based on the visual the two points in the pac man's mouth are likely the two corners of the best boxes.
    # Check each half's sizes
    top_half = entries[:249]
    top_half_largest_box, top_half_largest_box_size = largest_box([top_half[-1],], top_half[:-1])
    print(top_half_largest_box, top_half_largest_box_size)
    bottom_half = entries[249:]
    bottom_half_largest_box, bottom_half_largest_box_size = largest_box([bottom_half[0],], bottom_half[1:])
    print(bottom_half_largest_box, bottom_half_largest_box_size)

    # For all candidates check if there isn't a point inside the box, likely the closest neighbours.


def read_puzzle_data(data_file: str) -> list:
    with open(data_file) as infile:
        return [[int(x) for x in line.strip().split(',')] for line in infile.readlines()]


assertions = {
    "Test 1": 50,
    "Part 1": None,
    "Test 2": None,
    "Part 2": None,
}
