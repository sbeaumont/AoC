#!/usr/bin/env python3

"""Solution for Advent of Code challenge 2017

[---](http://adventofcode.com/2017/day/10)"""


PUZZLE_INPUT = "76,1,88,148,166,217,130,0,128,254,16,2,130,71,255,229"
PART_TWO_END_SEQUENCE = [17, 31, 73, 47, 23]
STRING_LENGTH = 256


def reverse_slice(li, position, length):
    assert length <= len(li)
    if (position + length) < len(li):
        high = position + length
        low = position
        slc = li[low:high]
        slc.reverse()
        return li[:low] + slc + li[high:]
    else:
        low = (position + length) % len(li)
        high = position
        slc = li[high:] + li[:low]
        slc.reverse()
        slc_split_index = len(li) - high
        return slc[slc_split_index:] + li[low:high] + slc[:slc_split_index]


def knot_hash(s, lengths, current_position=0, skip_size=0):
    for l in lengths:
        s = reverse_slice(s, current_position, l)
        current_position = (current_position + l + skip_size) % len(s)
        skip_size += 1
        # print("Pos {:4d} Skip {:4d}: {}".format(current_position, skip_size, s))

    return s, current_position, skip_size


def full_knot_hash(sequence):
    position = 0
    skip_size = 0
    s = range(STRING_LENGTH)
    for i in range(64):
        s, position, skip_size = knot_hash(s, sequence, position, skip_size)
    dense_hash = [reduce(lambda x, y: x ^ y, s[r*16:r*16+16]) for r in range(16)]
    return "".join(["{:02x}".format(n) for n in dense_hash])


if __name__ == '__main__':
    # Tests
    test_string = list(range(1, 6))
    assert reverse_slice(test_string, 0, 3) == [3, 2, 1, 4, 5]
    assert reverse_slice(test_string, 1, 3) == [1, 4, 3, 2, 5]
    assert reverse_slice(test_string, 0, 5) == [5, 4, 3, 2, 1]
    assert reverse_slice(test_string, 4, 4) == [2, 1, 5, 4, 3]
    assert reverse_slice([4, 3, 0, 1, 2], 1, 5) == [3, 4, 2, 1, 0]
    assert knot_hash(range(5), (3, 4, 1, 5))[0] == [3, 4, 2, 1, 0]

    # Part 1
    p_input = [int(i) for i in PUZZLE_INPUT.split(',')]
    k_hash = knot_hash(range(STRING_LENGTH), p_input)
    print("Current position: {}, skip size: {}.".format(k_hash[1], k_hash[2]))
    st = k_hash[0]
    print("Part 1: The first two numbers are {} and {}, their product is {}.".format(st[0], st[1], st[0] * st[1]))

    # Part 2
    seq = [ord(c)for c in PUZZLE_INPUT] + PART_TWO_END_SEQUENCE
    solution = full_knot_hash(seq)

    print("\nPart 2: {}".format(solution))

    assert solution == '4db3799145278dc9f73dcdbc680bd53d'
