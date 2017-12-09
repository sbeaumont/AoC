


PUZZLE_INPUT_FILE_NAME = "AoC-2017-9-input.txt"


level = 0
in_garbage = False
skip = False
score = 0
garbage_count = 0
with open(PUZZLE_INPUT_FILE_NAME, 'r') as puzzle_input_file:
    for c in puzzle_input_file.read():
        if skip:
            skip = False
        elif c == '!':
            skip = True
        elif not in_garbage:
            if c == '{':
                level += 1
            elif c == '}':
                score += level
                level -= 1
            elif c == '<':
                in_garbage = True
        elif in_garbage:
            if c == '>':
                in_garbage = False
            else:
                garbage_count += 1

print(score, garbage_count)
