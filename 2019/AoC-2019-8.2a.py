#!/usr/bin/env python3

"""Solution for Advent of Code challenge 2019 - Day 8"""

__author__ = "Serge Beaumont"
__date__ = "December 2019"

from norvigutils import transpose, cat, load_input
import re

PIC_WIDTH = 25
PIC_HEIGHT = 6


class Picture(object):
    def __init__(self, layers, width, height):
        self.layers = layers
        self.width = width
        self.height = height

    @classmethod
    def from_string(cls, data, width, height):
        sz = width * height
        layers = list()
        for i in range(len(data) // sz):
            start = i * sz
            end = i * sz + sz
            layers.append(data[start:end])
        return cls(layers, width, height)

    @property
    def size(self):
        return self.width * self.height

    @property
    def rendered(self):
        rendered_pixels = list()
        for stack in transpose(self.layers):
            stack_no_transparency = re.sub('2', '', cat(stack))
            rendered_pixels.append(stack_no_transparency[0])
        return self.layer_to_lines(rendered_pixels)

    def layer_to_lines(self, layer):
        lines = list()
        for i in range(self.height):
            lines.append(cat(layer[i * self.width: i * self.width + self.width]))
        return lines


def print_layer(layer):
    for line in layer:
        print(cat(['X' if c == '1' else ' ' for c in line]))


def do(data, width, height):
    picture = Picture.from_string(data, width, height)
    return picture.rendered


if __name__ == '__main__':
    test_render = do('0222112222120000', 2, 2)
    assert test_render == ['01', '10']
    pic = do(load_input(8, False), PIC_WIDTH, PIC_HEIGHT)

    print("\nRendered picture\n")
    for line in pic:
        print(line)

    print("\nPrinted picture\n")
    print_layer(pic)
