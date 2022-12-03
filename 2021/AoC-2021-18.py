#!/usr/bin/env python3

"""Solution for Advent of Code challenge 2021 - Day 18"""

__author__ = "Serge Beaumont"
__date__ = "December 2021"

from math import floor

DEBUG = False


class Value(object):
    """Basically a Pair Null Object..."""
    def __init__(self, parent=None, value=0):
        self.children = list()
        self.value = value
        self.parent = parent

    def __str__(self):
        return f"{self.value}"

    @property
    def level(self):
        if self.parent:
            return self.parent.level + 1
        else:
            return 0

    @property
    def left(self):
        return self.value

    @property
    def right(self):
        return self.value

    @property
    def magnitude(self):
        return self.value

    def add_left(self, value):
        self.value += value

    def add_right(self, value):
        self.value += value

    def explode(self):
        return False

    def split(self):
        if self.value >= 10:
            new_pair = Pair(self.parent)
            new_pair.children.append(Value(new_pair, floor(self.value / 2)))
            new_pair.children.append(Value(new_pair, round(self.value / 2 + 0.5)))

            if self.parent.left == self:
                self.parent.left = new_pair
            else:
                self.parent.right = new_pair
            return True
        else:
            for child in self.children:
                if child.split():
                    return True
            return False


class Pair(Value):
    def __str__(self):
        level_text = f"{self.level}|" if DEBUG else ""
        if len(self.children) == 2:
            return f"[{level_text}{str(self.children[0])},{str(self.children[1])}]"
        elif len(self.children) == 1:
            return f"[{level_text}{str(self.children[0])}]"
        else:
            raise Exception("Pair must have children")

    @property
    def level(self):
        if self.parent:
            return self.parent.level + 1
        else:
            return 0

    @property
    def left(self):
        return self.children[0]

    @left.setter
    def left(self, value):
        self.children[0] = value

    @property
    def right(self):
        return self.children[-1]

    @right.setter
    def right(self, value):
        self.children[-1] = value

    @property
    def left_sibling(self):
        if self.parent:
            if self.parent.right == self:
                return self.parent.left
            else:
                return self.parent.left_sibling
        else:
            return None

    @property
    def right_sibling(self):
        if self.parent:
            if self.parent.left == self:
                return self.parent.right
            else:
                return self.parent.right_sibling
        else:
            return None

    @property
    def magnitude(self):
        left_magnitude = self.left.magnitude
        right_magnitude = self.right.magnitude
        result = left_magnitude * 3 + right_magnitude * 2
        return result

    def add_left(self, value):
        if len(self.children) >= 1:
            if isinstance(self.children[0], Pair):
                self.children[0].add_left(value)
            else:
                self.children[0].value += value

    def add_right(self, value):
        if len(self.children) >= 1:
            if isinstance(self.children[-1], Pair):
                self.children[-1].add_right(value)
            else:
                self.children[-1].value += value

    def explode(self):
        if self.level >= 4:
            if self.left_sibling:
                self.left_sibling.add_right(self.left.value)
            if self.right_sibling:
                self.right_sibling.add_left(self.right.value)
            if self.parent.left == self:
                self.parent.left = Value(self.parent, 0)
            else:
                self.parent.right = Value(self.parent, 0)
            return True
        else:
            if self.left.explode():
                return True
            else:
                return self.right.explode()


def build_pairs(entry, parent=None):
    if not parent:
        parent = Pair()
    for item in entry:
        if isinstance(item, list):
            new_child = Pair(parent)
            parent.children.append(new_child)
            build_pairs(item, new_child)
        else:
            parent.children.append(Value(parent, item))
    return parent


def add_snail_numbers(sn1, sn2):
    result = Pair()
    result.children.append(sn1)
    sn1.parent = result
    result.children.append(sn2)
    sn2.parent = result
    return result


def reduce(snail_tree):
    still_reducing = True
    while still_reducing:
        if not snail_tree.explode():
            if not snail_tree.split():
                still_reducing = False
            else:
                if DEBUG:
                    print("S ", snail_tree)
        else:
            if DEBUG:
                print("E ", snail_tree)


def part_1(entries):
    result = build_pairs(entries[0])
    for entry in entries[1:]:
        next_snail_number = build_pairs(entry)
        result = add_snail_numbers(result, next_snail_number)
        reduce(result)
    print(result, result.magnitude)

    return result.magnitude


def part_2(entries):
    return 0


def read_puzzle_data(file_number):
    with open(f"AoC-2021-{file_number}-input.txt") as infile:
        lines = [line.strip() for line in infile.readlines()]
        lines = [eval(line) for line in lines]
    return lines


if __name__ == '__main__':
    DAY = "18"

    test_result_part_1 = part_1(read_puzzle_data(f"{DAY}-test"))
    print("Test Part 1:", test_result_part_1)
    assert test_result_part_1 == 1384

    test_result_part_1 = part_1(read_puzzle_data(f"{DAY}-test-2"))
    print("Test Part 1:", test_result_part_1)
    assert test_result_part_1 == 4140

    print("     Part 1:", part_1(read_puzzle_data(DAY)))

    # test_result_part_2 = part_2(read_puzzle_data(f"{DAY}-test"))
    # print("Test Part 2:", test_result_part_2)
    # assert test_result_part_2 == 0
    #
    # print("     Part 2:", part_2(read_puzzle_data(DAY)))
