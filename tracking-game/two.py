"""
Solution for part two of Reaktor's puzzle.
"""

from binascii import hexlify
import json
from base64 import b64decode
from pprint import pprint

with open("two.txt") as f:
    raw = f.read().strip()
    data = raw.split(' ')

decoded = ''.join([chr(int(x, 2)) for x in data])
parsed = json.loads(decoded)

# print(json.dumps(parsed, indent=4, sort_keys=True))

all_totals = list()
for readings_day in parsed:
    for reading in readings_day['readings']:
        total = 0
        for contaminant_value in reading['contaminants'].values():
            total += int(contaminant_value)
        if total > 1010000:
            # pprint(reading)
            spike_id = reading['id']
            # print(f"Found spike at {readings_day['date']}, {reading['time']} with ID {spike_id}")

letters = list()
for i in range(0, len(spike_id), 2):
    c = int(spike_id[i:i+2], 16)
    letters.append(chr(c))
result = ''.join(letters)

print(f"The spike happened at {result}")
