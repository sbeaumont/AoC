SEED = '1113222113'
ITERATIONS = 50

result = SEED
for i in range(ITERATIONS):
    currentDigit = result[0]
    copies = 0
    newResult = ''
    for c in result:
        if c == currentDigit:
            copies += 1
        else:
            newResult += str(copies) + currentDigit
            currentDigit = c
            copies = 1
    result = newResult + str(copies) + currentDigit

print("The length of the result is", len(result))
