from AoC201710 import full_knot_hash

PUZZLE_INPUT = 'jxqlasbh' # 8080 too low
TEST_INPUT = 'flqrgnkx'


def defrag(hash_input):
    grid = list()
    for i in range(128):
        inp = '{}-{}'.format(hash_input, i)
        kh = full_knot_hash([ord(c) for c in inp])
        assert len(kh) == 32
        grid.append("".join(["{0:04b}".format(int(c, 16)) for c in kh]))

    return grid


def count_used(grid):
    return reduce(lambda x, y: x + y, [row.count('1') for row in grid])


def print_grid(grid):
    for line in grid:
        print(line)

print("Test input has {} used sectors, should have 8108.".format(count_used(defrag(TEST_INPUT))))

grid = defrag(PUZZLE_INPUT)

print("Part 1: grid has {} used sectors".format(count_used(grid)))

print_grid(grid)