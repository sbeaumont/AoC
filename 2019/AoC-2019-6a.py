from norvigutils import load_input
import networkx as nx

g = nx.DiGraph()

for line in load_input(6):
    a, b = line.strip().split(')')
    g.add_edge(a, b)

root = list(nx.topological_sort(g))[0]

g2 = g.to_undirected()

orbits = 0
for n in g2:
    orbits += nx.shortest_path_length(g2, n, root)

print(f"Part 1: {orbits} orbits.")
assert orbits == 158090

hops = nx.shortest_path_length(g2, 'YOU', 'SAN') - 2

print(f"Part 2: distance from YOU to SAN = {hops}.")
assert hops == 241
