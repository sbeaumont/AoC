FILE_NAME = "santa2015-8-data.txt"

import ast

total = 0

f = open(FILE_NAME, "rb")
try:
    for line in f:
        convertedLine = str(line, 'utf-8').rstrip('\n')
        parsedline = ast.literal_eval(convertedLine.rstrip())
        total += len(convertedLine) - len(parsedline)
finally:
    f.close()

print("Total parsed difference", total)
