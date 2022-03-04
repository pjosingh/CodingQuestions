ugly_list = [10,12,36,[41,59,63],[77],81,93]
flat = []
for i in ugly_list:
    if isinstance(i, list): flat.extend(i)
    else: flat.append(i)
print(flat)


list1 = [1,2,3]
list2 = [3,4]
list1.append(list2)
print(list1)

list3 = [1,2,3]
list3.extend(list2)
print(list3)