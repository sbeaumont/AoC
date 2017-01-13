
#!/usr/bin/env python

"""Solution for the Advent of Code challenge 2016, day 14."""

__author__ = "Serge Beaumont"
__date__ = "December 2016"

SALT = 'cuanljph'
#SALT = 'abc'

import hashlib, re
from collections import defaultdict

m = hashlib.md5()

threePattern = re.compile(r'([a-z0-9])\1{2}')
fivePattern = re.compile(r'(\w)\1{4}')

keys = []
candidateKeys = defaultdict(list)

def generateKey(index):
    hashString = SALT + str(index)
    m = hashlib.md5(bytes(hashString, 'utf-8'))
    currentHash = m.hexdigest()
    for i in range(2016):
        currentHash = hashlib.md5(bytes(currentHash, 'utf-8')).hexdigest()
    return currentHash

def tryThreeKey(index, key):
    if re.search(threePattern, key):
        character = re.search(threePattern, key).group(1)
        candidateKeys[character].append((index, key))

def tryFiveKey(index, key):
    for fiveMatch in re.findall(fivePattern, key):
        character = fiveMatch[0]
        if character in candidateKeys.keys():
            candidateKeysToRemove = []
            for keyIndex, candidateKey in candidateKeys[character]:
                if (index != keyIndex) and (index - keyIndex < 1000):
                    keys.append((keyIndex, candidateKey))
                    candidateKeysToRemove.append((keyIndex, candidateKey))
                    print("{4}: Found key {0} at index {1} that has a five character ({5}) sibling {2} at index {3}".format(candidateKey, keyIndex, key, index, len(keys), character))
            if candidateKeysToRemove:
                candidateKeys[character] = [item for item in candidateKeys[character] if item not in candidateKeysToRemove]

index = 0
while len(keys) < 64:
    key = generateKey(index)
    tryThreeKey(index, key)
    tryFiveKey(index, key)
    index += 1

keynr = 1
for index, key in sorted(keys):
    print("{2}: {0} / {1}".format(index, key, keynr))
    keynr += 1