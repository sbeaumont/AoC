INPUT = (273025, 767253)


def check_password(p):
    num_list = [int(n) for n in str(p)]
    ok_so_far = (len(set(num_list)) < 6) and (num_list == sorted(num_list))
    if ok_so_far:
        found_double = False
        for c in set(num_list):
            if num_list.count(c) == 2:
                found_double = True
                break
    return ok_so_far and found_double


num_matches = 0
for x in range(INPUT[0], INPUT[1] + 1):
    if check_password(x):
        num_matches += 1

assert not check_password(111111)
assert check_password(111122)
assert not check_password(112211)
assert check_password(122345)
assert not check_password(223450)
assert not check_password(123789)

print(num_matches)
