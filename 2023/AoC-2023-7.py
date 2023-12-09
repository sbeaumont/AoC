#!/usr/bin/env python3

"""Solution for Advent of Code challenge 2023 - Day 7"""

__author__ = "Serge Beaumont"
__date__ = "December 2023"

import sys
from collections import Counter


def hand_type(hand, with_jokers=False):
    labels = Counter(hand)
    joker_label = 0

    match len(labels):
        case 5: # High card (1)
            # One Joker: High (1) => One Pair (2)
            result = 2 if with_jokers and labels.get(joker_label, 0) else 1
        case 4: # One Pair (2)
            # One Joker: two of a kind (2) => three of a kind (4)
            # The pair are two Jokers: => also three of a kind
            result = 4 if with_jokers and labels.get(joker_label, 0) else 2
        case 3: # Two pair (3) or Three of a Kind (4)
            if max(labels.values()) == 3:
                # Three of a kind
                result = 4
                if with_jokers and labels.get(joker_label, 0):
                    # The three of a kind are the jokers => can make four of a kind
                    # Single card is a joker => four of a kind
                    result = 6
            else:
                # Two pair
                result = 3
                if with_jokers and labels.get(joker_label, 0):
                    # A pair are the jokers => can make four of a kind
                    # The single card is a joker => can make full house
                    result = 6 if labels[joker_label] == 2 else 5
        case 2: # Full house (5) or Four of a Kind (6)
            result = 6 if max(labels.values()) == 4 else 5
            if with_jokers and labels.get(joker_label, 0):
                # One of the labels is a joker => five of a kind
                result = 7
        case 1: # Five of a Kind
            result = 7
        case _:
            raise Exception("Can't find hand type")
    return result


def all_hand_types(entries, labels_to_values, with_jokers=False):
    hands = dict()
    for e in entries:
        hand, bid = e.split()
        hand = [labels_to_values[c] for c in hand]
        hand.insert(0, hand_type(hand, with_jokers))
        hands[tuple(hand)] = int(bid)
    return hands


def total_winnings(hands):
    total = 0
    for i, key in enumerate(sorted(hands.keys())):
        total += (i + 1) * hands[key]
    return total


def part_1(entries):
    labels_to_values = {'1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'T': 10, 'J': 11,
                        'Q': 12, 'K': 13, 'A': 14}
    hands = all_hand_types(entries, labels_to_values)
    return total_winnings(hands)


def part_2(entries):
    labels_to_values = {'J': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'T': 10,
                        'Q': 12, 'K': 13, 'A': 14}
    hands = all_hand_types(entries, labels_to_values, True)
    return total_winnings(hands)


def read_puzzle_data(file_number):
    with open(f"AoC-2023-{file_number}-input.txt") as infile:
        lines = [line.strip() for line in infile.readlines()]
    return lines


if __name__ == '__main__':
    DAY = sys.argv[0].split('.')[0].split('-')[-1]
    print("Results for day", DAY)

    test_result_part_1 = part_1(read_puzzle_data(f"{DAY}-test"))
    print("Test Part 1:", test_result_part_1)
    assert test_result_part_1 == 6440

    print("     Part 1:", part_1(read_puzzle_data(DAY)))

    test_result_part_2 = part_2(read_puzzle_data(f"{DAY}-test"))
    print("Test Part 2:", test_result_part_2)
    assert test_result_part_2 == 5905

    result_part_2 = part_2(read_puzzle_data(DAY))
    print("     Part 2:", result_part_2)
    assert result_part_2 == 248747492