from intcode_computer import Computer


with open("AoC-2019-input-13.txt") as f:
    data = [int(x) for x in f.read().strip().split(',')]

computer = Computer(data, pause_on_output=3)

blocks = set()
while not computer.on_fire:
    result = computer.run_program([])
    if result:
        blocks.add(tuple(result))

block_count = 0

for block in blocks:
    if block[2] == 2:
        block_count += 1

print(blocks)

print(block_count)
