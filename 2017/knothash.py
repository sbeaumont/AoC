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
        s, position, skip_size = knot_hash(s, sequence + PART_TWO_END_SEQUENCE, position, skip_size)
    dense_hash = [reduce(lambda x, y: x ^ y, s[r*16:r*16+16]) for r in range(16)]
    return "".join(["{:02x}".format(n) for n in dense_hash])