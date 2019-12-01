# {
#     "date": "30-Dec-2018",
#     "readings": [
#         {
#             "contaminants": {
#                 "#16F": 69168,
#                 "#205": 2,
#                 "#281": 3,
#                 "#3F9": 261877,
#                 "#4D4": 33019,
#                 "#5B9": 608497,
#                 "#6F3": 14624,
#                 "#8F5": 13337,
#                 "#B30": 20,
#                 "#B48": 446,
#                 "#B67": 12,
#                 "#C32": 13,
#                 "#CEA": 1,
#                 "#E46": 8,
#                 "#E48": 212,
#                 "#E96": 52
#             },
#             "id": "CD916FB2A88CDA",
#             "time": 0
#         },

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

#F60D 12r3g595