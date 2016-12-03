with open("santa2016-3-data.txt", 'r') as content_file:
    content = content_file.read()

content = content.split('\n')
possible = 0
print("Total number of triplets", len(content))
for i in range(0, len(content), 3):
    lines = []
    for j in range(3):
        lines.append([int(s) for s in content[i+j].split()])
    lines = list(map(list, zip(*lines)))
    for line in lines:
        line.sort()
        if line[2] < line[0] + line[1]:
            possible += 1
            print(line[2], "<", line[0], "+", line[1])
        else:
            print(line[2], ">=", line[0], "+", line[1])
print("Possible triangles", possible)