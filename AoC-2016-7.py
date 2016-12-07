#!/usr/bin/env python

"""Solution for the Advent of Code challenge 2016, day 7 part 1."""

__author__ = "Serge Beaumont"
__date__ = "December 2016"

import  re

# Load
with open("AoC-2016-7-data.txt", 'r') as content_file:
    lines = [line.strip() for line in content_file]

# Regex patterns
hyperPattern = re.compile(r'\[(.*?)\]')
nonhyperPattern = re.compile((r'(^|\])([a-z]*?)(\[|$)'))
abbaPattern = re.compile(r'([a-z])(?!\1)([a-z])\2\1')
xyxPattern = re.compile(r'(?=(([a-z])(?!\2)([a-z]\2)))')

# Process
supportTLS = set()
supportSSL = set()
for line in lines:
    # Make two versions of the line, one with hyper parts stripped out, and vice versa
    nonhyperparts = re.sub(hyperPattern, " ", line)
    hyperparts = re.sub(nonhyperPattern, " ", line)

    # Find abba patterns but not in hyper parts for part 1
    if re.search(abbaPattern, nonhyperparts) and not re.search(abbaPattern, hyperparts):
        supportTLS.add(line)

    # Find aba[bab] patterns for part 2
    abas = [match[0] for match in re.findall(xyxPattern, nonhyperparts)]
    for aba in abas:
        # Create the bab of this aba
        bab = (aba + aba[1])[1:]
        if bab in hyperparts:
            supportSSL.add(line)
            break

print("{0} IP's support TLS".format(len(supportTLS)))
print("{0} IP's support SSL".format(len(supportSSL)))