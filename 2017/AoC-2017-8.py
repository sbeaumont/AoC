PUZZLE_INPUT_FILE_NAME = "AoC-2017-8-input.txt"

with open(PUZZLE_INPUT_FILE_NAME, 'r') as puzzle_input_file:
    my_vars = dict()
    max_vars = dict()
    for line in puzzle_input_file.readlines():
        line_parts = line.strip().split()
        cond_expr = "{} {} {}".format(my_vars.get(line_parts[4], 0), line_parts[5], line_parts[6])
        conditional_var = my_vars.get(line_parts[4], 0)
        if eval(cond_expr):
            print(line_parts[4], conditional_var, int(line_parts[2]))
            v = line_parts[0]
            if line_parts[1] == 'inc':
                my_vars[v] = my_vars.get(v, 0) + int(line_parts[2])
            else:
                my_vars[v] = my_vars.get(v, 0) - int(line_parts[2])
            if my_vars[v] > max_vars.get(v, 0):
                max_vars[v] = my_vars[v]

print(my_vars)
print(max([int(s) for s in my_vars.values()]))
print(max([int(s) for s in max_vars.values()]))
