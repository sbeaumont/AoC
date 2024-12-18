#!/usr/bin/env python3

"""Solution for Advent of Code challenge 2018 - Day 4

Totally YOLO edition.

[1518-02-10 23:56] Guard #1487 begins shift
[1518-02-11 00:14] falls asleep
[1518-02-11 00:40] wakes up

"""

__author__ = "Serge Beaumont"
__date__ = "December 2018"

import numpy as np
import re

re_line = re.compile("\[(.*)\] (.*)")
with open("AoC-2018-4-input.txt") as infile:
    lines = sorted([re_line.match(line.strip()).groups() for line in infile])

guards = dict()

re_shift_start = re.compile("Guard #(\d+)")
sleeping = False

for line in lines:
    # Check for new guard, add to dict if not present
    shift_match = re_shift_start.match(line[1])
    if shift_match:
        # Handle old sleeping guard
        if sleeping:
            sleeping = False
            current_guard[sleep_time:] += 1

        # Set new guard
        current_guard_id = int(shift_match.group(1))
        if current_guard_id in guards:
            current_guard = guards[current_guard_id]
        else:
            current_guard = np.zeros(60)
            guards[current_guard_id] = current_guard
    else:
        # Handle sleeping and waking
        if line[1] == "falls asleep":
            sleeping = True
            sleep_time = int(re.search(":(\d+)$", line[0]).group(1))
        elif line[1] == "wakes up":
            assert sleeping
            sleeping = False
            wake_time = int(re.search(":(\d+)$", line[0]).group(1))
            current_guard[sleep_time: wake_time] += 1

max_sleep = 0
for guard_id, guard_sleeps in guards.items():
    if sum(guard_sleeps) > max_sleep:
        sleepy_guard_id = guard_id
        max_sleep = sum(guard_sleeps)

sleepy_guard_sleep = guards[sleepy_guard_id]
minute = list(sleepy_guard_sleep).index(max(sleepy_guard_sleep))

print(f"Part 1: Guard ID {sleepy_guard_id} * Minute {minute} = {sleepy_guard_id * minute}")

max_sleep = 0
for guard_id, guard_sleeps in guards.items():
    if max(guard_sleeps) > max_sleep:
        sleepy_guard_id = guard_id
        max_sleep = max(guard_sleeps)
        minute = list(guard_sleeps).index(max_sleep)

print(f"\nPart 2: Guard {sleepy_guard_id} slept the most with {max_sleep} minutes at minute {minute}")
print(f"Part 2 answer: {sleepy_guard_id * minute}")

assert sleepy_guard_id * minute == 117061
