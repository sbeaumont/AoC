"""
Infi 2019 puzzle part 1
"""

import json
from pprint import pprint
from visualize import Visualizer, COLORS

SCALE = 100

with open("infi-2019-input.json") as f:
    data = json.load(f)

flats = {k: v for k, v in data['flats']}
x = min(flats.keys())
y = flats[x]
max_x = max(flats.keys()) + 1
max_y = max(flats.values()) + 1

viz = Visualizer((0, 0, max_x, max_y), scale=SCALE)

for m, n in flats.items():
    viz.draw_line(((m, 0), (m, n)), COLORS[0], width=SCALE)

stap = 0
for rechts, omhoog in data['sprongen']:
    assert rechts + omhoog <= 4
    stap += 1
    new_x = x + 1 + rechts
    new_y = y + omhoog
    viz.draw_polyline(((x, y), (x + 1, y), (new_x, new_y)), COLORS[1], width=SCALE//10)
    viz.draw_point((x, y), COLORS[2], size=SCALE//10)
    x = new_x
    y = new_y

    if (x not in flats) or (y < flats[x]):
        print(f"Santa is op zijn bek gegaan na stap {stap}")
        break

    drop_y = flats[x]
    viz.draw_line(((x, y), (x, drop_y)), COLORS[1])
    y = drop_y

    if x == max(flats.keys()):
        print("Santa heeft de laatste flat gehaald! (Antwoord = 0).")
        break

viz.show()
