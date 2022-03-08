# https://pypi.org/project/bitarray/
from bitarray import bitarray

arr = bitarray()
arr.append(False)
arr.append(True)

print(arr)

arr = bitarray("10111")
print(arr)
print(arr.count(1))
print(arr.remove(1))
print(arr)

arr = bitarray(10)
print(arr)
arr.setall(0)
print(arr)
print(~arr)
print(arr.)