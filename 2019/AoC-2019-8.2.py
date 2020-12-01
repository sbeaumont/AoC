#!/usr/bin/env python3

"""Solution for Advent of Code challenge 2019 - Day 8"""

__author__ = "Serge Beaumont"
__date__ = "December 2019"

from norvigutils import transpose, cat
import re

PIC_WIDTH = 25
PIC_HEIGHT = 6


def pic_size(sizes):
    return sizes[0] * sizes[1]


def load_input(day):
    with open(f"AoC-2019-input-{day}.txt") as infile:
        return infile.read()


def to_layers(data, sizes):
    layers = list()
    for i in range(len(data) // pic_size(sizes)):
        size = pic_size(sizes)
        start = i * size
        end = i * size + size
        layers.append(data[start:end])
    return layers


def render_picture(data, sizes):
    picture = list()
    for stack in transpose(to_layers(data, sizes)):
        stack_no_transparency = re.sub('2', '', cat(stack))
        picture.append(stack_no_transparency[0])
    return picture


def print_picture(picture, sizes):
    for i in range(sizes[1]):
        start = i * sizes[0]
        end = start + sizes[0]
        print(cat(['\u2588' if c == '1' else ' ' for c in picture[start:end]]))


def do(data, sizes=(PIC_WIDTH, PIC_HEIGHT)):
    picture = render_picture(data, sizes)
    print_picture(picture, sizes)
    return picture


if __name__ == '__main__':
    assert do('0222112222120000', (2, 2)) == ['0', '1', '1', '0']
    print()

    data = load_input(8)
    do(data)
