#!/usr/bin/env python3

"""Solution for Advent of Code challenge 2018 - Day 2 Part 2"""

__author__ = "Serge Beaumont"
__date__ = "December 2018"


def get_levenshtein_distance(word1, word2):
    """
    Copied from https://medium.com/@yash_agarwal2/soundex-and-levenshtein-distance-in-python-8b4b56542e9e

    Alse see https://en.wikipedia.org/wiki/Levenshtein_distance
    """
    word2 = word2.lower()
    word1 = word1.lower()
    matrix = [[0 for x in range(len(word2) + 1)] for x in range(len(word1) + 1)]

    for x in range(len(word1) + 1):
        matrix[x][0] = x
    for y in range(len(word2) + 1):
        matrix[0][y] = y

    for x in range(1, len(word1) + 1):
        for y in range(1, len(word2) + 1):
            if word1[x - 1] == word2[y - 1]:
                matrix[x][y] = min(
                    matrix[x - 1][y] + 1,
                    matrix[x - 1][y - 1],
                    matrix[x][y - 1] + 1
                )
            else:
                matrix[x][y] = min(
                    matrix[x - 1][y] + 1,
                    matrix[x - 1][y - 1] + 1,
                    matrix[x][y - 1] + 1
                )

    return matrix[len(word1)][len(word2)]


with open("AoC-2018-input-2.txt") as infile:
    box_ids = sorted([line.strip() for line in infile.readlines()])

for i in range(len(box_ids)):
    if get_levenshtein_distance(box_ids[i], box_ids[i+1]) == 1:
        print("Levenshtein distance is 1 between:")
        print("{} and".format(box_ids[i]))
        print(box_ids[i+1])
        print("\nThe common characters are:")
        print (''.join([c1 for c1, c2 in zip(box_ids[i], box_ids[i+1]) if c1 == c2]))
        break

