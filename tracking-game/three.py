# {
#     "regions": [
#         {
#             "regionID": "BE4E78",
#             "readings": [
#                 {
#                     "readingID": "A",
#                     "reading": [
#                         1,
#                         1,
#                         11,
#                         -3,
#                         -4,
#                         10,
#                         19,

#                         ...

#                         258,
#                         262
#                     ],
#                     "date": "1-Dec-2018"
#                 },
#                 {
#                     "readingID": "B",
#                     "reading": [
#                         0,
#                         -1,
#                         12,
#                         -4,


import json
from collections import defaultdict
from pprint import pprint
from datetime import datetime


with open("flood.json") as f:
    data = json.load(f)


def water_in_region(reading):
    last_peak_pos = 0
    last_peak_height = reading[last_peak_pos]

    under_water = list()
    lake = list()
    for i in range(0, len(reading)):
        current_level = reading[i]
        if current_level < last_peak_height:
            lake.append(last_peak_height - current_level)
        else:
            if lake:
                under_water.extend(lake)
                lake = list()
            last_peak_pos = i
            last_peak_height = reading[last_peak_pos]

    last_peak_forward = last_peak_pos
    last_peak_height = reading[-1]
    for j in range(len(reading) - 1, last_peak_forward - 1, -1):
        current_level = reading[j]
        if current_level < last_peak_height:
            under_water.append(last_peak_height - current_level)
        else:
            last_peak_height = reading[j]

    # print(reading, under_water, sum(under_water))
    return sum(under_water)


assert water_in_region((1, 1, 1, 1)) == 0
assert water_in_region((1, 1, 1, 0, 1)) == 1
assert water_in_region((4, 2, 3, 0, 8, 0, 8)) == 15
assert water_in_region((4, 2, 3, 0, 8, 0, 8, 0, 2, 0, 1)) == 18
assert water_in_region((1, 2, 1, 0, 1, 3, 2, 1, 0, 1)) == 5
assert water_in_region((1, 2, 1, 0, 1, 3, 2, 1, 0, 1, 2, 1, 3)) == 15
assert water_in_region((20, 0, 15)) == 15
assert water_in_region((15, 0, 20)) == 15

print(water_in_region(data['regions'][0]['readings'][0]['reading']))

region_totals = defaultdict(list)
for region in data['regions']:
    readings = region['readings']
    regionID = region['regionID']
    for reading_at_date in readings:
        volume = water_in_region(reading_at_date['reading'])
        region_totals[regionID].append((reading_at_date['readingID'], reading_at_date['date'], volume))

# pprint(region_totals)

weird_regions = list()
for region in region_totals.values():
    for i in range(1, len(region)):
        if abs(region[i][2] - region[i-1][2]) > 1000:
            weird_regions.append(region[i])


for r in weird_regions:
    print(r)

print('===')

print(''.join([r[0] for r in weird_regions]))
