#!/usr/bin/env python3

"""Solution for Advent of Code challenge 2022 - Day X"""

__author__ = "Serge Beaumont"
__date__ = "December 2022"

from pprint import pprint


def part_1(entries):
    small_dir_sizes = 0
    filesystem = {'/': {'subs': {}, 'size': 0, 'parent': None, 'name': '/'}}
    dir_sizes = {}
    current = filesystem['/']
    for line in entries[1:]:
        if line.startswith('$ cd'):
            dir_name = line.split(' ')[2]
            if dir_name == '..':
                if current['size'] <= 100000:
                    small_dir_sizes += current['size']
                current['parent']['size'] += current['size']
                dir_sizes[current['name']] = current['size']
                current = current['parent']
            else:
                current = current['subs'][dir_name]
        elif line.startswith('dir'):
            dir_name = line.split(' ')[1]
            current['subs'][dir_name] = {'subs': {}, 'size': 0, 'parent': current, 'name': dir_name}
        elif line.split(' ')[0].isnumeric():
            current['size'] += int(line.split(' ')[0])

    while current != filesystem['/']:
        if current['size'] <= 100000:
            small_dir_sizes += current['size']
        if current['parent']:
            current['parent']['size'] += current['size']
        dir_sizes[current['name']] = current['size']
        current = current['parent']

    dir_sizes['/'] = filesystem['/']['size']

    return small_dir_sizes, dir_sizes


def part_2(dir_sizes):
    unused_space = 70000000 - dir_sizes['/']
    need_space = 30000000 - unused_space
    smallest_dir = 70000000
    smallest_dir_name = ''
    for dir_name, size in dir_sizes.items():
        if need_space <= size <= smallest_dir:
            smallest_dir = size
            smallest_dir_name = dir_name
    return smallest_dir_name, smallest_dir


def read_puzzle_data(file_number):
    with open(f"AoC-2022-{file_number}-input.txt") as infile:
        lines = [line.strip() for line in infile.readlines()]
    return lines


if __name__ == '__main__':
    DAY = "7"

    test_result_part_1, test_dir_sizes = part_1(read_puzzle_data(f"{DAY}-test"))
    print("Test Part 1:", test_result_part_1)
    assert test_result_part_1 == 95437

    result_part_1, p1_dir_sizes = part_1(read_puzzle_data(DAY))
    print("     Part 1:", result_part_1)
    assert result_part_1 == 1582412

    test_result_part_2 = part_2(test_dir_sizes)
    print("Test Part 2:", test_result_part_2)
    assert test_result_part_2[1] == 24933642

    result_part_2 = part_2(p1_dir_sizes)
    print("     Part 2:", result_part_2)
    assert result_part_2[1] == 3696336