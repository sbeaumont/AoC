import base64

with open("one.txt") as f:
    data = f.read()

print(base64.b64decode(data, '-_'))