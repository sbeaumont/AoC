"""Solution for Advent of Code challenge 2024"""

__author__ = "Serge Beaumont"
__date__ = "December 2024"


def create_blocks(disk_map):
    blocks = list()
    file_id = 0
    for i in range(0, len(disk_map), 2):
        blocks.extend([file_id,] * int(disk_map[i]))
        if i + 1 < len(disk_map):
            blocks.extend([-1] * int(disk_map[i+1]))
        file_id += 1
    return blocks

def compress(blocks):
    while -1 in blocks:
        item = blocks.pop()
        blocks[blocks.index(-1)] = item
        while blocks[-1] == -1:
            blocks.pop()
    return blocks

def checksum(blocks):
    result = 0
    for i in range(len(blocks)):
        if blocks[i] > -1:
            result += i * blocks[i]
    return result

def block_string(blocks):
    return ''.join(['.' if x == -1 else str(x) for x in blocks])

def part_1(disk_map: str):
    blocks = create_blocks(disk_map)
    blocks = compress(blocks)
    return checksum(blocks)

def part_2(disk_map):
    def empty_space(size):
        for i in range(len(blocks)):
            if (blocks[i] == -1) and blocks[i:i + size] == [-1, ] * size:
                return i
        return -1

    def find_file(f_id):
        idx = blocks.index(f_id)
        size = 0
        j = idx
        while j < len(blocks) and (blocks[j] == f_id):
            size += 1
            j += 1
        return idx, size

    def move_file(idx, size):
        idx = empty_space(size)
        if (idx > 0) and (idx < file_index):
            for k in range(size):
                blocks[idx + k] = blocks[file_index + k]
                blocks[file_index + k] = -1

    blocks = create_blocks(disk_map)
    # print(block_string(blocks))
    for file_id in range(max(blocks), 0, -1):
        file_index, size = find_file(file_id)
        move_file(file_index, size)
        # print(block_string(blocks))
    return checksum(blocks)

def read_puzzle_data(data_file: str) -> str:
    with open(data_file) as infile:
        return infile.read().strip()

assertions = {
    "Test 1": 1928,
    "Part 1": 6463499258318,
    "Test 2": 2858,
    "Part 2": 6493634986625,
}
