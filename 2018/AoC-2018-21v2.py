r = [0, 0, 0, 0, 0, 0]

while r[5] != 72:
    r[5] = 123
    r[5] = r[5] & 456
r[5] = 0
# C
r[2] = r[5] | 65536
r[5] = 10362650
# B
r[5] += r[2] | 255
r[5] = r[5] & 16777215
r[5] = r[5] * 65899
r[5] = r[5] & 16777215
# E
r[4] = 256 > r[2]
r[3] = r[4] + r[3]
r[3] += 3
# Jump to A
r[4] = 0
r[1] = r[4] + 1
r[1] = r[1] * 256
if r[1] <= r[2]:
    r[4] += 1
# Jump to E

# A, D
r[2] = r[4]
# Jump to B
r[4] = 1 if r[5] == r[0] else 0
r[3] += r[4]
# Jump to C