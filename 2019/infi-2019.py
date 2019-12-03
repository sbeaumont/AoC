"""
For some reason I can't see why Infi won't accept my puzzle. My Santa makes it to the end..?
"""

import json
from pprint import pprint

with open("infi-2019-input.json") as f:
    data = json.load(f)

flats = {k: v for k, v in data['flats']}
pprint(flats)
print(f"Er zijn {len(flats)} flats en {len(data['sprongen'])} sprongen.")
x, y = data['flats'][0]
print(f"Stap 0 (-, -): {x},{y}")

stap = 0
for rechts, omhoog in data['sprongen']:
    assert rechts + omhoog <= 4
    stap += 1
    print(f"Santa gaat {rechts},{omhoog}")
    x = x + 1 + rechts
    y = y + omhoog

    if x in flats:
        if y >= flats[x]:
            print(f"Stap {stap} ({rechts}, {omhoog}): {x},{y}=>{flats[x]}")
            y = flats[x]
        else:
            print(f"Oh jee, te laag: {x},{y} bij flat {x}, {flats[x]}")
            break
    else:
        print(f"Oh jee, geen flat op positie {x}")
        break

print(f"Santa is op zijn bek gegaan na stap {stap}")
