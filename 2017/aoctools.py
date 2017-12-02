def load_and_split_file(filename):
    with open(filename, 'r') as content_file:
        return [line.strip().split() for line in content_file]


def convert_to_ints(lines):
    return [[int(n) for n in line] for line in lines]
