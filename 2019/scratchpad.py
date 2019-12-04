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