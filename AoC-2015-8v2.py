FILE_NAME = "santa2015-8-data.txt"

total = 0

f = open(FILE_NAME, "rb")
for line in f:
    convertedLine = str(line, 'utf-8').rstrip('\n')
    rawLength = len(convertedLine)


f.close()

print("Total difference", total)