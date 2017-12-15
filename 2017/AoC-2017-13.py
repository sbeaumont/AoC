PUZZLE_INPUT_FILE_NAME = "AoC-2017-13-input.txt"

# Parse parent and children names
with open(PUZZLE_INPUT_FILE_NAME) as puzzle_input_file:
    layers = {int(line.split(":")[0]): int(line.split(":")[1]) for line in puzzle_input_file.readlines()}

print(layers)


def run_firewall(delay):
    severity = 0
    for picosecs in range(delay, 93+delay):
        layer = picosecs - delay
        if layers.has_key(layer):
            loop_pos = picosecs % (layers[layer] * 2 - 2)
            pos = layers[layer] - abs(layers[layer] - loop_pos)
            if not pos:
                severity += picosecs * layers[layer]
            #print(picosecs, layers[picosecs], loop_pos, pos)

    #print(delay, severity)
    return severity

print("Part 1: Severity is {}".format(run_firewall(0)))

delay = 0
severity = 1
while severity:
    severity = run_firewall(delay)
    print("Delay {} leads to severity {}".format(delay, severity))
    delay += 1

print("Delay {} leads to severity {}".format(delay - 1, severity))

# not delay: 54, 53