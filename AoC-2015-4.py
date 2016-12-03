import hashlib

secret = 'bgvyzdsv'
number = 0
answer = "not found"

while number < 1000000000:
    hashString = secret + str(number)
    md = hashlib.md5(bytes(hashString, 'utf-8'))
    hexdigest = md.hexdigest()
    if str(hexdigest)[0:6] == '000000':
        answer = number
        break
    if number % 1000000 == 0:
        print(number)
    number += 1

print("Done. Answer:", answer)

