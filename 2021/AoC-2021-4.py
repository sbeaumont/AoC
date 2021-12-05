#!/usr/bin/env python3

"""Solution for Advent of Code challenge 2021 - Day X"""

__author__ = "Serge Beaumont"
__date__ = "December 2021"


def flatten_card(card):
    flat_card = list()
    for line in card:
        flat_card.append(line)
    for line in zip(*card):
        flat_card.append(list(line))
    return flat_card


def card_wins(flat_card, current_draw):
    result = False
    for j in range(len(flat_card)):
        if set(flat_card[j]).issubset(current_draw):
            result = True
            break
    return result


def card_score(card, matched_numbers):
    unmatched_numbers = set([val for sublist in card for val in sublist]) - set(matched_numbers)
    return matched_numbers[-1] * sum(unmatched_numbers)


def part_1(drawn_numbers, cards):
    max_draws = len(drawn_numbers)
    winning_card_score = 0

    for card in cards:
        flat_card = flatten_card(card)
        for i in range(5, len(drawn_numbers)):
            current_draw = set(drawn_numbers[:i])
            if card_wins(flat_card, current_draw):
                if i < max_draws:
                    max_draws = i
                    winning_card_score = card_score(card, drawn_numbers[:i])
                break

    return winning_card_score


def part_2(drawn_numbers, cards):
    min_draws = 0
    winning_card_score = 0

    for card in cards:
        flat_card = flatten_card(card)
        for i in range(5, len(drawn_numbers)):
            current_draw = set(drawn_numbers[:i])
            if card_wins(flat_card, current_draw):
                if i > min_draws:
                    min_draws = i
                    winning_card_score = card_score(card, drawn_numbers[:i])
                break

    return winning_card_score


def read_puzzle_data(file_number):
    with open(f"AoC-2021-{file_number}-input.txt") as infile:
        lines = [line.strip() for line in infile.readlines()]

    drawn_numbers = [int(c) for c in lines[0].split(',')]

    bingo_cards = list()
    for bingo_card_start in range(2, len(lines), 6):
        bingo_card = list()
        for i in range(bingo_card_start, bingo_card_start + 5):
            bingo_card.append([int(c) for c in lines[i].split()])
        bingo_cards.append(bingo_card)

    return drawn_numbers, bingo_cards


if __name__ == '__main__':
    DAY = "4"

    test_result_part_1 = part_1(*read_puzzle_data(f"{DAY}-test"))
    print("Test Part 1", test_result_part_1)
    assert test_result_part_1 == 4512

    print("Part 1", part_1(*read_puzzle_data(DAY)))

    test_result_part_2 = part_2(*read_puzzle_data(f"{DAY}-test"))
    print("Test Part 2", test_result_part_2)
    assert test_result_part_2 == 1924

    print("Part 2", part_2(*read_puzzle_data(DAY)))
