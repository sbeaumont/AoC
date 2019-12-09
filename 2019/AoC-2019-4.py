INPUT = (273025, 767253)


def check_password(p):
    num_list = [int(n) for n in str(p)]
    return (len(set(num_list)) < 6) and (num_list == sorted(num_list))


num_matches = 0
for x in range(INPUT[0], INPUT[1] + 1):
    if check_password(x):
        num_matches += 1

assert check_password(111111)
assert check_password(122345)
assert not check_password(223450)
assert not check_password(123789)

print(num_matches)

assert num_matches == 910
