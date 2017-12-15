PUZZLE_INPUT_FILE_NAME = "AoC-2017-13-input.txt"

# Parse parent and children names
with open(PUZZLE_INPUT_FILE_NAME) as puzzle_input_file:
    layers = {int(line.split(":")[0]): int(line.split(":")[1]) for line in puzzle_input_file.readlines()}


def run_firewall(delay, firewall):
    severity = 0
    for picosecs in range(delay, 100 + delay):
        layer = picosecs - delay
        if layer in firewall:
            loop_pos = picosecs % (firewall[layer] * 2 - 2)
            pos = firewall[layer] - abs(firewall[layer] - loop_pos)
            if not pos:
                severity += layer * firewall[layer]
    return severity


test_firewall = {0: 3, 1: 2, 4: 4, 6: 4}
print("Test firewall has severity {}".format(run_firewall(0, test_firewall)))


print("Part 1: Severity is {}".format(run_firewall(0, layers)))

wait = 0
sev = 1
while sev:
    sev = run_firewall(wait, layers)
    if not sev or wait % 50000 == 0:
        print("Part 2: Delay {} leads to severity {}".format(wait, sev))
    wait += 1


# not delay: 54, 53, 259572 too low

