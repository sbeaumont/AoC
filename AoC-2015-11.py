# Policy
# 8 lowercase letters
# 1 increasing straight of 3 letters
# At least 2 different non overlapping pairs of letters
# No letters i, o or l
import re

password = list("vzbxkghb")
LETTERS = "abcdefghjkmnpqrstuvwxyz"
STRAIGHTS = "abc|bcd|cde|def|efg|pqr|qrs|rst|stu|tuv|uvw|vwx|wxy|xyz"
DOUBLES = r"([a-z])\1"

def increment(passwordChars, position):
    digitIndex = LETTERS.index(passwordChars[position])
    if digitIndex + 1 < len(LETTERS):
        passwordChars[position] = LETTERS[digitIndex + 1]
    else:
        passwordChars[position] = LETTERS[0]
        increment(passwordChars, position - 1)

for i in range(2):
    while len(password) <= 8:
        increment(password, -1)
        passwordString = "".join(password)
        doubles = re.findall(DOUBLES, passwordString)
        doublesOK = (len(doubles) >= 2) and (len(set(doubles)) >= 2)
        straightOK = re.search(STRAIGHTS, passwordString)
        if doublesOK and straightOK:
            print("Found new password", passwordString)
            break
