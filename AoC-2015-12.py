FILE_NAME = "santa2015-12-data.json"

import re, json
import collections

with open(FILE_NAME, 'r') as content_file:
    content = content_file.read()

numbers = [int(s) for s in re.findall(r'-?\d+', content)]
print(sum(numbers))

data = json.loads(content)

def traverse(obj):
    if isinstance(obj, dict):
        return {k: traverse(v) for k, v in obj.items()}
    elif isinstance(obj, list):
        return [traverse(elem) for elem in obj]
    else:
        return obj  # no container, just values (str, int, float)

def scan(data):
    for item in data:
        if isinstance(item, dict) and ("red" in item.values()):
            del dict[item]

        if isinstance(item, collections.Iterable):
            scan(item)

print(scan(data))