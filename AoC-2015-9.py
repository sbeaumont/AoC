DATA = """AlphaCentauri to Snowdin = 66
AlphaCentauri to Tambi = 28
AlphaCentauri to Faerun = 60
AlphaCentauri to Norrath = 34
AlphaCentauri to Straylight = 34
AlphaCentauri to Tristram = 3
AlphaCentauri to Arbre = 108
Snowdin to Tambi = 22
Snowdin to Faerun = 12
Snowdin to Norrath = 91
Snowdin to Straylight = 121
Snowdin to Tristram = 111
Snowdin to Arbre = 71
Tambi to Faerun = 39
Tambi to Norrath = 113
Tambi to Straylight = 130
Tambi to Tristram = 35
Tambi to Arbre = 40
Faerun to Norrath = 63
Faerun to Straylight = 21
Faerun to Tristram = 57
Faerun to Arbre = 83
Norrath to Straylight = 9
Norrath to Tristram = 50
Norrath to Arbre = 60
Straylight to Tristram = 27
Straylight to Arbre = 81
Tristram to Arbre = 90"""

import itertools

edges = {}
places = set()
for line in DATA.split('\n'):
    splitLine = line.split()
    edges[(splitLine[0], splitLine[2])] = int(splitLine[4])
    edges[(splitLine[2], splitLine[0])] = int(splitLine[4])
    places.add(splitLine[0])
    places.add(splitLine[2])

smallestLength = 9001
smallestRoute = ''
longestLength = 0
longestRoute = ''
for permutation in itertools.permutations(places):
    distance = 0
    for i in range(len(permutation) - 1):
        distance += edges[(permutation[i], permutation[i+1])]
    if distance < smallestLength:
        smallestLength = distance
        smallestRoute = permutation
    if distance > longestLength:
        longestLength = distance
        longestRoute = permutation

print("Smallest route is", smallestRoute, "with length", smallestLength)
print("Longest route is", longestRoute, "with length", longestLength)