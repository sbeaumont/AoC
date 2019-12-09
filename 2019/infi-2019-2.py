import json
from visualize import Visualizer, COLORS

with open("infi-2019-input.json") as f:
    data = json.load(f)

flats = {k: v for k, v in data['flats']}
x, y = data['flats'][0]

print(flats)

max_x = max(flats.keys()) + 1
max_y = max(flats.values()) + 1
viz = Visualizer((0, 0, max_x, max_y))
for x, y in flats.items():
    viz.draw_line(((x, 0), (x, y)), COLORS[0])
viz.show()
