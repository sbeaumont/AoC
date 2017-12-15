from AoC_2017_10 import full_knot_hash

PUZZLE_INPUT = 'jxqlasbh' # 8080 too low
TEST_INPUT = 'flqrgnkx'

def defrag(hash_input):
    used = 0
    for i in range(128):
        inp = '{}-{}'.format(hash_input, i)
        kh = full_knot_hash([ord(c) for c in inp])
        assert len(kh) == 32
        row = "".join(["{0:04b}".format(int(c, 16)) for c in kh])
        used += row.count('1')
        #print(inp, row.count('1'), row)

    return used

print("Test input has {} used sectors, should have 8108.".format(defrag(TEST_INPUT)))
print("Part 1: grid has {} used sectors".format(defrag(PUZZLE_INPUT)))
