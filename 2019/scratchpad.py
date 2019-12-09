print("Hello 2019!")

num_list = [int(n) for n in str(122345)]
num_list2 = [int(n) for n in str(123245)]
print(num_list == sorted(num_list))
print(num_list2 == sorted(num_list2))
print(num_list)
print(set(num_list))
print(list(str(122345)))
print(set(str(122345)))
print(set(list(str(122345))))


# def gen():
#     for i in (1, 2):
#         yield i
#
#
# g = gen()
# print(next(g))
# print(next(g))
# print(next(g))

from itertools import cycle

c = cycle(range(5))

for i in range(10):
    print(next(c))


print({i: v for i, v in enumerate(['a','b','c'])})