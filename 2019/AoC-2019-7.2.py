from norvigutils import load_input
from intcode_computer import Computer
from itertools import permutations, cycle


def load_program():
    return [int(x) for x in load_input(7, False).split(',')]


def phase_settings():
    return permutations((5, 6, 7, 8, 9), 5)


def run_amplifiers(program, settings):
    amplifiers = [Computer(program, setting, True) for setting in settings]
    current_amp = cycle(range(len(amplifiers)))
    signal = 0
    while not amplifiers[-1].halted:
        amp = amplifiers[next(current_amp)]
        amp.run_program((signal,))
        signal = amp.last_output()
    return signal


def find_max_output(program):
    max_thruster_signal = 0
    max_thruster_settings = None
    for settings in phase_settings():
        signal = run_amplifiers(program, settings)
        if signal > max_thruster_signal:
            max_thruster_signal = signal
            max_thruster_settings = settings
    return max_thruster_settings, max_thruster_signal


if __name__ == '__main__':
    result1 = find_max_output(
        [3, 26, 1001, 26, -4, 26, 3, 27, 1002, 27, 2, 27, 1, 27, 26, 27, 4, 27, 1001, 28, -1, 28, 1005, 28, 6, 99, 0, 0,
         5])
    assert result1 == ((9, 8, 7, 6, 5), 139629729), f"Result 1: {result1}"
    result2 = find_max_output(
        [3, 52, 1001, 52, -5, 52, 3, 53, 1, 52, 56, 54, 1007, 54, 5, 55, 1005, 55, 26, 1001, 54, -5, 54, 1105, 1, 12, 1,
         53, 54, 53, 1008, 54, 0, 55, 1001, 55, 1, 55, 2, 53, 55, 53, 4, 53, 1001, 56, -1, 56, 1005, 56, 6, 99, 0, 0, 0,
         0, 10])
    assert result2 == ((9, 7, 8, 5, 6), 18216), f"Result 2: {result2}"

    result = find_max_output(load_program())
    print(f"Part 2: settings {result[0]} lead to maximum output {result[1]}.")
