#!/usr/bin/env python3

"""Solution for Advent of Code challenge 2018 - Day 8 part 2

"""

__author__ = "Serge Beaumont"
__date__ = "December 2018"

with open("AoC-2018-8-input.txt") as infile:
    tree = [int(node) for node in infile.read().split(' ')]


def tree_iterator():
    for node in tree:
        yield node


class Node(object):
    def __init__(self):
        self.children = list()
        self.metadata = list()

    def process(self, ti):
        children = next(ti)
        header = next(ti)
        for i in range(children):
            child = Node()
            self.children.append(child)
            child.process(ti)
        for j in range(header):
            self.metadata.append(next(ti))

    def value(self):
        total = 0
        if self.children:
            for m in self.metadata:
                idx = m - 1
                if (idx >= 0) and (idx < len(self.children)):
                    total += self.children[idx].value()
        else:
            total = sum(self.metadata)

        return total


root = Node()
root.process(tree_iterator())

print(f"Total is: {root.value()}")

assert root.value() == 22306
