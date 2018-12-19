BIG_NUMBER = 10551358

a = 0
e = 1
while e <= BIG_NUMBER:
    if BIG_NUMBER % e == 0:
        a += e
    e += 1

print(a)

assert a == 15827040