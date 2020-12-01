#!/usr/bin/env python3

"""Solution for Advent of Code challenge 2019 - Day 8"""

__author__ = "Serge Beaumont"
__date__ = "December 2019"

from norvigutils import BIG

PIC_SIZE = 6 * 25


def load_input(day):
    with open(f"AoC-2019-input-{day}.txt") as infile:
        return infile.read()


def do(data):
    assert len(data) % PIC_SIZE == 0
    least_zeroes = BIG
    layer_1x2 = None
    for i in range(len(data) // PIC_SIZE):
        start = i * PIC_SIZE
        end = i * PIC_SIZE + PIC_SIZE
        layer = data[start:end]
        layer_0 = layer.count('0')
        layer_1 = layer.count('1')
        layer_2 = layer.count('2')
        print(start, end, layer_0, layer_1, layer_2)
        if layer_0 < least_zeroes:
            layer_1x2 = layer_1 * layer_2
            least_zeroes = layer_0

    return layer_1x2


if __name__ == '__main__':
    data = load_input(8)
    result = do(data)
    print(f"Part 1: {result}")
    assert result == 1548