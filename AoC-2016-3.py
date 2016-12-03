with open("santa2016-3-data.txt", 'r') as content_file:
    content = content_file.read()

possible = 0
for line in content.split('\n'):
    sides = [int(s) for s in line.split()]
    sides.sort()
    if sides[2] < sides[0] + sides[1]:
        possible += 1
print("Possible triangles", possible)