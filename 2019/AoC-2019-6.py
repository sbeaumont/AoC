"""
My naive-because-I-suck-at-programming-but-it-works solution
"""

from norvigutils import load_input


class ObjectInSpace(object):
    def __init__(self, name):
        self.name = name
        self.parent = None
        self.children = list()

    def add_child(self, obj):
        self.children.append(obj)
        obj.parent = self

    def parents(self, names=False):
        if self.parent:
            pts = self.parent.parents(names)
            pts.append(self.parent.name if names else self.parent)
        else:
            pts = list()
        return pts

    @property
    def num_parents(self):
        return len(self.parents())

    def __repr__(self):
        return f"ObjectInSpace('{self.name}')"


objects_in_space = dict()


def find_object(o):
    if o not in objects_in_space:
        objects_in_space[o] = ObjectInSpace(o)
    return objects_in_space[o]


for line in load_input(6):
    a, b = line.strip().split(')')
    find_object(a).add_child(find_object(b))

orbits = 0
for o in objects_in_space.values():
    orbits += o.num_parents

print("Part 1", orbits)

assert orbits == 158090

you = objects_in_space['YOU']
san = objects_in_space['SAN']
you_parents = you.parents(True)[::-1]
san_parents = san.parents(True)[::-1]

for n in you_parents:
    if n in san_parents:
        you_to_common = you_parents[:you_parents.index(n)+1]
        san_to_common = san_parents[:san_parents.index(n)+1]
        # Count the common parent once
        # Don't count the object you're currently orbiting.
        orbital_transfers = len(you_to_common) + len(san_to_common) - 2
        assert orbital_transfers == 241
        print("Part 2", orbital_transfers)
        break
