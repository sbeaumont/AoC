"""
Solution for Advent of Code challenge 2025

1.
"""

__author__ = "Serge Beaumont"
__date__ = "December 2025"

from functools import lru_cache
from itertools import batched


def part_1(entries: list[str]):
    wrong_ids = []
    for e in entries:
        start, end = [int(x) for x in e.split('-')]
        ids_to_test = [str(i) for i in range(start, end + 1) if (len(str(i)) % 2) == 0]
        for test_id in ids_to_test:
            middle = len(test_id) // 2
            left = test_id[:middle]
            right = test_id[middle:]
            if left == right:
                wrong_ids.append(test_id)
    return sum([int(_id) for _id in wrong_ids])


def part_2(entries: list[str]):
    """This solution gets all the divisors of each id's length - except for the length itself and then
    chunks the id into equal pieces per valid divisor, and then checks if all the pieces are the same."""
    wrong_ids = []
    for e in entries:
        start, end = [int(x) for x in e.split('-')]
        ids_to_test = [str(i) for i in range(start, end + 1)]
        for test_id in ids_to_test:
            for i in get_divisors(len(test_id)):
                chunks = list(batched(test_id, i))
                if len(set(chunks)) == 1:
                    wrong_ids.append(test_id)
                    break
    return sum([int(_id) for _id in wrong_ids])

@lru_cache
def get_divisors(n: int) -> list[int]:
    """Get divisors of n in reverse order without n itself.
    For the puzzle this tells you in how many ways a string can be divided into equal pieces.
    Example: string abcdef (length 6) can be split into chunks of size 1 (a b c d e f), 2 (ab cd ef) and 3 (abc def).
    Uses a cache do we don't recalculate this basic algoritm all the time."""
    n = abs(n)
    divisors = set()
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            divisors.add(i)
            divisors.add(n // i)
    return sorted(divisors, reverse=True)[1:]


def read_puzzle_data(data_file: str) -> list:
    with open(data_file) as infile:
        return [line.strip().split(',') for line in infile.readlines()][0]


assertions = {
    "Test 1": 1227775554,
    "Part 1": 19605500130,
    "Test 2": 4174379265,
    "Part 2": None,
}
