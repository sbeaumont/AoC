PUZZLE_INPUT_FILE_NAME = "AoC-2017-13-input.txt"

# Parse parent and children names
with open(PUZZLE_INPUT_FILE_NAME) as puzzle_input_file:
    firewall = {int(line.split(":")[0]): int(line.split(":")[1]) for line in puzzle_input_file.readlines()}

max_depth = max(firewall, key=firewall.get)


def check_layers(wait_time):
    severity = 0
    for d, r in firewall.iteritems():
        at_layer_time = wait_time + d
        if at_layer_time % (2*r-2) == 0:
            severity += d * r
    return severity

print(check_layers(0))

# delay = 0
# sev = 1
# while sev:
#     pass