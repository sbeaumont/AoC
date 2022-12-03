#!/usr/bin/env python3

"""Solution for Advent of Code challenge 2021 - Day 16"""

__author__ = "Serge Beaumont"
__date__ = "December 2021"

from math import prod

LITERAL_VALUE = 4
TYPES = ('+', '*', 'Min', 'Max', 'Val', '>', '<', '=')

# Literal (Type 4)
# VVVTTT100001000001111???
# 0  3  6

# Type 0 Bit length
# VVVTTTLMMMMMMMMMMMMMMMB
# 0  3  67              22

# Type 1 Count
# VVVTTTLMMMMMMMMMMMB
# 0  3  67          18


def is_empty(s: str) -> bool:
    return all([c == '0' for c in s]) or not s


class Packet(object):
    def __init__(self):
        self.version = None
        self.type_id = None
        self.length_id = None
        self.body = list()

    def __str__(self, level=0):
        result = "  " * level + f"{TYPES[self.type_id]} (V{self.version} l:{self.length_id})\n"
        for sub in self.body:
            if isinstance(sub, Packet):
                result += sub.__str__(level + 1)
            else:
                result += ("  " * (level + 1)) + str(sub) + "\n"
        return result

    def chomp(self, packet_string: str) -> str:
        self.version = int(packet_string[0:3], 2)
        self.type_id = int(packet_string[3:6], 2)

        if self.type_id == LITERAL_VALUE:
            packet_string = self.chomp_literal(packet_string[6:])
        else:
            self.length_id = int(packet_string[6])
            if self.length_id == 0:
                length = int(packet_string[7:22], 2)
                self.chomp_length(packet_string[22:22 + length])
                packet_string = packet_string[22 + length:]
            elif self.length_id == 1:
                packet_string = self.chomp_number(packet_string)
            else:
                raise Exception(f"Unknown length type id {self.type_id}")
        return packet_string

    def chomp_literal(self, packet_string: str) -> str:
        last_found = False
        bin_repr = ''
        while not last_found and not is_empty(packet_string):
            last_found = packet_string[0] == '0'
            bin_repr += packet_string[1:5]
            packet_string = packet_string[5:]
        self.body.append(int(bin_repr, 2))
        return packet_string

    def chomp_length(self, sub_string: str):
        while not is_empty(sub_string):
            sub_packet = Packet()
            sub_string = sub_packet.chomp(sub_string)
            self.body.append(sub_packet)

    def chomp_number(self, packet_string: str) -> str:
        num_packets = int(packet_string[7:18], 2)
        packet_string = packet_string[18:]
        for i in range(num_packets):
            sub_packet = Packet()
            packet_string = sub_packet.chomp(packet_string)
            self.body.append(sub_packet)
        return packet_string

    @property
    def value(self) -> int:
        if self.type_id == 0:
            # Sum
            return sum([p.value for p in self.body])
        elif self.type_id == 1:
            # Product
            return prod([p.value for p in self.body])
        elif self.type_id == 2:
            # Min
            return min([p.value for p in self.body])
        elif self.type_id == 3:
            # Max
            return max([p.value for p in self.body])
        elif self.type_id == 4:
            # Literal Value
            return self.body[0]
        elif self.type_id == 5:
            # Greater Than
            return 1 if self.body[0].value > self.body[1].value else 0
        elif self.type_id == 6:
            # Less Than
            return 1 if self.body[0].value < self.body[1].value else 0
        elif self.type_id == 7:
            # Equal To
            return 1 if self.body[0].value == self.body[1].value else 0
        else:
            raise Exception(f"Unknown type id {self.type_id}")


def to_bits(hexstring: str) -> str:
    return ''.join([bin(int(c, 16))[2:].zfill(4) for c in hexstring])


def part_1(entries: str, debug=False):
    def add_version_numbers(p: Packet) -> int:
        total = 0
        if p.type_id != LITERAL_VALUE:
            for sub_packet in p.body:
                total += add_version_numbers(sub_packet)
        return total + p.version

    packet = Packet()
    remaining_string = packet.chomp(to_bits(entries))
    if debug:
        print(packet)
        print(f"Remaining: {remaining_string}")
    return add_version_numbers(packet)


def part_2(entries: str, debug=False) -> int:
    packet = Packet()
    remaining = packet.chomp(to_bits(entries))
    if debug:
        print(packet)
        print(f"Remaining: {remaining}")
    return packet.value


def read_puzzle_data(file_number):
    with open(f"AoC-2021-{file_number}-input.txt") as infile:
        lines = [line.strip() for line in infile.readlines()]
    return lines


if __name__ == '__main__':
    DAY = "16"

    # for test_line in read_puzzle_data(f"{DAY}-test"):
    #     test_input, expected_output = test_line.split(',')
    #     # print(f"======\nTest Part 1 ({test_input} -> {expected_output})\n")
    #     test_result_part_1 = part_1(test_input)
    #     print(f"Test Part 1 ({test_input} -> {expected_output}):", test_result_part_1)
    #     assert test_result_part_1 == int(expected_output)
    #
    # result_part_1 = part_1(read_puzzle_data(DAY)[0])
    # print("     Part 1:", result_part_1)
    # assert result_part_1 == 904
    #
    # for test_line in read_puzzle_data(f"{DAY}-test-2"):
    #     test_input, expected_output = test_line.split(',')
    #     # print(f"======\nTest Part 2 ({test_input} -> {expected_output})\n")
    #     test_result_part_2 = part_2(test_input)
    #     print(f"Test Part 2 ({test_input} -> {expected_output}):", test_result_part_2)
    #     assert test_result_part_2 == int(expected_output)

    day_2_puzzle_data = read_puzzle_data(DAY)[0]
    part_2_result = part_2(day_2_puzzle_data, True)
    print("     Part 2:", part_2_result)
    # assert part_2_result > 200464296877
