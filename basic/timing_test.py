import time
from dll import Dll

a = [i/2 for i in range(200000)]
#print(a)

start = time.time()
a.pop()
end = time.time()
print(f'pop: {(end-start)*100000}')
first = (end-start)

start = time.time()
del(a[int(200000/2)])
end = time.time()
second = (end-start)
print(f'pop: {(end-start)*100000}')

print(f' difference: {second/first}')


# using dll
dll = Dll()
node_to_delete = None
for el in a:
    node = dll.addToFront(el)
    if (el == a[int(200000/2)]):
        node_to_delete = node

start = time.time()
dll.remove(node_to_delete)
end = time.time()
third = (end-start)
print(f' difference2: {third/first}')

#dll.print()
print(f'node to delete: {node_to_delete.val}')

