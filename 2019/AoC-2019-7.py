from norvigutils import load_input
from intcode_computer import Computer
from itertools import permutations


def load_program():
    return [int(x) for x in load_input(7, False).split(',')]


def phase_settings():
    return permutations((0, 1, 2, 3, 4), 5)


def run_amplifiers(program, settings, input_signal=0):
    for setting in settings:
        computer = Computer(program, setting)
        output_value = computer.run_program([input_signal])
        input_signal = output_value
    return output_value


def find_max_output(program):
    max_thruster_signal = 0
    max_thruster_settings = None
    for settings in phase_settings():
        thruster_signal = run_amplifiers(program, settings)
        if thruster_signal > max_thruster_signal:
            max_thruster_signal = thruster_signal
            max_thruster_settings = settings
    return max_thruster_settings, max_thruster_signal


if __name__ == '__main__':
    result1 = find_max_output([3, 15, 3, 16, 1002, 16, 10, 16, 1, 16, 15, 15, 4, 15, 99, 0, 0])
    assert result1 == ((4, 3, 2, 1, 0), 43210), f"Result 1: {result1}"
    result2 = find_max_output(
        [3, 23, 3, 24, 1002, 24, 10, 24, 1002, 23, -1, 23, 101, 5, 23, 23, 1, 24, 23, 23, 4, 23, 99, 0, 0])
    assert result2 == ((0, 1, 2, 3, 4), 54321), f"Result 2: {result2}"
    result3 = find_max_output(
        [3, 31, 3, 32, 1002, 32, 10, 32, 1001, 31, -2, 31, 1007, 31, 0, 33, 1002, 33, 7, 33, 1, 33, 31, 31, 1, 32, 31,
         31, 4, 31, 99, 0, 0, 0])
    assert result3 == ((1, 0, 4, 3, 2), 65210), f"Result 3: {result3}"

    result = find_max_output(load_program())
    print(f"Part 1: settings {result[0]} lead to maximum output {result[1]}.")
