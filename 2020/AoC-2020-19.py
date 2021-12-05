#!/usr/bin/env python3

"""Solution for Advent of Code challenge 2020 - Day 19"""

__author__ = "Serge Beaumont"
__date__ = "December 2020"

import re


def load(filename):
    with open(filename) as infile:
        file_data = [line.strip() for line in infile.readlines()]
        split_index = file_data.index('')
        rules = {r[0]: r[1].strip() for r in [line.split(':') for line in file_data[:split_index]]}
        for k, v in rules.items():
            rules[k] = v.replace('"', '').split(' | ')
        print(rules)
        messages = file_data[split_index + 1:]
        print(messages)
    return rules, messages


def expand_string(s, expanded):
    results = set()
    results.add(s)
    for expanded_key, expanded_variants in expanded.items():
        new_results = set()
        for r in results:
            for variant in expanded_variants:
                new_results.add(re.sub(r"\b{}\b".format(expanded_key), variant, r))
        results = new_results
    return results


def do_expand_pass(rules, expanded, verbose=False):
    keys_current_pass = list(expanded.keys())
    complete = dict()
    for rule_key, rule_value in rules.items():
        new_rule_alts = set()
        for rule_alt in rule_value:
            new_rule_alts.update(expand_string(rule_alt, expanded))
        if not any([c.isdigit() for c in ''.join(new_rule_alts)]):
            complete[rule_key] = new_rule_alts
        rules[rule_key] = new_rule_alts

    for k, v in complete.items():
        expanded[k] = [s.replace(' ', '') for s in v]
        del(rules[k])

    for k in keys_current_pass:
        del(expanded[k])

    if verbose:
        print("Rules", rules)
        print("Expanded", expanded)


def do(filename, verbose=False):
    rls, msgs = load(filename)
    exp = dict()

    if verbose:
        print('Rules', rls)
        print('Expanded', exp)
    passes = 0
    while len(rls) > 0:
        print("Starting pass", passes)
        do_expand_pass(rls, exp, verbose)
        passes += 1

    alternatives = exp['0']
    valid_messages = [m for m in msgs if m in alternatives]
    print(f"There are {len(valid_messages)}/{len(msgs)} valid messages and {len(alternatives)} total variants.")
    print("Number of messages of correct length:", len([m for m in msgs if len(m) == 24]))
    print(len(exp['0']), len([m for m in exp['0'] if len(m) == 24]), len(set(exp['0'])))
    return len(valid_messages)


do("AoC-2020-19-test-1.txt", True)

part_1 = do("AoC-2020-19-input.txt")
assert part_1 > 134
