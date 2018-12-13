#!/usr/bin/env python3

"""Solution for Advent of Code challenge 2017 - Day 18"""

__author__ = "Serge Beaumont"
__date__ = "December 2018"

import time
from collections import defaultdict
from collections import deque

start = time.time()


with open("AoC-2017-18-input.txt") as infile:
    puzzle_code = ([line.strip().split() for line in infile])


class Program(object):
    def __init__(self, prog_id, code):
        self.prog_id = prog_id
        self.code = code

        self.registers = defaultdict(int)
        self.registers['p'] = prog_id

        self.send_queue = None
        self.recv_queue = deque()

        self.instruction_pointer = 0
        self.is_waiting = False
        self.num_values_sent = 0

    def is_terminated(self):
        return 0 > self.instruction_pointer >= len(self.code)

    def register_or_value(self, term):
        if term.lstrip("-").isdigit():
            return int(term)
        else:
            return int(self.registers[term])

    def tick(self):
        if not self.is_terminated():
            instruction = self.code[self.instruction_pointer]
            #print(f"Program {self.prog_id} executing {instruction}")
            keyword = instruction[0]
            if keyword == 'snd':
                assert self.send_queue is not None
                self.send_queue.appendleft(self.register_or_value(instruction[1]))
                self.instruction_pointer += 1
                self.num_values_sent += 1
            elif keyword == 'set':
                self.registers[instruction[1]] = self.register_or_value(instruction[2])
                self.instruction_pointer += 1
            elif keyword == 'add':
                self.registers[instruction[1]] += self.register_or_value(instruction[2])
                self.instruction_pointer += 1
            elif keyword == 'mul':
                self.registers[instruction[1]] *= self.register_or_value(instruction[2])
                self.instruction_pointer += 1
            elif keyword == 'mod':
                self.registers[instruction[1]] = self.registers[instruction[1]] % self.register_or_value(instruction[2])
                self.instruction_pointer += 1
            elif keyword == 'rcv':
                self.is_waiting = len(self.recv_queue) == 0
                if not self.is_waiting:
                    self.registers[instruction[1]] = self.recv_queue.pop()
                    self.instruction_pointer += 1
            elif keyword == 'jgz':
                if self.register_or_value(instruction[1]) > 0:
                    self.instruction_pointer += self.register_or_value(instruction[2])
                else:
                    self.instruction_pointer += 1


def test_snd():
    prog = Program(0, [('snd', '1')])
    prog.send_queue = deque()
    prog.tick()
    assert prog.is_terminated()
    assert prog.send_queue.pop() == 1


def test_rcv():
    prog = Program(0, [('rcv', 'a'), ('rcv', 'b')])
    prog.recv_queue.appendleft(1)
    prog.tick()
    assert prog.registers['a'] == 1
    assert prog.instruction_pointer == 1
    prog.tick()
    assert prog.is_waiting
    assert prog.instruction_pointer == 1
    prog.recv_queue.appendleft(2)
    prog.tick()
    assert not prog.is_waiting
    assert prog.registers['b'] == 2
    assert prog.instruction_pointer == 2
    assert prog.is_terminated()


def test_set():
    prog = Program(0, [('set', 'a', '1'), ('set', 'a', '3')])
    prog.tick()
    assert prog.registers['a'] == 1
    assert prog.instruction_pointer == 1
    prog.tick()
    assert prog.registers['a'] == 3
    assert prog.instruction_pointer == 2
    assert prog.is_terminated()


def test_mod():
    prog = Program(0, [('set', 'a', '8'), ('set', 'b', '3'), ('mod', 'a', 'b')])
    prog.tick()
    assert prog.registers['a'] == 8
    prog.tick()
    assert prog.registers['b'] == 3
    prog.tick()
    assert prog.registers['a'] == 2


def test_jgz():
    prog = Program(0, [('jgz', 'a', '-1000'), ('set', 'a', '1'), ('jgz', 'a', '-2')])
    prog.tick()
    assert prog.instruction_pointer == 1
    assert not prog.is_terminated()
    prog.tick()
    assert prog.instruction_pointer == 2
    prog.tick()
    assert prog.instruction_pointer == 0
    prog.tick()
    assert prog.instruction_pointer == -1000
    assert prog.is_terminated()


def test_mul():
    prog = Program(0, [('set', 'a', '-1000'), ('set', 'b', '-2'), ('mul', 'a', 'b')])
    prog.tick()
    prog.tick()
    prog.tick()
    assert prog.registers['a'] == 2000


def do_puzzle():
    prog0 = Program(0, puzzle_code)
    prog1 = Program(1, puzzle_code)
    prog0.send_queue = prog1.recv_queue
    prog1.send_queue = prog0.recv_queue

    while True:
        if prog0.is_terminated() and prog1.is_terminated():
            print("Both programs terminated")
            break
        if prog0.is_waiting and prog1.is_waiting:
            print("Deadlock. Stopping.")
            break
        prog0.tick()
        prog1.tick()

    print(f"Program 1 sent a value {prog1.num_values_sent} times.")


print(f"{time.time() - start:.4f} seconds to run.")

if __name__ == '__main__':
    #test_snd()
    #test_rcv()
    #test_set()
    #test_jgz()
    #test_mod()
    #test_mul()
    do_puzzle()
