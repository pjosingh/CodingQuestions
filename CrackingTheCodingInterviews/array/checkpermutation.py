def checkperm(str1, str2):
    list1 = []
    for el in str1:
        list1.append(el)
    list2 = []
    for el in str2:
        list2.append(el)
    
    list1.sort()
    list2.sort()
    return list1 == list2


## testing

print(checkperm("god","dog"))
print(checkperm("god","dogg"))
    