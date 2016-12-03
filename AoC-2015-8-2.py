FILE_NAME = "santa2015-8-data.txt"

import re

total = 0

f = open(FILE_NAME, "rb")
try:
    for line in f:
        convertedLine = str(line, 'utf-8').rstrip('\n')
        replacedLine = '"' + re.sub(r'\\|\"', r'\\\g<0>', convertedLine) + '"'
        total += len(replacedLine) - len(convertedLine)
finally:
    f.close()

print("Total parsed difference", total)
