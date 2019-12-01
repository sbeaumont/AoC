import base64

# Q3VydGlzaXNsYW5k wrong

with open("one.txt") as f:
    data = f.read()

i = 0
result = ''
while not result:
    s = data[i:i+16]
    if sorted(s) == sorted(''.join(set(s))):
        result = s
    i += 1

print(result, 'decodes to', str(base64.b64decode(result)))
