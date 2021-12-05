#!/usr/bin/env python3

"""Solution for Advent of Code challenge 2020 - Day 18"""

__author__ = "Serge Beaumont"
__date__ = "December 2020"

# import operator

with open("AoC-2020-18-input.txt") as infile:
    file_data = [line.strip().replace(' ', '') for line in infile.readlines()]

operands = ('+', '*')
# ops = {'+': (1, operator.add), '*': (1, operator.mul)}
# adv_ops = {'+': (2, operator.add), '*': (1, operator.mul)}


def infix_to_postfix(expr, advanced=False):
    result = list()
    stack = list()
    expr = expr.replace(' ', '')

    def top():
        return stack[-1] if len(stack) > 0 else None

    def precedence(token):
        if token == '+' and advanced:
            return 2
        elif token in operands:
            return 1
        else:
            return 0

    for c in expr:
        if c == '(':
            stack.append(c)
        elif c == ')':
            d = stack.pop()
            while d != '(':
                result.append(d)
                d = stack.pop()
        elif c in operands:
            # while top of stack has higher or equal (left-to-right) precedence, pop and append
            while top() in operands and precedence(top()) >= precedence(c):
                result.append(stack.pop())
            stack.append(c)
        else:
            result.append(int(c))
    while len(stack) > 0:
        result.append(stack.pop())
    return result


def evaluate_postfix_expression(expr):
    stack = list()
    for c in expr:
        if c in operands:
            right = stack.pop()
            left = stack.pop()
            if c == '+':
                stack.append(left + right)
            elif c == '*':
                stack.append(left * right)
            else:
                assert False
        else:
            stack.append(c)
    return stack.pop()


def do(expr_list, advanced=False):
    return sum([evaluate_postfix_expression(infix_to_postfix(e, advanced)) for e in expr_list])


part_1 = do(file_data)
print("Part 1:", part_1)
assert part_1 == 75592527415659

assert(do(['1 + (2 * 3) + (4 * (5 + 6))'], True)) == 51
assert(do(['2 * 3 + (4 * 5)'], True)) == 46
assert(do(['5 + (8 * 3 + 9 + 3 * 4 * 3)'], True)) == 1445
assert(do(['5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))'], True)) == 669060
assert(do(['((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2'], True)) == 23340

part_2 = do(file_data, True)
print("Part 2:", part_2)
assert part_2 == 360029542265462
